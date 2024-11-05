// src/components/BannerForm.js
import React, { useState } from 'react';

const BannerForm = ({ onSubmit }) => {
    const [numRolls, setNumRolls] = useState('');
    const [desiredCharacters, setDesiredCharacters] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ numRolls, desiredCharacters });
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Number of Rolls:
                <input type="number" value={numRolls} onChange={(e) => setNumRolls(e.target.value)} />
            </label>
            <label>
                Desired Characters:
                <input type="number" value={desiredCharacters} onChange={(e) => setDesiredCharacters(e.target.value)} />
            </label>
            <button type="submit">Calculate Probability</button>
        </form>
    );
};

export default BannerForm;
