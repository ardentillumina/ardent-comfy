import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "ArdentNodes.CLIPEncodePositivePromptOnly",

    async setup() {
        // console.log("CLIPEncodePositivePromptOnly setup");
    },

    async nodeCreated(node) {
        // console.log("CLIPEncodePositivePromptOnly nodeCreated", node);
    },
});
