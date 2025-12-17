import { feacLog } from '../../utils/feacLogger';

export interface Step {
    id: string;
    description: string;
    action: () => Promise<void>;
}

export class WorkflowOrchestrator {
    private pipeline: Step[] = [];

    addStep(step: Step): this {
        this.pipeline.push(step);
        return this;
    }

    async executeAll(): Promise<boolean> {
        feacLog("WORKFLOW", `Starting pipeline execution [${this.pipeline.length} steps]`);
        for (const step of this.pipeline) {
            try {
                feacLog("WORKFLOW", `Running Step ${step.id}: ${step.description}`);
                await step.action();
            } catch (error: any) {
                feacLog("CRITICAL", `Workflow failed at ${step.id}: ${error.message}`);
                return false;
            }
        }
        return true;
    }
}
