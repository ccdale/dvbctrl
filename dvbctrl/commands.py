"""commands module for dvbstreamer control."""
import sys

from dvbctrl.connection import ControlConnection
from dvbctrl.errors import errorNotify


# commands:
#         quit - Exit the program.
#         help - Display the list of commands or help on a specific command.
#       select - Select a new service to stream.
#       setmrl - Set the MRL of the primary service filter.
#       getmrl - Get the primary service filter MRL.
#        addsf - Add a service filter.
#         rmsf - Remove a service filter.
#        lssfs - List all service filters.
#        setsf - Set the service to be filtered by a service filter.
#        getsf - Get the service to stream to a secondary service output.
#     setsfmrl - Set the service filter's MRL.
#     getsfmrl - Get the service filter's MRL.
# setsfavsonly - Enable/disable streaming of Audio/Video/Subtitles only.
# getsfavsonly - Get whether Audio/Video/Subtitles only streaming is enabled.
#   lsservices - List all services or for a specific multiplex.
#      lsmuxes - List multiplexes.
#       lspids - List the PIDs for a specified service.
#      current - Print out the service currently being streamed.
#  serviceinfo - Display information about a service.
#      muxinfo - Display information about a mux.
#        stats - Display the stats for the PAT,PMT and service PID filters.
#     festatus - Displays the status of the tuner.
#     feparams - Get current frontend parameters.
#      lsprops - List available properties.
#      getprop - Get the value of a property.
#      setprop - Set the value of a property.
#     propinfo - Display information about a property.
#      dumptsr - Dump information from the TSReader
#       lslnbs - List known LNBs
#         scan - Scan the specified multiplex(es) for services.
#   cancelscan - Cancel the any scan that is in progress.
#      epgdata - Register to receive EPG data in XML format.
#         date - Display the last date/time received.
#  enabledsmcc - Enable DSM-CC data download for the specified service filter.
# disabledsmcc - Disable DSM-CC data download for the specified service filter.
#    dsmccinfo - Display DSM-CC info for the specified service filter.
# epgcaprestart - Starts or restarts the capturing of EPG content.
#  epgcapstart - Starts the capturing of EPG content.
#   epgcapstop - Stops the capturing of EPG content.
#          now - Display the current program on the specified service.
#         next - Display the next program on the specified service.
#  addlistener - Add a destination to send event notification to.
#   rmlistener - Remove a destination to send event notification to.
#  lslisteners - List all registered event listener
# addlistenevent - Add an internal event to monitor.
# rmlistenevent - Remove an internal event to monitor
# lslistenevents - List all registered event listener
#        lslcn - List the logical channel numbers to services.
#      findlcn - Find the service for a logical channel number.
#    selectlcn - Select the service from a logical channel number.
#        addmf - Add a new destination for manually filtered PIDs.
#         rmmf - Remove a destination for manually filtered PIDs.
#        lsmfs - List current filters.
#     setmfmrl - Set the filter's MRL.
#     addmfpid - Adds a PID to a filter.
#      rmmfpid - Removes a PID from a filter.
#     lsmfpids - List PIDs for filter.
#    addoutput - Add a new output.
#     rmoutput - Remove an output.
#  enablesicap - Enable the capture of PSI/SI data.
# disablesicap - Disable the capture of PSI/SI data.
#    lsplugins - List loaded plugins.
#   plugininfo - Display the information about a plugin.
#          who - Display current control connections.
#         auth - Login to control dvbstreamer.
#       logout - Close the current control connection.


class DVBCommand(ControlConnection):
    """Class implementing control commands for a DVBStreamer daemon."""

    def __init__(self, adaptor=0, host=None, user="dvbctrl", passw="dvbctrl"):
        try:
            super().__init__(adaptor, host, user, passw)
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)

    def lslcn(self):
        """List the logical channel numbers to services."""
        try:
            errmsg, lines = self.doCommand("lslcn")
            return lines
        except Exception as e:
            errorNotify(sys.exc_info()[2], e)
