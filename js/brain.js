require("rxjs/add/operator/filter");
require("rxjs/add/operator/map");

const { MuseClient, channelNames } = require("muse-js");

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
    const jumpEvent = new Event("keydown");
    jumpEvent.keyCode = 32; // Space key
    document.dispatchEvent(jumpEvent);
  });
}

async function connectToEventServer() {
  // TODO connect to local Python server
  // const source = new EventSource("demo_sse.php");
  // source.onmessage = function(event) {
  //     document.getElementById("result").innerHTML += event.data + "<br>";
  // };
}

window.connectToMuse = connectToMuse;
window.connectToEventServer = connectToEventServer;
