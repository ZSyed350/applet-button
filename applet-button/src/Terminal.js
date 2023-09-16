// Terminal.js
import React, { useState } from 'react';
import './Terminal.css';

function Terminal() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setMessages([...messages, { role: 'user', text: input }]);
    const formData = new FormData();
    formData.append('prompt', input);

    try {
      const response = await fetch('http://localhost:5000/generate', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      let text = '=====================\n'
      text += `Code: \n${data.code}\n`
      text += '---------------------\n'
      text += `Test Cases: \n${data.test_cases}\n`
      text += '=====================\n'


      setMessages([...messages, { role: 'user', text: input }, { role: 'bot', text: text }]);
      setInput('');

    } catch (error) {
      setMessages([...messages, { role: 'user', text: input }, { role: 'bot', text: 'Error processing the request.' }]);
    }
  };

  return (
    <div className="terminal">
      <div className="chat-window">
        {messages.map((message, index) => (
          <div key={index} className={message.role}>
          <NewlineText text={message.text} />
          </div>
      
        ))}
      </div>
      <form onSubmit={handleSubmit} className="input-area">
        <input 
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
      </form>
    </div>
  );
}

function NewlineText({ text }) {
  const newText = text.split('\n').map((str, index, array) => 
    index === array.length - 1 ? str : <>
      {str}
      <br />
    </>
  );
  
  return <>{newText}</>;
}


export default Terminal;
