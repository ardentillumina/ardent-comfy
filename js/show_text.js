import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";


const textAreaStyles = {
    readOnly: true,
    opacity: 1,
    padding: '2px',
    paddingLeft: '7px',
    border: '1px solid #999',
    borderRadius: '4px',
    backgroundColor: '#333',
    color: 'Lime',
    fontFamily: 'Arial, sans-serif',
    fontSize: '12px',
    lineHeight: '1.2',
    resize: 'none',
    overflowY: 'auto',
};


app.registerExtension({
    name: "ArdentNodes.ShowText",

    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name !== "ShowText") return;

        function populate(text) {
            if (typeof text !== 'string') {
                console.warn("populate expects a string, got:", text);
                return;
            }

            if (this.widgets) {
                const pos = this.widgets.findIndex((w) => w.name === "preview");
                if (pos !== -1) {
                    for (let i = pos; i < this.widgets.length; i++) {
                        this.widgets[i].onRemove?.();
                    }
                    this.widgets.length = pos;
                }
            } else {
                this.widgets = [];
            }

            const existingWidget = this.widgets.find(w => w.name === "preview" && w.value === text);
            if (!existingWidget) {
                console.log("Creating new widget with text:", text);

                const w = ComfyWidgets["STRING"](this, "preview", ["STRING", { multiline: true }], app).widget;
                w.inputEl.readOnly = true;
                Object.assign(w.inputEl.style, textAreaStyles);

                w.value = text;
            }

            requestAnimationFrame(() => {
                const sz = this.computeSize();
                if (sz[0] < this.size[0]) sz[0] = this.size[0];
                if (sz[1] < this.size[1]) sz[1] = this.size[1];
                this.onResize?.(sz);
                app.graph.setDirtyCanvas(true, false);
            });
        }


        const onExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            onExecuted?.apply(this, arguments);
            populate.call(this, message.text.join('').trim());
        };

        const onConfigure = nodeType.prototype.onConfigure;
        nodeType.prototype.onConfigure = function () {
            onConfigure?.apply(this, arguments);
            if (this.widgets_values?.length) {
                populate.call(this, this.widgets_values);
            }
        };
    },
});
