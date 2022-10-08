# dvbctrl

## starting

```python
from dvbctrl.dvbstreamer import DVBStreamer

adaptor = 0
dvbs = DVBStreamer(adaptor)
running = dvbs.start()
if not running:
    raise Exception(f"Failed to start dvbstreamer on adaptor {adaptor}")
```

## stopping

```python
from dvbctrl.dvbstreamer import DVBStreamer

adaptor = 0
dvbs = DVBStreamer(adaptor)

...

if dvbs.isRunning():
    dvbs.stop()
```
