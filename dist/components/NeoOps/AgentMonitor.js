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
exports.AgentMonitor = void 0;
const react_1 = __importStar(require("react"));
const AgentMonitor = () => {
    const [stats, setStats] = (0, react_1.useState)({ agent_list: [], status: "OFFLINE" });
    (0, react_1.useEffect)(() => {
        const sync = setInterval(() => {
            fetch("http://10.4.35.107:8080/api/dashboard/stats")
                .then(r => r.json())
                .then(setStats)
                .catch(() => setStats({ agent_list: [], status: "DISCONNECTED" }));
        }, 3000);
        return () => clearInterval(sync);
    }, []);
    return (<div className="neo-monitor-ui p-4 bg-black/50 border border-cyan-500 rounded-lg">
            <h2 className="text-cyan-400 font-bold mb-4">🏛️ NEURAL COUNCIL: {stats.status}</h2>
            <div className="grid grid-cols-2 gap-2 text-xs text-green-400">
                {stats.agent_list.map(a => <div key={a}>✅ {a}</div>)}
            </div>
        </div>);
};
exports.AgentMonitor = AgentMonitor;
