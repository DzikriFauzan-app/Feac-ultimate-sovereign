import { useState } from 'react';
import { Search, RefreshCw, Plus } from 'lucide-react';

const RepositoryManager = () => {
  const [repos, setRepos] = useState([{ id: 1, name: 'Feac-ultimate-sovereign', url: '', token: '' }]);
  const addRepo = () => setRepos([...repos, { id: Date.now(), name: 'New Repo', url: '', token: '' }]);

  return (
    <div className="p-5 pb-24 space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-black text-blue-500 italic uppercase">Repo Manager</h2>
        <button onClick={addRepo} className="p-2 bg-blue-600 rounded-xl text-white"><Plus /></button>
      </div>
      {repos.map((repo: any) => (
        <div key={repo.id} className="bg-[#111821] border border-gray-800 rounded-2xl p-5 space-y-4">
          <input className="w-full bg-black/40 border border-gray-800 p-3 rounded-xl text-xs text-white" placeholder="Repository Name" />
          <div className="relative group">
            <textarea className="w-full bg-black border border-blue-900/30 p-4 rounded-xl text-xs text-gray-300 outline-none h-24" placeholder="Instruction for this repo..." />
            <div className="absolute bottom-3 right-3 flex space-x-2">
              <button className="bg-blue-600 p-2 rounded-lg text-white text-[10px] font-black flex items-center"><Search className="w-3 h-3 mr-1"/> SCAN</button>
              <button className="bg-emerald-600 p-2 rounded-lg text-white text-[10px] font-black flex items-center"><RefreshCw className="w-3 h-3 mr-1"/> AUTO FIX</button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};
export default RepositoryManager;
