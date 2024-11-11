// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import SingleBannerPage from './pages/SingleBannerPage';
import PairBannerPage from './pages/PairBannerPage';
import QuadBannerPage from './pages/QuadBannerPage';

const App = () => (
    <Router>
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<SingleBannerPage />} />
          <Route path="/single-banner" element={<SingleBannerPage />} />
          <Route path="/pair-banner" element={<PairBannerPage />} />
          <Route path="/quad-banner" element={<QuadBannerPage />} />
        </Routes>
      </main>
      <Footer />
    </Router>
);

export default App;
