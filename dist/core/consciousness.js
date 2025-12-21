"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Consciousness = exports.SystemState = void 0;
var SystemState;
(function (SystemState) {
    SystemState["IDLE"] = "IDLE";
    SystemState["THINKING"] = "THINKING";
    SystemState["EXECUTING"] = "EXECUTING";
    SystemState["CRITICAL"] = "CRITICAL";
})(SystemState || (exports.SystemState = SystemState = {}));
class Consciousness {
    state = SystemState.IDLE;
    lastPulse = Date.now();
    updateState(newState) {
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
exports.Consciousness = Consciousness;
