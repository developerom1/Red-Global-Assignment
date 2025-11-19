# Red Global Assignment - Full-Stack Web Application

## 🚀 Project Overview

A complete full-stack web application built with modern technologies, featuring a responsive frontend, robust backend API, and database integration. This project demonstrates professional development practices including proper project structure, documentation, and deployment readiness.

## ✨ Features

- **Responsive Web Interface**: Modern, mobile-friendly UI built with HTML5, CSS3, and JavaScript
- **RESTful API**: Secure backend API with CRUD operations
- **Database Integration**: MongoDB/MySQL support for data persistence
- **Authentication**: User registration and login system with JWT
- **Real-time Updates**: Dynamic content loading without page refresh
- **Form Validation**: Client and server-side input validation
- **Error Handling**: Comprehensive error handling and user feedback
- **Security**: Input sanitization, CORS protection, and environment variables

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3 (with Flexbox/Grid)
- JavaScript (ES6+)
- Fetch API for HTTP requests

### Backend
- Python (Flask/FastAPI)
- RESTful API architecture
- JWT for authentication
- Password hashing with bcrypt

### Database
- MongoDB / MySQL
- Data modeling and relationships
- Query optimization

### Tools & Libraries
- Git for version control
- Environment variables for configuration
- CORS middleware
- Request validation

## 📁 Project Structure

```
Red-Global-Assignment/
│
├── frontend/
│   ├── index.html          # Main landing page
│   ├── dashboard.html      # User dashboard
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── css/
│   │   └── styles.css      # Main stylesheet
│   └── js/
│       ├── main.js         # Main JavaScript file
│       ├── auth.js         # Authentication logic
│       └── api.js          # API communication
│
├── backend/
│   ├── app.py              # Main application file
│   ├── config.py           # Configuration settings
│   ├── models/
│   │   └── user.py         # User model
│   ├── routes/
│   │   ├── auth.py         # Authentication routes
│   │   └── api.py          # API routes
│   ├── utils/
│   │   ├── db.py           # Database connection
│   │   └── helpers.py      # Utility functions
│   └── requirements.txt    # Python dependencies
│
├── database/
│   ├── schema.sql          # Database schema (MySQL)
│   └── seed.py             # Sample data
│
├── docs/
│   ├── Project_Documentation.docx
│   ├── API_Documentation.docx
│   └── Deployment_Guide.docx
│
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- MongoDB or MySQL installed and running
- Modern web browser (Chrome, Firefox, Edge)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/developerom1/Red-Global-Assignment.git
   cd Red-Global-Assignment
   ```

2. **Set up the backend**
   ```bash
   cd backend
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

4. **Set up the database**
   
   For MongoDB:
   ```bash
   # Make sure MongoDB is running
   mongod
   ```
   
   For MySQL:
   ```bash
   mysql -u root -p < database/schema.sql
   ```

5. **Run the backend server**
   ```bash
   cd backend
   python app.py
   # Server will start on http://localhost:5000
   ```

6. **Open the frontend**
   ```bash
   # Open frontend/index.html in your browser
   # Or use a local server:
   cd frontend
   python -m http.server 8000
   # Open http://localhost:8000 in your browser
   ```

## 📖 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "message": "User registered successfully",
  "user_id": "12345"
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "12345",
    "username": "johndoe",
    "email": "john@example.com"
  }
}
```

### Data Endpoints

#### Get All Items
```http
GET /api/items
Authorization: Bearer <token>
```

#### Create Item
```http
POST /api/items
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Sample Item",
  "description": "This is a sample item",
  "category": "general"
}
```

#### Update Item
```http
PUT /api/items/:id
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Item",
  "description": "Updated description"
}
```

#### Delete Item
```http
DELETE /api/items/:id
Authorization: Bearer <token>
```

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
# Server Configuration
PORT=5000
HOST=localhost
DEBUG=True

# Database Configuration
DB_TYPE=mongodb  # or mysql
DB_HOST=localhost
DB_PORT=27017    # 27017 for MongoDB, 3306 for MySQL
DB_NAME=red_global_db
DB_USER=your_username
DB_PASSWORD=your_password

# JWT Configuration
JWT_SECRET_KEY=your_super_secret_key_change_this_in_production
JWT_EXPIRATION=86400  # 24 hours in seconds

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000
```

## 🧪 Testing

### Manual Testing

1. **Test Registration**
   - Open the registration page
   - Fill in the form with valid data
   - Submit and verify success message

2. **Test Login**
   - Use registered credentials
   - Verify redirect to dashboard
   - Check token storage in localStorage

3. **Test CRUD Operations**
   - Create new items
   - Read/display items
   - Update existing items
   - Delete items

### Using Postman

1. Import the API collection (if provided)
2. Set environment variables
3. Test each endpoint
4. Verify responses

## 🚀 Deployment

### Backend Deployment (Heroku)

```bash
heroku create red-global-api
heroku config:set JWT_SECRET_KEY=your_secret_key
heroku config:set DB_TYPE=mongodb
# Set other environment variables
git push heroku main
```

### Frontend Deployment (Netlify/Vercel)

1. Connect your GitHub repository
2. Set build command: `npm run build` (if using build process)
3. Set publish directory: `frontend`
4. Deploy

### Database Deployment

- **MongoDB**: Use MongoDB Atlas (cloud)
- **MySQL**: Use PlanetScale, AWS RDS, or similar

## 📚 Additional Documentation

Detailed documentation is available in the `docs/` folder:

1. **Project_Documentation.docx**: Complete project overview, architecture, and design decisions
2. **API_Documentation.docx**: Comprehensive API reference with examples
3. **Deployment_Guide.docx**: Step-by-step deployment instructions

## 🔧 Configuration

### Database Schema

#### Users Table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

#### Items Table
```sql
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Developer Om**
- GitHub: [@developerom1](https://github.com/developerom1)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Thanks to Red Global for the assignment opportunity
- Inspiration from modern web application best practices
- Community resources and documentation

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact: your.email@example.com

## 🔄 Version History

- **v1.0.0** (2025-11-19): Initial release
  - Complete frontend with responsive design
  - RESTful API with authentication
  - Database integration
  - Comprehensive documentation

---

**Note**: This is a demonstration project for Red Global Assignment. Make sure to change all placeholder values (secret keys, passwords, etc.) before deploying to production.
