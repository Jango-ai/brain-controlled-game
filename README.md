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

And then `cd` into it

```
cd brain-controlled-game
```

### 2. Start up the client web server

Let's first display the actual game window.

Install dependencies

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

Open up a new console, `cd` into the project folder and then `cd` into the Python server folder

```
cd python_event_server
```

Install dependencies

```
pip install flask flask-sse redis gunicorn gevent mne
pip install https://api.github.com/repos/mne-tools/mne-realtime/zipball/master
```

Now, we need Redis to allow the Python server message system to work. Install and run redis on your machine:

#### Redis on macOS

```
brew install redis
```

And then run the local redis server

```
redis-server /usr/local/etc/redis.conf
```

#### Redis on Windows

Download the `Latest release` compiled version of Redis: https://github.com/microsoftarchive/redis/releases/download/win-3.0.504/Redis-x64-3.0.504.zip

Uncompress the `.zip` file and execute `redis-server.exe`

A black terminal screen with the Redis logo should pop up indicating that a local server of Redis is now up and running.

#### Redis on Linux

// TODO search for redis installation instructions on Linux

-----------------

Once Redis is installed and running, fire up the Python event server:

```
gunicorn main:app --worker-class gevent --bind 127.0.0.1:50005
```

And everything should be set up now.