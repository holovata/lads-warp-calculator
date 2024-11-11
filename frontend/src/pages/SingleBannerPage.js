// src/pages/SingleBannerPage.js
import React, { useState } from 'react';
import BannerForm from '../components/BannerForm';
import ResultDisplay from '../components/ResultDisplay';

const SingleBannerPage = () => {
    const [result, setResult] = useState(null);

    const handleSubmit = async (formData) => {
        const response = await fetch('/api/single-banner', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        });
        const data = await response.json();
        setResult(data.result);
    };

    return (
        <div>
            <h1>Single Banner Probability Calculator</h1>
            <BannerForm onSubmit={handleSubmit} bannerType="single" />
            <ResultDisplay result={result} />
        </div>
    );
};

export default SingleBannerPage;
