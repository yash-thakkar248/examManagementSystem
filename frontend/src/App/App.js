import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from "../login/login";
import Signup from "../signUp/signup";
import Navbar from '../Navbar/navbar';

const App = () => {
  return (
    <Router>
      <div className="App">
        <Navbar/>
        <Switch>
          <Route exact={true} path="/login" component={Login} />
          <Route exact={true} path="/signup" component={Signup} />
          {/* Other routes can be added here */}
        </Switch>
      </div>
    </Router>
  );
};

export default App;
