import socket
import sys
import time

from dvbctrl.errors import errorNotify, DVBConnectionError, makeError


class ControlConnection:
    """Class implementing a connection to a DVBStreamer daemon."""

    def __init__(self, host, adapter):
        """Create a connection object to talk to a DVBStreamer daemon."""
        try:
            self.host = host
            self.adapter = adapter
            self.opened = False
            self.authenticated = False
            self.welcomemsg = None
            self.myip = None
            self.lastsuccess = 0
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def expired(self):
        try:
            now = time.time()
            return now > (self.lastsuccess + 5)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def open(self):
        """Open the connection to the DVBStreamer daemon."""
        try:
            if self.opened:
                return self.opened
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.adapter + 54197))
            self.authenticated = False
            self.myip = self.socket.getsockname()[0]
            self.socketfile = self.socket.makefile("r")
            self.opened = True
            errorcode, errormessage, lines = self.readResponse()
            if errorcode != 0:
                self.socket.close()
                self.opened = False
            else:
                self.welcomemsg = errormessage
            return self.opened
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def close(self):
        """Close the connection to the DVBStreamer daemon."""
        try:
            if self.opened:
                self.sendCommand("logout")
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
        finally:
            if self.opened:
                self.socketfile.close()
                self.socket.close()
                self.opened = False

    def sendCommand(self, command):
        """
        Send a command to the DVBStreamer daemon connection.
        @param command: Command to send to the server.
        """
        try:
            if not self.opened:
                raise DVBConnectionError("not connected")
            self.socketfile.write(f"{command}\n")
            self.socketfile.flush()
            self.lastsuccess = time.time()
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def readResponse(self):
        """
        Read a response from the DVBStreamer deamon after a command has been sent.
        Returns a tuple of error code, error message and response lines.
        """
        try:
            morelines = True
            lines = []
            errorcode = -1
            errormessage = ""
            while morelines:
                line = self.socketfile.readline()
                if line.startswith("DVBStreamer/"):
                    morelines = False
                    sections = line.split("/")
                    self.version = sections[1]
                    errorsections = sections[2].split(" ", 1)
                    errorcode = int(errorsections[0])
                    if len(errorsections) > 1:
                        errormessage = errorsections[1].strip()
                    else:
                        errormessage = ""
                elif line == "":
                    morelines = False
                else:
                    lines.append(line.strip("\n\r"))
            self.lastsuccess = time.time()
            return (errorcode, errormessage, lines)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def executeCommand(self, command):
        """
        Send command and wait for response
        Returns a tuple of error message and response lines if the return error code was 0,
        otherwise a DVBStreamerError is raised.
        """
        try:
            self.sendCommand(command)
            errorcode, errormessage, lines = self.readResponse()
            if errorcode != 0:
                raise makeError(errorcode, errormessage, lines)
            return (errormessage, lines)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def authenticate(self, username, password):
        """
        Authenticate the connection allowing it to execute more commands.
        """
        try:
            errormessage, lines = self.executeCommand(f'auth "{username}" "{password}"')
            self.authenticated = True
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
