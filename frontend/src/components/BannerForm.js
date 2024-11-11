// src/components/BannerForm.js
import React, { useState } from 'react';

const BannerForm = ({ onSubmit, bannerType }) => {
    const [numRolls, setNumRolls] = useState('');
    const [initialPity, setInitialPity] = useState('');
    const [isGuaranteed, setIsGuaranteed] = useState(false);
    const [desiredCopies, setDesiredCopies] = useState(bannerType === 'single' ? '' : 1);
    const [isSummoningPair, setIsSummoningPair] = useState(false);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({
            num_rolls: numRolls,
            initial_pity: initialPity,
            is_guaranteed: isGuaranteed,
            desired_copies: bannerType === 'single' ? desiredCopies : 1,
            is_summoning_pair: bannerType === 'pair' ? isSummoningPair : undefined,
        });
    };

    return (
        <form onSubmit={handleSubmit} className="p-3">
            <div className="form-group">
                <label>Number of Rolls:</label>
                <input type="number" className="form-control" value={numRolls} onChange={(e) => setNumRolls(e.target.value)} required />
            </div>

            <div className="form-group">
                <label>Initial Pity:</label>
                <input type="number" className="form-control" value={initialPity} onChange={(e) => setInitialPity(e.target.value)} required />
            </div>

            <div className="form-group form-check">
                <input type="checkbox" className="form-check-input" checked={isGuaranteed} onChange={(e) => setIsGuaranteed(e.target.checked)} />
                <label className="form-check-label">Guaranteed</label>
            </div>

            {bannerType === 'pair' && (
                <div className="form-group form-check">
                    <input
                        type="checkbox"
                        className="form-check-input"
                        checked={isSummoningPair}
                        onChange={(e) => setIsSummoningPair(e.target.checked)}
                    />
                    <label className="form-check-label">Summoning Pair</label>
                </div>
            )}

            {bannerType === 'single' && (
                <div className="form-group">
                    <label>Desired Copies:</label>
                    <input type="number" className="form-control" value={desiredCopies} onChange={(e) => setDesiredCopies(e.target.value)} required />
                </div>
            )}

            <button type="submit" className="btn btn-primary">Calculate Probability</button>
        </form>
    );
};

export default BannerForm;
