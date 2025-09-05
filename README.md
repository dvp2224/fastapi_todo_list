# ✨ Modern To-Do List - Full Stack Application

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

**A modern, feature-rich full-stack to-do list application with user authentication, real-time updates, and a beautiful responsive interface.**

[Features](#-features) • [Demo](#-demo) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [API Documentation](#-api-documentation)
- [Frontend Features](#-frontend-features)
- [Usage Examples](#-usage-examples)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

## 🎯 Overview

This is a complete full-stack to-do list application that demonstrates modern web development practices. It features a **FastAPI** backend with JWT authentication and a **React** frontend with a beautiful, responsive design built with **Tailwind CSS**.

### Key Highlights
- 🔐 **Secure Authentication** - JWT-based user authentication
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- ⚡ **Real-time Updates** - Instant task updates without page refresh
- 🎨 **Modern UI/UX** - Clean, intuitive interface with smooth animations
- 🔍 **Advanced Filtering** - Filter tasks by status (all, active, completed)
- 📊 **Progress Tracking** - Visual progress indicators and statistics
- 🔧 **Easy Setup** - Simple installation and configuration process

## ✨ Features

### Backend Features
- **RESTful API** with FastAPI
- **JWT Authentication** for secure user sessions
- **Password Hashing** with bcrypt for security
- **Data Validation** using Pydantic models
- **CORS Support** for cross-origin requests
- **Comprehensive Error Handling**
- **API Documentation** with Swagger UI
- **In-memory Database** (easily extendable to PostgreSQL/MongoDB)

### Frontend Features
- **React 18** with functional components and hooks
- **Modern Authentication Flow** with login/register
- **Task Management**: Create, read, update, delete tasks
- **Smart Filtering**: Filter by all, active, or completed tasks
- **Flexible Sorting**: Sort by newest, oldest, or alphabetical
- **Progress Visualization**: Progress bars and completion statistics
- **Responsive Design**: Mobile-first approach
- **Loading States**: Visual feedback for all operations
- **Error Handling**: User-friendly error messages
- **Local Storage**: Persistent login sessions
- **Keyboard Shortcuts**: Quick task creation with Enter key

## 🛠 Tech Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **Python 3.12+** - Programming language
- **Pydantic** - Data validation and settings management
- **python-jose** - JWT token handling
- **passlib** - Password hashing
- **uvicorn** - ASGI server

### Frontend
- **React 18** - Frontend JavaScript library
- **Tailwind CSS** - Utility-first CSS framework
- **Font Awesome** - Icon library
- **Babel** - JavaScript compiler
- **HTML5** - Markup language

### Development Tools
- **VS Code** - Recommended IDE
- **Git** - Version control
- **curl** - API testing

## 📁 Project Structure

```
fastapi_todo_list/
├── 📄 main1.py              # Main FastAPI application
├── 🔐 security.py           # Authentication & JWT handling
├── 🎨 frontend.html         # Complete React frontend
├── 📚 README.md             # Project documentation
├── 🗂️ __pycache__/          # Python cache files
└── 📋 requirements.txt      # Python dependencies (to be created)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Modern web browser (Chrome, Firefox, Safari, Edge)

### 1. Clone the Repository
```bash
git clone https://github.com/dvp2224/fastapi_todo_list.git
cd fastapi_todo_list
```

### 2. Install Dependencies
```bash
pip install "fastapi[all]" "passlib[bcrypt]" python-jose
```

### 3. Start the Backend
```bash
uvicorn main1:app --reload --host 0.0.0.0 --port 8000
```

### 4. Open the Frontend
Open `frontend.html` in your web browser or serve it with a simple HTTP server:
```bash
python3 -m http.server 3000
# Then open http://localhost:3000/frontend.html
```

### 5. Start Using the App! 🎉
1. Register a new account
2. Login with your credentials
3. Start managing your tasks!

## 🔧 Installation

### Detailed Installation Steps

1. **Set up Python Environment** (Recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Python Dependencies**
   ```bash
   pip install --upgrade pip
   pip install "fastapi[all]" "passlib[bcrypt]" python-jose
   ```

3. **Create Requirements File**
   ```bash
   pip freeze > requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python -c "import fastapi, passlib, jose; print('All dependencies installed successfully!')"
   ```

## ⚙️ Configuration

### Environment Variables
Create a `.env` file for production settings:
```env
SECRET_KEY=your-super-secret-key-here-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Backend Configuration
Modify `security.py` to use environment variables:
```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
```

### Frontend Configuration
Update the API base URL in `frontend.html` if needed:
```javascript
const API_BASE = 'http://127.0.0.1:8000'; // Change this for production
```

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /register/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

#### Login
```http
POST /token
Content-Type: application/json

{
    "username": "your_username", 
    "password": "your_password"
}
```

### Protected Endpoints (Require JWT Token)

#### Get All Tasks
```http
GET /todos/
Authorization: Bearer {your_jwt_token}
```

#### Create Task
```http
POST /todos/
Authorization: Bearer {your_jwt_token}
Content-Type: application/json

{
    "task": "Your task description (5-100 characters)",
    "completed": false
}
```

#### Update Task
```http
PUT /todos/{task_id}
Authorization: Bearer {your_jwt_token}
Content-Type: application/json

{
    "id": 1,
    "task": "Updated task description",
    "completed": true
}
```

#### Delete Task
```http
DELETE /todos/{task_id}
Authorization: Bearer {your_jwt_token}
```

### Interactive API Documentation
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🎨 Frontend Features

### User Interface Components
- **Authentication Pages**: Beautiful login and registration forms
- **Dashboard**: Comprehensive task management interface
- **Task Cards**: Individual task items with inline editing
- **Progress Indicators**: Visual progress bars and statistics
- **Responsive Navigation**: Mobile-friendly navigation

### User Experience Features
- **Smooth Animations**: CSS transitions and animations
- **Loading States**: Visual feedback during API calls
- **Error Handling**: User-friendly error messages
- **Form Validation**: Real-time form validation
- **Keyboard Shortcuts**: Efficient task management

## 💡 Usage Examples

### Using cURL for API Testing

1. **Register a new user:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/register/" \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "password": "securepassword"}'
   ```

2. **Login and get token:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/token" \
        -H "Content-Type: application/json" \
        -d '{"username": "testuser", "password": "securepassword"}'
   ```

3. **Create a task:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/todos/" \
        -H "Authorization: Bearer YOUR_TOKEN_HERE" \
        -H "Content-Type: application/json" \
        -d '{"task": "Learn FastAPI and build amazing apps"}'
   ```

4. **Get all tasks:**
   ```bash
   curl -X GET "http://127.0.0.1:8000/todos/" \
        -H "Authorization: Bearer YOUR_TOKEN_HERE"
   ```

### Using the Web Interface

1. **Registration**: 
   - Open the frontend in your browser
   - Click "Create Account"
   - Enter username (3+ characters) and password (6+ characters)
   - Confirm password and submit

2. **Task Management**:
   - Add tasks using the input field (5-100 characters)
   - Click the circle to mark tasks as complete
   - Use edit button to modify task text
   - Delete tasks with the trash icon
   - Filter tasks using the filter buttons

3. **Dashboard Features**:
   - View completion statistics
   - Track progress with visual indicators
   - Sort tasks by different criteria
   - Monitor your productivity

## 🧪 Testing

### Manual Testing Checklist

#### Backend Testing
- [ ] API endpoints respond correctly
- [ ] Authentication works properly
- [ ] Data validation functions correctly
- [ ] Error handling returns appropriate messages
- [ ] CORS headers are present

#### Frontend Testing
- [ ] User registration and login flow
- [ ] Task CRUD operations
- [ ] Responsive design on different screen sizes
- [ ] Error handling and user feedback
- [ ] Data persistence across browser sessions

### Automated Testing (Future Enhancement)
```bash
# Backend tests with pytest
pip install pytest httpx
pytest tests/

# Frontend tests with Jest
npm install --save-dev jest
npm test
```

## 🚀 Deployment

### Backend Deployment Options

#### 1. Heroku
```bash
# Create Procfile
echo "web: uvicorn main1:app --host=0.0.0.0 --port=${PORT:-5000}" > Procfile

# Deploy
heroku create your-app-name
git push heroku main
```

#### 2. Docker
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main1:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### 3. AWS Lambda
Use **Mangum** to wrap the FastAPI app for serverless deployment.

### Frontend Deployment Options

#### 1. Netlify/Vercel
- Simply upload the `frontend.html` file
- Configure the API base URL for production

#### 2. GitHub Pages
- Create a repository
- Upload the frontend file
- Enable GitHub Pages in settings

#### 3. AWS S3 + CloudFront
- Upload to S3 bucket
- Configure CloudFront distribution
- Set up custom domain

### Environment-Specific Configuration

#### Production Settings
```python
# security.py - Production settings
SECRET_KEY = os.getenv("SECRET_KEY")  # Use strong secret key
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours
CORS_ORIGINS = ["https://yourdomain.com"]  # Specific origins only
```

#### Frontend Production Build
```javascript
// Update API_BASE for production
const API_BASE = process.env.NODE_ENV === 'production' 
    ? 'https://your-api-domain.com' 
    : 'http://127.0.0.1:8000';
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Contributing Guidelines

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Add tests** for new functionality
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Setup

1. Fork and clone the repo
2. Create a virtual environment
3. Install dependencies
4. Make your changes
5. Test thoroughly
6. Submit a pull request

### Code Style Guidelines

- **Python**: Follow PEP 8 style guide
- **JavaScript**: Use ES6+ features
- **Comments**: Write clear, descriptive comments
- **Documentation**: Update docs for new features

### Reporting Issues

Found a bug? Have a feature request? Please create an issue:

1. Check if the issue already exists
2. Use the appropriate issue template
3. Provide detailed reproduction steps
4. Include screenshots if relevant

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 FastAPI Todo List Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🆘 Support

### Getting Help

- **Documentation**: Check this README and API docs
- **Issues**: Create an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the maintainers

### Common Issues & Solutions

#### Backend Issues

**Issue**: `ImportError: attempted relative import with no known parent package`
```bash
# Solution: Use absolute imports
# Change: from .security import ...
# To: from security import ...
```

**Issue**: `ModuleNotFoundError: No module named 'jose'`
```bash
# Solution: Install the correct package
pip install python-jose[cryptography]
```

#### Frontend Issues

**Issue**: CORS errors in browser console
```javascript
// Solution: Enable CORS in backend (already configured)
// Or serve frontend from same origin as backend
```

**Issue**: API calls failing
```javascript
// Solution: Check API_BASE URL in frontend.html
// Ensure backend is running on correct port
```

### System Requirements

- **Python**: 3.7 or higher
- **Browser**: Chrome 80+, Firefox 75+, Safari 13+, Edge 80+
- **Memory**: 512MB RAM minimum
- **Storage**: 50MB free space

### Performance Tips

- Use a reverse proxy (nginx) for production
- Enable gzip compression
- Implement caching strategies
- Monitor with tools like Sentry
- Use a proper database for production

## 🎉 Acknowledgments

- **FastAPI Team** - For the amazing web framework
- **React Team** - For the powerful frontend library
- **Tailwind CSS** - For the utility-first CSS framework
- **Contributors** - Thank you to all contributors!

---

<div align="center">

**Made with ❤️ using FastAPI and React**

⭐ Star this repo if you found it helpful!

[🔝 Back to Top](#-modern-to-do-list---full-stack-application)

</div>
