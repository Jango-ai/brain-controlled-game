require("js/brain-link.js");

var selectedBrainControlSystem = "lsl";

var brainControlSystems = {
  lsl: connectToEventServer,
  muse: connectToMuse
};

$(".btn-radio").click(e => {
  input = $(e.target).find("input")[0];
  selectedBrainControlSystem = input.attributes.brainControlSystemType.value;
  console.log("Selected brain interface type: ", selectedBrainControlSystem);
});

connectToBrainInterface = () => {
  brainControlSystems[selectedBrainControlSystem]();
};
