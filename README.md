# dvbctrl

Module to control a local [dvbstreamer](http://sourceforge.net/projects/dvbstreamer/).  On Arch you can install dvbstreamer from
the [AUR](https://aur.archlinux.org/packages/dvbstreamer).

## starting

```python
from dvbctrl.dvbstreamer import DVBStreamer

adapter = 0
dvbs = DVBStreamer(adapter)
running = dvbs.start()
if not running:
    raise Exception(f"Failed to start dvbstreamer on adapter {adapter}")
```

## stopping

```python
from dvbctrl.dvbstreamer import DVBStreamer

adapter = 0
dvbs = DVBStreamer(adapter)

...

if dvbs.isRunning():
    dvbs.stop()
```

## commands

```python
from dvbctrl.commands import DVBCommand

kwargs = {
    "adapter": 0,
    "host": "127.0.0.1"
    "pass": "dvbctrl"
    "user": "dvbctrl"
}
dvbc = DVBCommand(**kwargs)

# services (channels)
chans = dvbc.lsservices()
```

## recorder

A simple interface to dvbctrl to easily record to files from channels.  Utilises the primary service filter only.

```
from dvbctrl.recorder import Recorder

# initialise the recorder
r = Recorder("BBC TWO", "/tmp/bbc_two.ts", adapter=0)

# start the recorder, this checks that the file is growing
r.start()

...

# stop the recording
r.stop()
```

You can periodically check that the recording file is still growing by using the check function, passing in the last file size.
This returns a tuple containing a True/False flag and the current size.  If the flag is False (i.e. the file isn't growing or is
not there) then the lastsize argument is returned.

```
isok, currentsize = r.check(12345)
```
## dvbctrl recorder commands

* `tuneToChannel()` Tunes the dvbstreamer to a channel will wait up to 5 seconds for dvbstreamer to stabilise. Returns True if
  tuned or False otherwise
* `isTuned()` returns True if tuned, False otherwise
* `waitTuned()` waits for up to 5 seconds for the streamer to tune returns True if tuned successfully, False otherwise

## dvbctrl commands

* `select` Select a new service to stream.
* `setmrl` Set the MRL of the primary service filter.
* `getmrl` Get the primary service filter MRL.
* `addsf` Add a service filter.
* `rmsf` Remove a service filter.
* `lssfs` List all service filters.
* `setsf` Set the service to be filtered by a service filter.
* `getsf` Get the service to stream to a secondary service output.
* `setsfmrl` Set the service filter's MRL.
* `getsfmrl` Get the service filter's MRL.
* `setsfavsonly` Enable/disable streaming of Audio/Video/Subtitles only.
* `getsfavsonly` Get whether Audio/Video/Subtitles only streaming is enabled.
* `lsservices` List all services or for a specific multiplex.
* `lsmuxes` List multiplexes.
* `lspids` List the PIDs for a specified service.
* `current` Print out the service currently being streamed.
* `serviceinfo` Display information about a service.
* `muxinfo` Display information about a mux.
* `stats` Display the stats for the PAT,PMT and service PID filters.
* `festatus` Displays the status of the tuner.
* `scan` Scan the specified multiplex(es) for services.
* `cancelscan` Cancel the any scan that is in progress.
* `lslcn` List the logical channel numbers to services.
* `findlcn` Find the service for a logical channel number.
* `selectlcn` Select the service from a logical channel number.
* `lsmfs` List current filters.

### dvbctrl commands not yet implemented

* `feparams` Get current frontend parameters. (NOT IMPLEMENTED)
* `lsprops` List available properties. (NOT IMPLEMENTED)
* `getprop` Get the value of a property. (NOT IMPLEMENTED)
* `setprop` Set the value of a property. (NOT IMPLEMENTED)
* `propinfo` Display information about a property. (NOT IMPLEMENTED)
* `dumptsr` Dump information from the TSReader (NOT IMPLEMENTED)
* `lslnbs` List known LNBs (NOT IMPLEMENTED)
* `epgdata` Register to receive EPG data in XML format. (NOT IMPLEMENTED)
* `date` Display the last date/time received. (NOT IMPLEMENTED)
* `enabledsmcc` Enable DSM-CC data download for the specified service filter. (NOT IMPLEMENTED)
* `disabledsmcc` Disable DSM-CC data download for the specified service filter. (NOT IMPLEMENTED)
* `dsmccinfo` Display DSM-CC info for the specified service filter. (NOT IMPLEMENTED)
* `epgcaprestart` Starts or restarts the capturing of EPG content. (NOT IMPLEMENTED)
* `epgcapstart` Starts the capturing of EPG content. (NOT IMPLEMENTED)
* `epgcapstop` Stops the capturing of EPG content. (NOT IMPLEMENTED)
* `now` Display the current program on the specified service. (NOT IMPLEMENTED)
* `next` Display the next program on the specified service. (NOT IMPLEMENTED)
* `addlistener` Add a destination to send event notification to. (NOT IMPLEMENTED)
* `rmlistener` Remove a destination to send event notification to. (NOT IMPLEMENTED)
* `lslisteners` List all registered event listener (NOT IMPLEMENTED)
* `addlistenevent` Add an internal event to monitor. (NOT IMPLEMENTED)
* `rmlistenevent` Remove an internal event to monitor (NOT IMPLEMENTED)
* `lslistenevents` List all registered event listener (NOT IMPLEMENTED)
* `addmf` Add a new destination for manually filtered PIDs. (NOT IMPLEMENTED)
* `rmmf` Remove a destination for manually filtered PIDs. (NOT IMPLEMENTED)
* `setmfmrl` Set the filter's MRL. (NOT IMPLEMENTED)
* `addmfpid` Adds a PID to a filter. (NOT IMPLEMENTED)
* `rmmfpid` Removes a PID from a filter. (NOT IMPLEMENTED)
* `lsmfpids` List PIDs for filter. (NOT IMPLEMENTED)
* `addoutput` Add a new output. (NOT IMPLEMENTED)
* `rmoutput` Remove an output. (NOT IMPLEMENTED)
* `enablesicap` Enable the capture of PSI/SI data. (NOT IMPLEMENTED)
* `disablesicap` Disable the capture of PSI/SI data. (NOT IMPLEMENTED)
* `lsplugins` List loaded plugins. (NOT IMPLEMENTED)
* `plugininfo` Display the information about a plugin. (NOT IMPLEMENTED)
* `who` Display current control connections. (NOT IMPLEMENTED)
* `auth` Login to control dvbstreamer. (NOT IMPLEMENTED)
* `logout` Close the current control connection. (NOT IMPLEMENTED)
* `quit` Exit the program. (NOT IMPLEMENTED)
* `help` Display the list of commands or help on a specific command. (NOT IMPLEMENTED)
