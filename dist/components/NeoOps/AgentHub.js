"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = __importStar(require("react"));
const AgentHub = () => {
    const [agents, setAgents] = (0, react_1.useState)([]);
    (0, react_1.useEffect)(() => {
        fetch("http://10.4.35.107:8080/api/dashboard/stats")
            .then(res => res.json())
            .then(data => setAgents(data.agent_list || []))
            .catch(() => console.log("NeoEngine Offline"));
    }, []);
    return (<div style={{ padding: '15px', background: '#111', color: '#0ff', borderRadius: '8px' }}>
            <h3>NEO-COUNCIL MONITOR</h3>
            <ul>
                {agents.map(a => <li key={a}>🟢 {a}</li>)}
            </ul>
        </div>);
};
exports.default = AgentHub;
