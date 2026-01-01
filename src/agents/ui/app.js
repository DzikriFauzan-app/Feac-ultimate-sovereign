const socket = io();

const statusEl = document.getElementById('status');
const terminal = document.getElementById('terminal');
const sendBtn = document.getElementById('sendBtn');

socket.on('connect', () => {
  statusEl.innerText = 'ONLINE';
  statusEl.className = 'status-online';
  log('SYSTEM', 'Connected to NeoEngine Bridge', 'info');
});

socket.on('disconnect', () => {
  statusEl.innerText = 'OFFLINE';
  statusEl.className = 'status-offline';
  log('SYSTEM', 'Disconnected', 'error');
});

socket.on('log', (data) => {
  log(data.agent || 'SYSTEM', JSON.stringify(data, null, 2), 'info');
});

socket.on('command_ack', (data) => {
  log('SCHEDULER', 'Task queued: ' + data.task_id, 'info');
});

function log(source, message, level='info') {
  const el = document.createElement('div');
  el.className = 'log-entry';
  el.innerText = `[${new Date().toLocaleTimeString()}] [${source}] ${message}`;
  terminal.appendChild(el);
  terminal.scrollTop = terminal.scrollHeight;
}

sendBtn.addEventListener('click', () => {
  const agent = document.getElementById('agentSelect').value;
  const command = document.getElementById('cmdInput').value;
  const paramStr = document.getElementById('paramInput').value;
  let params = {};
  try { params = paramStr ? JSON.parse(paramStr) : {}; } catch(e) {
    log('UI', 'Invalid JSON params', 'error'); return;
  }
  socket.emit('execute_command', { agent, command, params });
  log('UI', `Sent ${command} -> ${agent}`, 'info');
});
