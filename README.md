# Python Foundation Web Application

A Python foundation project demonstrating basic Python concepts through both console and web interfaces.

## Description

This project serves as a foundation for learning Python programming. It includes:

- Basic Python syntax and functions
- List comprehensions
- Function definitions and calls
- Main entry point pattern
- **Flask web application with interactive features**
- **RESTful API endpoints**
- **Modern responsive web interface**

## Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Create a virtual environment:

```bash
python3 -m venv venv
```

2. Activate the virtual environment:

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Console Application

```bash
python main.py
```

### Run the Web Application

```bash
python app.py
```

Then open your browser and go to: **http://localhost:8000**

### Available Web Pages

- **Home** (`/`) - Main landing page with project overview
- **Demo** (`/demo`) - Shows the original Python functionality in web format
- **Calculator** (`/calculator`) - Interactive calculator using your Python functions
- **API** (`/api/calculate`) - REST API endpoint for programmatic access

## Project Structure

```
01.FOUNDATION/
├── app.py              # Flask web application
├── main.py             # Original console application
├── requirements.txt    # Python dependencies (includes Flask)
├── README.md          # This file
├── templates/         # HTML templates for web interface
│   ├── index.html     # Home page
│   ├── demo.html      # Demo page
│   └── calculator.html # Interactive calculator
├── .vscode/          # VS Code configuration
│   ├── tasks.json    # Build and run tasks (includes Flask)
│   └── launch.json   # Debug configurations
└── .github/          # GitHub configuration
    └── copilot-instructions.md  # Copilot instructions
```

## Development

This project is set up for development in VS Code with:

- Python extension support
- Debugging configuration for both console and web applications
- Task runner for common operations
- **Flask development server with hot reload**

### VS Code Tasks (Ctrl+Shift+P → "Tasks: Run Task"):

- **Run Flask Web App** (default) - Starts the web server
- **Run Python Application** - Runs the console version
- **Run Tests** - Execute pytest
- **Format Code (Black)** - Code formatting
- **Lint Code (Flake8)** - Code linting

### VS Code Debug Configurations (F5):

- **Flask Web App** - Debug the web application
- **Python: Current File** - Debug any Python file
- **Python: Main Application** - Debug the console app
- **Python: Debug Tests** - Debug test execution

## Learning Objectives

- Understand Python project structure
- Learn basic Python syntax and functions
- Practice with lists, functions, and data structures
- Get familiar with Python development workflow
- **Learn web development with Flask framework**
- **Understand REST API design and implementation**
- **Experience responsive web design principles**
- **Practice with HTML templates and JavaScript integration**

## 🌐 Web Features

### Interactive Demo

- Visual representation of your Python code execution
- Real-time display of list operations and calculations
- Educational code explanations and examples

### Calculator Interface

- Interactive number input with validation
- Real-time API calls to your Python functions
- Error handling and user feedback
- Demonstrates AJAX and modern web development

### API Endpoints

- `POST /api/calculate` - Calculate sum and squares of number lists
- JSON request/response format for integration with other applications
- Proper error handling and HTTP status codes

## 🚀 Quick Start for Web Version

1. **Install dependencies**: Already done if you followed setup above
2. **Start the web server**:
   ```bash
   python app.py
   ```
3. **Open your browser**: Go to http://localhost:8000
4. **Explore the features**: Try the demo and calculator pages!

## 🌍 Accessing from Other Devices

The Flask app runs on `0.0.0.0:5000`, making it accessible from other devices on your network:

- Find your computer's local IP address
- Access from other devices using: `http://YOUR_IP_ADDRESS:5000`
