# 🚀 Quick Start Guide

## For Complete Beginners

### Step 1: Install Required Software

1. **Install Python** (if not installed)
   - Go to https://www.python.org/downloads/
   - Download Python 3.8 or higher
   - During installation, CHECK "Add Python to PATH"

2. **Install Node.js** (if not installed)
   - Go to https://nodejs.org/
   - Download LTS version
   - Install with default settings

### Step 2: Run the Backend

1. Open Command Prompt (Windows) or Terminal (Mac/Linux)

2. Navigate to backend folder:
```bash
cd "c:\Users\akash\Downloads\multilingual learning chatbot\backend"
```

3. Install Python packages:
```bash
pip install -r requirements.txt
```

4. Start the backend server:
```bash
python main.py
```

You should see: "Uvicorn running on http://0.0.0.0:8000"

**Keep this window open!**

### Step 3: Run the Frontend

1. Open a NEW Command Prompt/Terminal window

2. Navigate to frontend folder:
```bash
cd "c:\Users\akash\Downloads\multilingual learning chatbot\frontend"
```

3. Install Node packages (first time only):
```bash
npm install
```

4. Start the frontend:
```bash
npm run dev
```

You should see: "Local: http://localhost:5173"

### Step 4: Use the Chatbot

1. Open your browser
2. Go to: http://localhost:5173
3. Start chatting!

## 🎯 What Each Part Does

### Backend (FastAPI - Python)
- Handles all the logic
- Detects language
- Translates messages
- Stores knowledge base
- Generates quizzes

### Frontend (React - JavaScript)
- The visual interface you see
- Sends messages to backend
- Displays responses
- Shows quizzes

## 🔧 Common Issues & Solutions

### "Python not found"
- Reinstall Python and check "Add to PATH"
- Restart your computer

### "npm not found"
- Reinstall Node.js
- Restart your computer

### "Port already in use"
- Close other programs using port 8000 or 5173
- Or change the port in the code

### Backend won't start
- Make sure you're in the backend folder
- Check if all packages installed correctly
- Try: `pip install --upgrade pip` then reinstall

### Frontend shows "Cannot connect"
- Make sure backend is running first
- Check if backend is on http://localhost:8000

## 📝 Testing the Chatbot

Try these questions:
1. "What is Python?" (English)
2. "¿Qué es matemáticas?" (Spanish)
3. "Qu'est-ce que la chimie?" (French)
4. Click "Math Quiz" button
5. Answer questions and submit

## 🎨 Customizing

### Add Your Own Questions

1. Open `backend/main.py`
2. Find `knowledge_base` (around line 30)
3. Add your topic:
```python
"your_subject": {
    "your_topic": "Your explanation here"
}
```

### Change Colors

1. Open `frontend/src/App.css`
2. Find `#667eea` (purple color)
3. Replace with your color code

## 📚 Learning Resources

- **Python**: https://www.python.org/about/gettingstarted/
- **JavaScript**: https://javascript.info/
- **React**: https://react.dev/learn
- **FastAPI**: https://fastapi.tiangolo.com/tutorial/

## 🆘 Need Help?

1. Read error messages carefully
2. Google the error message
3. Check if all software is installed correctly
4. Make sure both backend and frontend are running

---

**Happy Learning! 🎓**
