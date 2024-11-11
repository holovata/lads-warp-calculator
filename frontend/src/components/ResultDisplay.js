// src/components/ResultDisplay.js
import React from 'react';

const ResultDisplay = ({ result }) => (
    result !== null ? (
        <div>
            <h2>Result:</h2>
            <p>The probability of success is: {result}</p>
        </div>
    ) : null
);

export default ResultDisplay;
