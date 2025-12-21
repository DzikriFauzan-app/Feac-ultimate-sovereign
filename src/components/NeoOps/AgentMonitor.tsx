import React, { useEffect, useState } from 'react';

export const AgentMonitor: React.FC = () => {
    const [stats, setStats] = useState({ agent_list: [], status: "OFFLINE" });

    useEffect(() => {
        const sync = setInterval(() => {
            fetch("http://10.4.35.107:8080/api/dashboard/stats")
                .then(r => r.json())
                .then(setStats)
                .catch(() => setStats({ agent_list: [], status: "DISCONNECTED" }));
        }, 3000);
        return () => clearInterval(sync);
    }, []);

    return (
        <div className="neo-monitor-ui p-4 bg-black/50 border border-cyan-500 rounded-lg">
            <h2 className="text-cyan-400 font-bold mb-4">🏛️ NEURAL COUNCIL: {stats.status}</h2>
            <div className="grid grid-cols-2 gap-2 text-xs text-green-400">
                {stats.agent_list.map(a => <div key={a}>✅ {a}</div>)}
            </div>
        </div>
    );
};
