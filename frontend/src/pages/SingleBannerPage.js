// src/pages/SingleBannerPage.js
import React, { useState } from 'react';
import axios from 'axios';
import BannerForm from '../components/BannerForm';
import ResultDisplay from '../components/ResultDisplay';

const SingleBannerPage = () => {
    const [result, setResult] = useState(null);

    const calculateProbability = async (data) => {
        try {
            const response = await axios.post('/api/single-banner', data);
            setResult(response.data);
        } catch (error) {
            console.error("Error calculating probability", error);
        }
    };

    return (
        <div>
            <h1>Single Banner</h1>
            <BannerForm onSubmit={calculateProbability} />
            {result && <ResultDisplay result={result} />}
        </div>
    );
};

export default SingleBannerPage;
