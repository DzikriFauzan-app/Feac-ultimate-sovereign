"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.WorkflowOrchestrator = void 0;
const feacLogger_1 = require("../../utils/feacLogger");
class WorkflowOrchestrator {
    pipeline = [];
    addStep(step) {
        this.pipeline.push(step);
        return this;
    }
    async executeAll() {
        (0, feacLogger_1.feacLog)("WORKFLOW", `Starting pipeline execution [${this.pipeline.length} steps]`);
        for (const step of this.pipeline) {
            try {
                (0, feacLogger_1.feacLog)("WORKFLOW", `Running Step ${step.id}: ${step.description}`);
                await step.action();
            }
            catch (error) {
                (0, feacLogger_1.feacLog)("CRITICAL", `Workflow failed at ${step.id}: ${error.message}`);
                return false;
            }
        }
        return true;
    }
}
exports.WorkflowOrchestrator = WorkflowOrchestrator;
