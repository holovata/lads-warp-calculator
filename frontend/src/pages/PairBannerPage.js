// src/pages/PairBannerPage.js
import React, { useState } from 'react';
import BannerForm from '../components/BannerForm';
import ResultDisplay from '../components/ResultDisplay';

const PairBannerPage = () => {
    const [result, setResult] = useState(null);
    const [isSummoningPair, setIsSummoningPair] = useState(false);

    const handleSubmit = async (formData) => {
        const response = await fetch('/api/pair-banner', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...formData, is_summoning_pair: isSummoningPair }),
        });
        const data = await response.json();
        setResult(data.result);
    };

    return (
        <div>
            <h1>Pair Banner Probability Calculator</h1>
            <BannerForm onSubmit={handleSubmit} bannerType="pair" />
            <ResultDisplay result={result} />
        </div>
    );
};

export default PairBannerPage;
