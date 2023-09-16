// Navbar.js
import React from 'react';
import './Navbar.css';

function Navbar() {
    return (
        <div className="navbar">
            <a href="/generate">Generate Applet</a>
            <a href="/my-apps">My Applets</a>
            <a href="/shared-apps">Community</a>
            <a href="/about">About</a>
        </div>
    );
}

export default Navbar