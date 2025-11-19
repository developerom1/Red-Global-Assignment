// API Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// Utility Functions
function showMessage(elementId, message, isError = false) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = message;
        element.style.display = 'block';
        
        // Hide after 5 seconds
        setTimeout(() => {
            element.style.display = 'none';
        }, 5000);
    }
}

function hideMessage(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = 'none';
    }
}

function getToken() {
    return localStorage.getItem('token');
}

function setToken(token) {
    localStorage.setItem('token', token);
}

function removeToken() {
    localStorage.removeItem('token');
}

function setUser(user) {
    localStorage.setItem('user', JSON.stringify(user));
}

function getUser() {
    const user = localStorage.getItem('user');
    return user ? JSON.parse(user) : null;
}

function isAuthenticated() {
    return !!getToken();
}

// Login Form Handler
const loginForm = document.getElementById('login-form');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        hideMessage('error-message');
        hideMessage('success-message');
        
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        
        try {
            const response = await fetch(`${API_BASE_URL}/auth/login`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password })
            });
            
            const data = await response.json();
            
            if (data.success) {
                setToken(data.data.token);
                setUser(data.data.user);
                showMessage('success-message', 'Login successful! Redirecting...');
                
                setTimeout(() => {
                    window.location.href = 'dashboard.html';
                }, 1500);
            } else {
                showMessage('error-message', data.message, true);
            }
        } catch (error) {
            showMessage('error-message', 'Network error. Please check if the server is running.', true);
            console.error('Login error:', error);
        }
    });
}

// Register Form Handler
const registerForm = document.getElementById('register-form');
if (registerForm) {
    registerForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        hideMessage('error-message');
        hideMessage('success-message');
        
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirm-password')?.value;
        
        // Client-side validation
        if (confirmPassword && password !== confirmPassword) {
            showMessage('error-message', 'Passwords do not match', true);
            return;
        }
        
        if (password.length < 6) {
            showMessage('error-message', 'Password must be at least 6 characters', true);
            return;
        }
        
        try {
            const response = await fetch(`${API_BASE_URL}/auth/register`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, email, password })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showMessage('success-message', 'Registration successful! Redirecting to login...');
                
                setTimeout(() => {
                    window.location.href = 'login.html';
                }, 1500);
            } else {
                showMessage('error-message', data.message, true);
            }
        } catch (error) {
            showMessage('error-message', 'Network error. Please check if the server is running.', true);
            console.error('Registration error:', error);
        }
    });
}

// Logout Function
function logout() {
    removeToken();
    localStorage.removeItem('user');
    window.location.href = 'index.html';
}

// Check Authentication on Protected Pages
if (window.location.pathname.includes('dashboard')) {
    if (!isAuthenticated()) {
        window.location.href = 'login.html';
    }
}

// Display User Info if Logged In
const userInfoElement = document.getElementById('user-info');
if (userInfoElement && isAuthenticated()) {
    const user = getUser();
    if (user) {
        userInfoElement.textContent = `Welcome, ${user.username}!`;
    }
}
