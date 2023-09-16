import React from 'react';
import './App.css';  // Import the styles
import Terminal from './Terminal';
import Navbar from './Navbar';
import Grid from './Grid'

function App() {
  return (
    <div className="App">
      <Navbar />
      <Terminal />
      <Grid numButtons={9} />
    </div>
  );
}

export default App;
