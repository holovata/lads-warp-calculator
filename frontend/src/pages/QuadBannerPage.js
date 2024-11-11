// src/pages/QuadBannerPage.js
import React, { useState } from 'react';
import BannerForm from '../components/BannerForm';
import ResultDisplay from '../components/ResultDisplay';

const QuadBannerPage = () => {
    const [result, setResult] = useState(null);

    const handleSubmit = async (formData) => {
        const response = await fetch('/api/quad-banner', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        });
        const data = await response.json();
        setResult(data.result);
    };

    return (
        <div>
            <h1>Quad Banner Probability Calculator</h1>
            <BannerForm onSubmit={handleSubmit} bannerType="quad" />
            <ResultDisplay result={result} />
        </div>
    );
};

export default QuadBannerPage;
