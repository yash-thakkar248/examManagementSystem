import React, { useState } from 'react';
import "./login.css";
import { Link } from "react-router-dom";
import { Alert } from 'react-bootstrap';


const Login = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(username, password)
    if (!username || !password) {
      setError('Please fill out all fields.');
      return;
    }

    if (password.length < 8) {
      setError('Enter a valid password');
      return;
    }

    await setError('Successfully logged into the account')
    // const response = await fetch('/login', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({ username, password }),
    // });
    // const data = await response.json();
    // onLogin(data);
  };

  return (
    <form onSubmit={handleSubmit} className="form-display">
      <h2>Log in</h2>
      {error && <Alert variant="danger">{error}</Alert>}
      <div className="form-group">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="form-control"
          required
        />
      </div>
      <div  >
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="form-control"
          required
        />
      </div>
      <div
        className="link"
        style={{
          textAlign: "center",
          fontWeight: 500,
          margin: "15px",
        }}
      >
        <Link to="/signup">Don't have account? Sign Up</Link>
      </div> 
      <button type="submit" className="btn-control">Log in</button>
    </form>
  );
};

export default Login;
