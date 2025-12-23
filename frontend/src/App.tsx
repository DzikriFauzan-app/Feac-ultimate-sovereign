import React, { useState, useEffect } from 'react';
import { API_URL } from './config';

const App = () => {
  const [status, setStatus] = useState('STANDBY');
  const [activeTab, setActiveTab] = useState('dashboard');
  const [logs, setLogs] = useState<string[]>([]);

  const addLog = (msg: string) => setLogs(prev => [`[${new Date().toLocaleTimeString()}] ${msg}`, ...prev]);

  useEffect(() => {
    addLog(`Attempting handshake to ${API_URL}...`);
    fetch(`${API_URL}/api/emergent/scan`)
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          setStatus('CONNECTED');
          addLog('System Online. Owner Key Verified.');
        }
      })
      .catch(err => {
        setStatus('OFFLINE MODE');
        addLog('Connection failed. Switching to Offline Interface.');
        console.error(err);
      });
  }, []);

  const handleBridgeExecute = () => {
    addLog('Executing Bridge manually...');
    fetch(`${API_URL}/api/bridge/execute`, { method: 'POST' })
      .then(res => res.json())
      .then(d => addLog(`Response: ${d.message}`))
      .catch(() => addLog('Execution failed: Server unreachable.'));
  };

  return (
    <div style={{ background: '#050505', color: '#0f0', minHeight: '100vh', padding: '15px', fontFamily: 'monospace' }}>
      
      <div style={{ borderBottom: '1px solid #333', paddingBottom: '10px', marginBottom: '20px' }}>
        <h2 style={{ margin: 0 }}>ARIES <span style={{ color: status === 'CONNECTED' ? '#0f0' : '#f00' }}>{status}</span></h2>
        <small style={{ color: '#666' }}>Target: {API_URL}</small>
      </div>

      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <button onClick={() => setActiveTab('dashboard')} style={{ background: activeTab === 'dashboard' ? '#222' : 'transparent', color: '#fff', border: '1px solid #333', padding: '10px' }}>DASHBOARD</button>
        <button onClick={() => setActiveTab('emergent')} style={{ background: activeTab === 'emergent' ? '#222' : 'transparent', color: '#fff', border: '1px solid #333', padding: '10px' }}>EMERGENT</button>
        <button onClick={() => setActiveTab('bridge')} style={{ background: activeTab === 'bridge' ? '#222' : 'transparent', color: '#fff', border: '1px solid #333', padding: '10px' }}>BRIDGE</button>
<button className="nav-button">EMERGENT</button>
<button className="nav-button">EMERGENT</button>
      </div>

      <div style={{ border: '1px solid #222', padding: '15px', borderRadius: '5px', minHeight: '300px' }}>
        {activeTab === 'dashboard' && (
          <div>
            <h3>SYSTEM METRICS</h3>
            <p>CPU: <span style={{color: '#fff'}}>OPTIMAL</span></p>
            <p>Neo Engine: <span style={{color: '#fff'}}>ACTIVE</span></p>
          </div>
        )}

        {activeTab === 'emergent' && (
          <div>
            <h3>EMERGENT SCANNER</h3>
            <p>Scanning local repositories...</p>
            <div style={{ background: '#111', padding: '10px', marginTop: '10px' }}>No anomalies detected.</div>
          </div>
        )}

        {activeTab === 'bridge' && (
          <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h3>MANUAL OVERRIDE</h3>
            <button onClick={handleBridgeExecute} style={{ fontSize: '24px', padding: '20px 40px', background: '#0f0', color: '#000', border: 'none', borderRadius: '10px', fontWeight: 'bold' }}>+ EXECUTE</button>
          </div>
        )}
      </div>

      <div style={{ marginTop: '20px', borderTop: '1px solid #333', paddingTop: '10px', fontSize: '12px', color: '#888' }}>
        {logs.map((l, i) => <div key={i}>{l}</div>)}
      </div>

    </div>
  );
};

export default App;
