// frontend/src/components/Auth/Login.js

import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import { useHistory } from 'react-router-dom';

const Login = () => {
    const { login, auth } = useContext(AuthContext);
    const history = useHistory();
    const [credentials, setCredentials] = useState({
        email: '',
        password: '',
    });

    const handleChange = (e) => {
        setCredentials({...credentials, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await login(credentials.email, credentials.password);
        if (auth.isAuthenticated) {
            history.push('/chatbot');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {auth.error && <p style={{color: 'red'}}>{auth.error}</p>}
            <form onSubmit={handleSubmit}>
                <input type="email" name="email" placeholder="Email" value={credentials.email} onChange={handleChange} required />
                <input type="password" name="password" placeholder="Password" value={credentials.password} onChange={handleChange} required />
                <button type="submit" disabled={auth.loading}>{auth.loading ? 'Logging in...' : 'Login'}</button>
            </form>
        </div>
    );
};

export default Login;
