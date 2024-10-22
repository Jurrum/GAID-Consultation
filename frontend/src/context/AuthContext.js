// frontend/src/context/AuthContext.js

import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({
        accessToken: localStorage.getItem('accessToken') || null,
        isAuthenticated: !!localStorage.getItem('accessToken'),
        loading: false,
        error: null,
    });

    const login = async (email, password) => {
        setAuth({ ...auth, loading: true, error: null });
        try {
            const response = await axios.post('/api/login', { email, password });
            const token = response.data.access_token || response.data.access_token;
            localStorage.setItem('accessToken', token);
            setAuth({ ...auth, accessToken: token, isAuthenticated: true, loading: false });
        } catch (error) {
            setAuth({ ...auth, loading: false, error: error.response?.data?.error || 'Login failed.' });
        }
    };

    const register = async (userData) => {
        setAuth({ ...auth, loading: true, error: null });
        try {
            await axios.post('/api/register', userData);
            setAuth({ ...auth, loading: false });
        } catch (error) {
            setAuth({ ...auth, loading: false, error: error.response?.data?.error || 'Registration failed.' });
        }
    };

    const logout = () => {
        localStorage.removeItem('accessToken');
        setAuth({ ...auth, accessToken: null, isAuthenticated: false, error: null });
    };

    return (
        <AuthContext.Provider value={{ auth, login, register, logout }}>
            {children}
        </AuthContext.Provider>
    );
};
