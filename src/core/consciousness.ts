export enum SystemState {
    IDLE = "IDLE",
    THINKING = "THINKING",
    EXECUTING = "EXECUTING",
    CRITICAL = "CRITICAL"
}

export class Consciousness {
    private state: SystemState = SystemState.IDLE;
    private lastPulse: number = Date.now();

    updateState(newState: SystemState) {
        this.state = newState;
        this.lastPulse = Date.now();
        console.log(`[CONSCIOUSNESS] State shifted to: ${newState}`);
    }

    getState() {
        return {
            state: this.state,
            uptime: Date.now() - this.lastPulse
        };
    }
}
