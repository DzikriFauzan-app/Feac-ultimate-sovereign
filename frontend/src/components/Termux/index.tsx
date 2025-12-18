
const TermuxInternal = () => {
  const [history, setHistory] = useState(['Welcome to FEAC Internal Termux v1.0', 'Sovereign Core: Connected']);
  const [input, setInput] = useState('');

  const handleCmd = (e: any) => {
    if (e.key === 'Enter') {
      setHistory([...history, `$ ${input}`, `Executing: ${input}...`, 'Done.']);
      setInput('');
    }
  };

  return (
    <div className="h-full bg-black font-mono text-[12px] p-4 flex flex-col">
      <div className="flex-1 overflow-y-auto text-emerald-500 space-y-1">
        {history.map((h, i) => <p key={i}>{h}</p>)}
        <div className="flex items-center">
          <span className="mr-2 text-white">$</span>
          <input autoFocus className="bg-transparent outline-none flex-1 text-white" value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={handleCmd} />
        </div>
      </div>
    </div>
  );
};
export default TermuxInternal;
