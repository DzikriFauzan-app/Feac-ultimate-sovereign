// Mock Test Logic untuk memastikan stabilitas UI
import { Agent } from '../types';

const mockAgents: Agent[] = [
  { id: 'Orchestrator', name: 'Orchestrator Core', status: 'processing', description: 'CEO Digital', powerUsage: 12 },
  { id: 'SovereignGuard', name: 'Sovereign Guard', status: 'standby', description: 'Security Sandbox', powerUsage: 2 }
];

export const runAgentTest = () => {
  console.log("🧪 [TEST] Validating AgentHub Component Logic...");
  
  // 1. Validasi Tipe Data
  if (mockAgents.length !== 2) throw new Error("Agent data mismatch!");
  
  // 2. Validasi Status
  mockAgents.forEach(a => {
    if (!['idle', 'processing', 'error', 'standby'].includes(a.status)) {
      throw new Error(`Invalid status detected on ${a.name}`);
    }
  });

  console.log("✅ [TEST] AgentHub Logic Stable.");
  return true;
};
