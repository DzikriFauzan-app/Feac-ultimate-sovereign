import { useState, useEffect } from 'react';
import { Activity, Thermometer, Cpu } from 'lucide-react';

const ResourceMonitor = () => {
  const [data, setData] = useState<any[]>([]);
  const [currentStats, setCurrentStats] = useState({ ram: 0, cpu: 0, temp: 0 });

  useEffect(() => {
    const eventSource = new EventSource('http://10.159.189.152:8080/api/logs');
    eventSource.onmessage = (event) => {
      const payload = JSON.parse(event.data);
      const stats = payload.stats;
      
      setCurrentStats({
        ram: stats.ram_usage,
        cpu: stats.cpu_usage || 0,
        temp: stats.temp || 0
      });

      setData(prev => {
        const newData = [...prev, stats.ram_usage].slice(-20); // Simpan 20 poin terakhir
        return newData;
      });
    };
    return () => eventSource.close();
  }, []);

  return (
    <div className="p-4 bg-[#080808] border border-gray-900 rounded-2xl mt-4 shadow-inner">
      <div className="flex justify-between items-center mb-4">
        <h4 className="text-[10px] font-black text-gray-500 tracking-[0.3em] uppercase flex items-center gap-2">
          <Activity size={12} className="text-blue-500" /> System_Vital_Sign
        </h4>
        <span className="text-[8px] text-emerald-500 font-mono animate-pulse">LIVE_STREAMING</span>
      </div>

      {/* Visual Graph Simple */}
      <div className="h-16 flex items-end gap-1 mb-4 px-1">
        {data.map((val, i) => (
          <div 
            key={i} 
            className="flex-1 bg-blue-600/40 border-t border-blue-400/50 rounded-t-sm transition-all duration-500"
            style={{ height: `${val}%` }}
          ></div>
        ))}
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-3 gap-2">
        <div className="text-center">
          <p className="text-[7px] text-gray-600 uppercase font-bold">RAM</p>
          <p className="text-xs text-white font-black">{currentStats.ram}%</p>
        </div>
        <div className="text-center border-x border-gray-900">
          <p className="text-[7px] text-gray-600 uppercase font-bold">CPU</p>
          <p className="text-xs text-blue-500 font-black">{currentStats.cpu}%</p>
        </div>
        <div className="text-center">
          <p className="text-[7px] text-gray-600 uppercase font-bold">TEMP</p>
          <p className="text-xs text-red-500 font-black">{currentStats.temp}°C</p>
        </div>
      </div>
    </div>
  );
};

export default ResourceMonitor;
