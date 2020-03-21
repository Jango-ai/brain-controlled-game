require("rxjs/add/operator/filter");
require("rxjs/add/operator/map");

const { MuseClient, channelNames } = require("muse-js");

function dispatchSpacebarKeydownEvent() {
  const jumpEvent = new Event("keydown");
  jumpEvent.keyCode = 32; // Space key
  document.dispatchEvent(jumpEvent);
}

async function connectToMuse() {
  const client = new MuseClient();
  await client.connect();
  await client.start();

  const leftChannel = channelNames.indexOf("AF7"); // Left eye electrode
  const blinks = client.eegReadings
    .filter(r => r.electrode === leftChannel)
    .map(r => Math.max(...r.samples.map(Math.abs)))
    .filter(max => max > 400);

  blinks.subscribe(() => {
    dispatchSpacebarKeydownEvent();
  });
}

async function connectToEventServer() {
  console.log("Connecting to event server...");
  const source = new EventSource("http://127.0.0.1:50005/events");
  source.addEventListener(
    "artifact",
    function(event) {
      console.log("Artifact detected: ", event.data);
      dispatchSpacebarKeydownEvent();
    },
    false
  );
}

window.connectToMuse = connectToMuse;
window.connectToEventServer = connectToEventServer;
