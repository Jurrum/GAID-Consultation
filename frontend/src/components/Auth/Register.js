// frontend/src/components/Auth/Register.js

import React, { useState, useContext } from 'react';
import { AuthContext } from '../../context/AuthContext';
import { useHistory } from 'react-router-dom';

const Register = () => {
    const { register } = useContext(AuthContext);
    const history = useHistory();
    const [formData, setFormData] = useState({
        full_name: '',
        date_of_birth: '',
        gender: '',
        phone_number: '',
        email: '',
        password: '',
        address: '',
        emergency_contact_name: '',
        emergency_contact_relationship: '',
        emergency_contact_phone: '',
    });

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        await register(formData);
        history.push('/login');
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                {/* Add form fields for each required input */}
                <input type="text" name="full_name" placeholder="Full Name" value={formData.full_name} onChange={handleChange} required />
                <input type="date" name="date_of_birth" placeholder="Date of Birth" value={formData.date_of_birth} onChange={handleChange} required />
                <select name="gender" value={formData.gender} onChange={handleChange}>
                    <option value="">Select Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                    <option value="Other">Other</option>
                </select>
                <input type="text" name="phone_number" placeholder="Phone Number" value={formData.phone_number} onChange={handleChange} required />
                <input type="email" name="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
                <input type="password" name="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
                <input type="text" name="address" placeholder="Address" value={formData.address} onChange={handleChange} />
                <input type="text" name="emergency_contact_name" placeholder="Emergency Contact Name" value={formData.emergency_contact_name} onChange={handleChange} />
                <input type="text" name="emergency_contact_relationship" placeholder="Relationship" value={formData.emergency_contact_relationship} onChange={handleChange} />
                <input type="text" name="emergency_contact_phone" placeholder="Emergency Contact Phone" value={formData.emergency_contact_phone} onChange={handleChange} />
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
