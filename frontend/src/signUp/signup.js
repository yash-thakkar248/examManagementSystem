import React, { useState } from 'react';
import "./signup.css";
import { Link } from "react-router-dom";
import { Alert } from 'react-bootstrap';
// import { Dropdown, DropdownButton } from 'react-bootstrap';

const Signup = ({ onSignup }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setlastName] = useState('');
  const [email, setEmail] = useState('');
  const [role, setRole] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!firstName || !lastName || !email || !role || !username || !password) {
      setError('Please fill out all fields.');
      return;
    }
    if (!email.includes('@') || !email.includes('.')) {
      setError('Please enter a valid email address.');
      return;
    }
    if (password.length < 8) {
      setError('Password must be at least 8 characters long.');
      return;
    }

    await setError('Successfully created account')
    // const response = await fetch('/signup', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({ username, password, firstName, lastName, email, role }),
    // });
    // const data = await response.json();
    // onSignup(data);
  };

  return (
    <form onSubmit={handleSubmit} className="form-display">
      <h2>Sign up</h2>
      {error && <Alert variant="danger">{error}</Alert>}
      <div className="form-group">
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          className="form-control"
          required
        />
      </div>
      <div className="form-group">
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          onChange={(e) => setlastName(e.target.value)}
          className="form-control"
          required
        />
      </div>
      <div className="form-group">
        <input
          type="text"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="form-control"
          required
        />
      </div>
      <div className="form-group">
        <select
            id="role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="form-control"
            required
        >
            <option value="">Select Role</option>
            <option value="student">Student</option>
            <option value="instructor">Instructor</option>
        </select>
      </div>

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
      <div className="form-group">
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
          marginBottom: "15px",
        }}
      >
        <Link to="/login">Already have account? Login</Link>
      </div>      
        <button type="submit" className="btn-control">Sign up</button>
    </form>

  );
};

export default Signup;
