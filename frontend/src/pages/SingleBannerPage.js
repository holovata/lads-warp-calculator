import React, { useState } from 'react';
import BannerForm from '../components/BannerForm';
import ResultDisplay from '../components/ResultDisplay';

const SingleBannerPage = () => {
    const [result, setResult] = useState(null);
    const [loadingTime, setLoadingTime] = useState(null); // state for timr

    const handleSubmit = async (formData) => {
        const startTime = Date.now();

        const response = await fetch('/api/single-banner', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        });

        const data = await response.json();
        setResult(data.result);

        const endTime = Date.now();
        setLoadingTime((endTime - startTime) / 1000);
    };

    return (
        <div>
            <h1>Single Banner Probability Calculator</h1>
            <BannerForm onSubmit={handleSubmit} bannerType="single" />
            <ResultDisplay result={result} />
            {loadingTime !== null && <p>Time taken: {loadingTime} seconds</p>} {}
        </div>
    );
};

export default SingleBannerPage;
