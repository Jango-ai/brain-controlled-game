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

Set up the `FLASK_APP` var

```
export FLASK_APP=main.py
```

And finally fire up the Python Flask server:

```
flask run --host=0.0.0.0 --port=50005
```