# Brain-controlled game

Game controlled via a Brain-Computer Interface (BCI).

Blinking fires the spacebar `keydown` event.

Based on [`urish/t-rex-brainer`](https://github.com/urish/t-rex-brainer) but modified so it can also ingest data from an EEG LSL server.

## Instructions

### 1. Get the code

First, clone this repo

```
git clone https://github.com/rameerez/brain-controlled-game.git
```

And then `cd` into it

```
cd brain-controlled-game
```

### 2. Start up the client web server

Install dependencies

```
npm intsall
```

And start up the web server

```
live-server
```


### 3. Start up the Python event server

`cd` into the Python server folder

```
cd python_event_server
```

Install dependencies
```
pip install flask flask-sse redis gunicorn gevent mne
pip install https://api.github.com/repos/mne-tools/mne-realtime/zipball/master
```

Install redis on your machine (if needed)
```
brew install redis # for macOS
```

Run a local redis server
```
redis-server /usr/local/etc/redis.conf
```

And finally fire up the Python Flask server:
```
gunicorn main:app --worker-class gevent --bind 127.0.0.1:50005
```