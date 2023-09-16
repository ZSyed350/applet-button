// Grid.js
import React from 'react';
import Button from './Button'

function Grid({ numButtons }) {
    const buttons = [];

    for (let i=1; i <= numButtons; i++) {
        buttons.push(
            <Button
                key={i}
                label={'Button $[i]'}
                onClick={() => {
                    // Handle button click here
                    console.log('Button ${i} clicked');
                }}
            />
        );
    }

    return <div className="button-grid">{buttons}</div>;
}

export default Grid;