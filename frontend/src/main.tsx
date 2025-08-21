import { createRoot } from 'react-dom/client';
import { useState } from 'react';

function App() {
  const [text, setText] = useState('');
  const [tasks, setTasks] = useState<any[]>([]);

  async function submit() {
    const res = await fetch('http://localhost:8000/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: Date.now(), text })
    });
    if (res.ok) {
      const task = await res.json();
      setTasks([...tasks, task]);
      setText('');
    }
  }

  return (
    <div>
      <h1>CodePro Console</h1>
      <input value={text} onChange={e => setText(e.target.value)} />
      <button onClick={submit}>add</button>
      <ul>
        {tasks.map(t => (
          <li key={t.id}>{t.text}</li>
        ))}
      </ul>
    </div>
  );
}

createRoot(document.getElementById('root')!).render(<App />);
