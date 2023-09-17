// Terminal.js
import React, { useState,useEffect } from "react";
import "./Terminal.css";
import { useLocation } from 'react-router-dom';
function AppTerminal() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [pid, setPid] = useState(0);
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);

  // For example, to get the value of a query parameter called "name":
  const name = queryParams.get('appName');
  useEffect(() => {
    // This code will only run once, after the initial render
    const data = { "script_name":name };

    // Make POST request to Flask server
    fetch("http://localhost:8080/start_script", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.output)
        let text = "";
        for(let i = 0; i < data.output.length; i++)text+=data.output[i] + "\n"
        setMessages([...messages, { role: "bot", text: text }]);
        setPid(data.pid)
        // assuming server sends back JSON response with "result" field
      })
      .catch((error) => {
        console.error("Error:", error);
      });

    // Optionally, you can return a cleanup function
    return () => {
      console.log('Component will unmount!');
    };
  }, []);
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    
    setMessages([...messages, { role: "user", text: input }]);
   

    try {
      let jsondata = {pid,input}
      const response = await fetch("http://localhost:8080/interact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(jsondata),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      console.log(data.output)
        let text = "";
        for(let i = 0; i < data.output.length; i++)text+=data.output[i] + "\n"
        setMessages([...messages, { role: "bot", text: text }]);

      setMessages([...messages, { role: "user", text: input }, { role: "bot", text: text }]);
      setInput("");
    } catch (error) {
      setMessages([...messages, { role: "user", text: input }, { role: "bot", text: "Error processing the request." }]);
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
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your message..." />
      </form>
    </div>
  );
}

function NewlineText({ text }) {
  const newText = text.split("\n").map((str, index, array) =>
    index === array.length - 1 ? (
      str
    ) : (
      <>
        {str}
        <br />
      </>
    )
  );

  return <>{newText}</>;
}

export default AppTerminal;
