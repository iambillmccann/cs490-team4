//task 7: Integrate Frontend with Authentication API

import axios from 'axios';
import { Navigate } from 'react-router-dom';

// Login Function
export const login = async (username, password) => {
  try {
    const response = await axios.post('http://localhost:8000/api/login', { username, password });
    const { token } = response.data;
    localStorage.setItem('token', token); // Save JWT to localStorage
    console.log('Login successful:', token);
    return true;
  } catch (error) {
    console.error('Login failed:', error.response?.data || error.message);
    return false;
  }
};

// Register Function
export const register = async (username, email, password) => {
  try {
    const response = await axios.post('http://localhost:8000/api/signup', { username, email, password });
    console.log('Registration successful:', response.data);
    return true;
  } catch (error) {
    console.error('Registration failed:', error.response?.data || error.message);
    return false;
  }
};

// Logout Function
export const logout = (navigate) => {
  localStorage.removeItem('token'); // Clear JWT
  console.log('Logged out successfully.');
  navigate('/login'); // Redirect to login page
};

// Check Authentication
export const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  return !!token; // Check if token exists
};

// Protected Route Component
export const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  if (!token) {
    return <Navigate to="/login" />; // Redirect to login if not authenticated
  }
  return children; // Render protected content if authenticated
};
