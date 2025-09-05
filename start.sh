#!/bin/bash

# FastAPI To-Do List Startup Script
# This script helps you quickly start the development environment

echo "🚀 FastAPI To-Do List Startup Script"
echo "=================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚙️  Creating .env file from template..."
    cp .env.example .env
    echo "📝 Please edit .env file with your configuration"
fi

# Start the backend server
echo "🌟 Starting FastAPI backend server..."
echo "📍 Backend will be available at: http://127.0.0.1:8000"
echo "📍 API Documentation: http://127.0.0.1:8000/docs"
echo "📍 Frontend: Open frontend.html in your browser"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

uvicorn main1:app --reload --host 0.0.0.0 --port 8000
