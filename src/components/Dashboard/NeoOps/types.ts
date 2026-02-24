export interface Agent {
  id: string;
  name: string;
  status: 'idle' | 'processing' | 'error' | 'standby';
  description: string;
  powerUsage: number; // Dalam persen untuk OptimizationAgent
}
