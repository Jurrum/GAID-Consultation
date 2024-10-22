// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';

import { AuthProvider, AuthContext } from './context/AuthContext';
import Register from './components/Auth/Register';
import Login from './components/Auth/Login';
import ChatbotComponent from './components/Chatbot/ChatbotComponent';

const PrivateRoute = ({ component: Component, ...rest }) => {
    const { auth } = React.useContext(AuthContext);
    return (
        <Route
            {...rest}
            render={props =>
                auth.isAuthenticated ? (
                    <Component {...props} />
                ) : (
                    <Redirect to="/login" />
                )
            }
        />
    );
};

function App() {
    return (
        <AuthProvider>
            <Router>
                <Switch>
                    <Route path="/register" component={Register} />
                    <Route path="/login" component={Login} />
                    <PrivateRoute path="/chatbot" component={ChatbotComponent} />
                    <Redirect from="/" to="/login" />
                </Switch>
            </Router>
        </AuthProvider>
    );
}

export default App;
