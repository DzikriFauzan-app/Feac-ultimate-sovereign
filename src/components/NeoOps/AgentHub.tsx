import React, { useEffect, useState } from 'react';

const AgentHub: React.FC = () => {
    const [agents, setAgents] = useState<string[]>([]);

    useEffect(() => {
        fetch("http://10.4.35.107:8080/api/dashboard/stats")
            .then(res => res.json())
            .then(data => setAgents(data.agent_list || []))
            .catch(() => console.log("NeoEngine Offline"));
    }, []);

    return (
        <div style={{ padding: '15px', background: '#111', color: '#0ff', borderRadius: '8px' }}>
            <h3>NEO-COUNCIL MONITOR</h3>
            <ul>
                {agents.map(a => <li key={a}>🟢 {a}</li>)}
            </ul>
        </div>
    );
};
export default AgentHub;
