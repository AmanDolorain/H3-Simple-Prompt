import { app } from "../../scripts/app.js";

// Retain this filename so upgrading from the experimental multi-field release is safe.
function mergeLegacy(values) {
    const nonempty = value => typeof value === "string" && value.trim().length > 0;
    if (values.length === 1) return values[0] ?? "";
    const parts = [];
    if (nonempty(values[0])) parts.push(values[0]);
    for (const [index, heading] of [[1,"subject_definitions"],[2,"summary"],[3,"retention_analysis"]]) {
        if (nonempty(values[index])) parts.push(heading + ":\n" + values[index]);
    }
    const detail = values.slice(4, 9).filter(nonempty);
    if (detail.length) parts.push("detailed_description:\n" + detail.join("\n\n"));
    for (const [index, heading] of [[9,"overall_soundscape"],[10,"non_diegetic_music"]]) {
        if (nonempty(values[index])) parts.push(heading + ":\n" + values[index]);
    }
    return parts.join("\n\n");
}
app.registerExtension({
    name: "AmanSimplePrompt.SingleFieldCompatibility",
    beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "AmanSimplePrompt") return;
        const previous = nodeType.prototype.onConfigure;
        nodeType.prototype.onConfigure = function(info, ...args) {
            if (Array.isArray(info?.widgets_values) && info.widgets_values.length === 11) {
                info = {...info, widgets_values: [mergeLegacy(info.widgets_values)]};
            }
            const result = previous?.call(this, info, ...args);
            const text = this.widgets?.find(widget => widget.name === "text");
            if (text && typeof info?.widgets_values?.[0] === "string") text.value = info.widgets_values[0];
            return result;
        };
    },
});
