"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const ShellView = () => {
    const [logs, setLogs] = (0, react_1.useState)([]);
    const logEndRef = (0, react_1.useRef)(null);
    (0, react_1.useEffect)(() => {
        const eventSource = new EventSource('http://10.159.189.152:8080/api/logs');
        eventSource.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setLogs(prev => [...prev.slice(-50), data.msg]);
        };
        eventSource.onerror = () => {
            setLogs(prev => [...prev, "⚠️ [ERROR] Lost connection to Neo Engine..."]);
            eventSource.close();
        };
        return () => eventSource.close();
    }, []);
    (0, react_1.useEffect)(() => {
        logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [logs]);
    return (<div className="bg-black border border-gray-900 mx-4 rounded-xl overflow-hidden flex flex-col h-[250px] font-mono">
      <div className="bg-[#111821] p-2 flex justify-between items-center border-b border-gray-900">
        <div className="flex items-center gap-2">
          <lucide_react_1.Terminal size={12} className="text-blue-500"/>
          <span className="text-[9px] font-black text-gray-400 uppercase">Live Engine Terminal</span>
        </div>
        <span className="text-[8px] text-emerald-500 animate-pulse">8080_CONNECTED</span>
      </div>
      
      <div className="flex-1 overflow-y-auto p-3 text-[10px] space-y-1">
        {logs.map((log, i) => (<div key={i} className="text-gray-400">
            <span className="text-blue-900 mr-2">{">>>"}</span>{log}
          </div>))}
        <div ref={logEndRef}/>
      </div>
    </div>);
};
exports.default = ShellView;
