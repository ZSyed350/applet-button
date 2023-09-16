// Button.js
import React from 'react';

function Button({ label, onClick}) {
    return (
        <button onClick={onClick} className="grid-button">
            {label}
        </button>
    );
}

export default Button;