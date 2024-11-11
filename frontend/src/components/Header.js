// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => (
    <header className="bg-light p-3">
        <nav className="nav justify-content-center">
            <Link className="nav-link" to="/single-banner">Single Banner</Link>
            <Link className="nav-link" to="/pair-banner">Pair Banner</Link>
            <Link className="nav-link" to="/quad-banner">Quad Banner</Link>
        </nav>
    </header>
);

export default Header;
