import React, { useState, useEffect } from 'react';
import { API_URL } from './config';

const App = () => {
  const [status, setStatus] = useState('OFFLINE');
  const [activeTab, setActiveTab] = useState('dashboard');

  useEffect(() => {
    fetch(`${API_URL}/api/emergent/scan`)
      .then(res => res.json())
      .then(data => data.success && setStatus('CONNECTED'))
      .catch(() => setStatus('BRIDGE FAILURE'));
  }, []);

  return (
    <div style={{ background: '#0a0a0a', color: '#fff', minHeight: '100vh', padding: '20px' }}>
      <header>
        <h1>FEAC SOVEREIGN <span style={{ color: status === 'CONNECTED' ? '#00ff00' : '#ff0000' }}>{status}</span></h1>
        <p>Endpoint: {API_URL}</p>
      </header>

      <nav style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <button onClick={() => setActiveTab('dashboard')}>Dashboard</button>
        <button onClick={() => setActiveTab('emergent')}>Emergent Tab</button>
        <button onClick={() => setActiveTab('bridge')}>Engine Bridge</button>
      </nav>

      <main>
        {activeTab === 'emergent' && (
          <div className="tab-content">
            <h2>Emergent Scanner</h2>
            <button onClick={() => alert('Scanning...')}>Start Deep Scan</button>
          </div>
        )}

        {activeTab === 'bridge' && (
          <div className="tab-content">
            <h2>Engine Bridge</h2>
            <button onClick={() => alert('Bridge Executed!')} style={{ fontSize: '2rem' }}>+</button>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
