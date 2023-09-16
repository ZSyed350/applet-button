// Grid.js
import React from 'react';
import Button from './Button'

function Grid({ numButtons }) {
    const buttons = [];

    const fs = require('fs');
    const directoryPath = '../../applets';

    fs.readdir(directoryPath, (err, files => {
        if (err) {
            console.error('Error reading directory: ', err);
            return;
        }

        console.log('Files in the directory', files);

        // process the files
    }));
    // parse the files
    // get the names
    // numButtons = numFiles

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