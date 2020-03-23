# Brain-controlled game

Game controlled via a Brain-Computer Interface (BCI).

Blinking fires the spacebar `keydown` event.

Based on [`urish/t-rex-brainer`](https://github.com/urish/t-rex-brainer) but modified so it can also ingest data from an EEG LSL server.

![Game screenshot](/assets/game-screenshot.png)

## Instructions

### 0. LSL Server

First of all, you need to have a LSL server streaming EEG data. Use [Notebook 3a](https://github.com/rameerez/brain-computer-interfacing/blob/master/course/session3a-neurofeedback_streaming_data_with_mock_lsl_server.ipynb) from the [Brain-Computer Interfacing Bootcamp Course repo](https://github.com/rameerez/brain-computer-interfacing) to start up a mock LSL server that streams EEG data from a dataset.

### 1. Get the code

Start by cloning this repo

```
git clone https://github.com/rameerez/brain-controlled-game.git
```

And then `cd` into it, in whichever folder you put it

```
cd brain-controlled-game
```

### 2. Start up the client web server

Let's first display the actual game window.

Install dependencies within the cd brain-controlled-game, if you do not have them yet

```
npm install
npm install -g live-server
```

And start up the web server

```
live-server
```

### 3. Start up the Python event server

Now, we need a Python `flask` server that sends events to the game web window. The goal of this "event server" is to read EEG data from a LSL streaming and fire events when it detects the right artifacts.

`cd` into the Python server folder

```
cd python_event_server
```

Install dependencies (within your coding environment. Anaconda prompt in my case)

```
pip install flask flask-sse redis gunicorn gevent mne
pip install https://api.github.com/repos/mne-tools/mne-realtime/zipball/master
```

Install redis on your machine.
If you're using Linux/Windows, you have to look elsewhere.
I found redis here and downloaded version 3.0.504  https://github.com/microsoftarchive/redis/releases
```
brew install redis  # for macOS
```

Run a local redis server
Or if you downloaded it in Windows, double click on redis-server.exe
```
redis-server /usr/local/etc/redis.conf  # for macOS
```

And finally fire up the Python Flask server:
For Windows you have here how to make it work https://stackoverflow.com/questions/1422368/fcntl-substitute-on-windows/25471508#25471508
```
gunicorn main:app --worker-class gevent --bind 127.0.0.1:50005
```
