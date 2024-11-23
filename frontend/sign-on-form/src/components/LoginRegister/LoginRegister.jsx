import React, { useState } from 'react';
import './LoginRegister.css';
import { FaUser, FaLock, FaEnvelope } from "react-icons/fa";
import axios from 'axios';

// Function to handle login API request
export const handleLogin = async (username, password) => {
  try {
    // Handles successful login
    const response = await axios.post('/api/login', { username, password });
    console.log('Login Success:', response.data);
  } catch (error) {
    // Handles login error
    console.error('Login Error:', error.response?.data || error.message);
  }
};

// Function to handle register API request
export const handleRegister = async (username, email, password) => {
  try {
    // Handles successful registration
    const response = await axios.post('/api/register', { username, email, password });
    console.log('Register Success:', response.data);
  } catch (error) {
    // Handles registration error
    console.error('Register Error:', error.response?.data || error.message);
  }
};

// Renders the login-register page
const LoginRegister = ({ action, registerLink, loginLink }) => {
  // State for login inputs
  //loginUsername and loginPassword: Holds current value of username/password input field
  //setLoginUsername and setLoginPassword: Used to update the state values
  const [loginUsername, setLoginUsername] = useState(''); //useState = React Hook
  const [loginPassword, setLoginPassword] = useState('');

  // State for register inputs
  const [registerUsername, setRegisterUsername] = useState('');
  const [registerEmail, setRegisterEmail] = useState('');
  const [registerPassword, setRegisterPassword] = useState('');
  const [registerConfirmPassword, setRegisterConfirmPassword] = useState('');

  return (
    <div className={`wrapper ${action}`}>
      {/* Login Form */}
      <div className="form-box login">
        <form
          onSubmit={(e) => {
            e.preventDefault(); //prevent the page from reloading
            handleLogin(loginUsername, loginPassword); // send the login info to backend
          }}
        >
          <h1>Login</h1>
          <div className="input-box">
            <input
              type="text"
              placeholder="Username"
              value={loginUsername}
              onChange={(e) => setLoginUsername(e.target.value)}
              required
            />
            <FaUser className="icon" />
          </div>
          <div className="input-box">
            <input
              type="password"
              placeholder="Password"
              value={loginPassword}
              onChange={(e) => setLoginPassword(e.target.value)}
              required
            />
            <FaLock className="icon" />
          </div>
          <div className="remember-forgot">
            <label>
              <input type="checkbox" />
              Remember me
            </label>
            <a href="#">Forgot password?</a>
          </div>
          <button type="submit">Login</button>
          <div className="register-link">
            <p>
              Don't have an account?{' '}
              <a href="#" onClick={registerLink}>
                Register
              </a>
            </p>
          </div>
        </form>
      </div>

      {/* Register Form */}
      <div className="form-box register">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            if (registerPassword !== registerConfirmPassword) {
              alert('Passwords do not match!');
              return;
            }
            // send register info to backend
            handleRegister(registerUsername, registerEmail, registerPassword);
          }}
        >
          <h1>Register</h1>
          <div className="input-box">
            <input
              type="text"
              placeholder="Username"
              value={registerUsername}
              onChange={(e) => setRegisterUsername(e.target.value)}
              required
            />
            <FaUser className="icon" />
          </div>
          <div className="input-box">
            <input
              type="email"
              placeholder="Email"
              value={registerEmail}
              onChange={(e) => setRegisterEmail(e.target.value)}
              required
            />
            <FaEnvelope className="icon" />
          </div>
          <div className="input-box">
            <input
              type="password"
              placeholder="Password"
              value={registerPassword}
              onChange={(e) => setRegisterPassword(e.target.value)}
              required
            />
            <FaLock className="icon" />
          </div>
          <div className="input-box">
            <input
              type="password"
              placeholder="Confirm Password"
              value={registerConfirmPassword}
              onChange={(e) => setRegisterConfirmPassword(e.target.value)}
              required
            />
            <FaLock className="icon" />
          </div>
          <div className="remember-forgot">
            <label>
              <input type="checkbox" required />
              I agree terms & conditions
            </label>
          </div>
          <button type="submit">Register</button>
          <div className="register-link">
            <p>
              Already have an account?{' '}
              <a href="#" onClick={loginLink}>
                Login
              </a>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

// Manages the state of each active form(login or register)
const LoginRegisterContainer = () => {
  // action: holds current form state. By default, the login page
  // setAction: used to update the 'action' state
  const [action, setAction] = useState('');

  // helper functions
  const registerLink = () => setAction('active'); // activates the register form
  const loginLink = () => setAction(''); // resets the action state to the login page

  return (
    //LoginRegister: component that renders the html
    <LoginRegister
      action={action} //property that gives info on what form is active(login or register)
      registerLink={registerLink} //used to activate the register form
      loginLink={loginLink} // used to activate the login form
    />
  );
};

export default LoginRegisterContainer;
