import React, { useState } from 'react';
import BannerForm from '../components/BannerForm';
import ResultDisplay from '../components/ResultDisplay';

const PairBannerPage = () => {
    const [result, setResult] = useState(null);
    const [isSummoningPair, setIsSummoningPair] = useState(false);
    const [loadingTime, setLoadingTime] = useState(null);

    const handleSubmit = async (formData) => {
        const startTime = Date.now();

        const response = await fetch('/api/pair-banner', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...formData, is_summoning_pair: isSummoningPair }),
        });

        const data = await response.json();
        setResult(data.result);

        const endTime = Date.now();
        setLoadingTime((endTime - startTime) / 1000);
    };

    return (
        <div>
            <h1>Pair Banner Probability Calculator</h1>
            <BannerForm onSubmit={handleSubmit} bannerType="pair" />
            <ResultDisplay result={result} />
            {loadingTime !== null && <p>Time taken: {loadingTime} seconds</p>} {}
        </div>
    );
};

export default PairBannerPage;
