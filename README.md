# 🌍 Multilingual Learning Chatbot

A modern, intelligent chatbot that helps students learn in their native language. Built with React (Vite) and FastAPI.

## ✨ Features

- 🌐 **Automatic Language Detection** - Detects user's language automatically
- 🔄 **Real-time Translation** - Translates responses to user's language
- 📚 **Educational Q&A** - Answers questions about Math, Science, Programming, History, Languages
- 📝 **Quiz Generation** - Generate quizzes on different subjects
- 💬 **Chat History** - Stores conversation history
- 🎨 **Modern UI** - Clean, responsive design
- ⚡ **Fast & Lightweight** - Built with Vite for optimal performance

## 🏗️ Project Structure

```
multilingual-chatbot/
│
├── backend/
│   ├── main.py              # FastAPI application
│   └── requirements.txt     # Python dependencies
│
└── frontend/
    ├── src/
    │   ├── App.jsx          # Main React component
    │   ├── App.css          # Styles
    │   └── main.jsx         # Entry point
    ├── package.json
    └── vite.config.js
```

## 🚀 Installation Steps

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the server:
```bash
python main.py
```

Backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

Frontend will run on `http://localhost:5173`

## 🎯 Usage

1. Open your browser and go to `http://localhost:5173`
2. Type any question in any language
3. The chatbot will detect your language and respond accordingly
4. Click quiz buttons to generate subject-specific quizzes
5. View your chat history in the conversation

### Example Questions:
- "What is algebra?" (English)
- "¿Qué es la física?" (Spanish)
- "Qu'est-ce que Python?" (French)
- "プログラミングとは何ですか？" (Japanese)

## 📡 API Endpoints

### POST /chat
Send a message to the chatbot
```json
{
  "message": "What is calculus?"
}
```

### POST /quiz
Generate a quiz
```json
{
  "subject": "math",
  "num_questions": 3
}
```

### GET /history
Get chat history

### DELETE /history
Clear chat history

### GET /subjects
Get available subjects

## 🚢 Deployment

### Backend Deployment (Render/Railway/Heroku)

1. Create a `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Push to GitHub

3. Connect to your hosting platform

4. Set environment variables if needed

### Frontend Deployment (Vercel/Netlify)

1. Build the project:
```bash
npm run build
```

2. Deploy the `dist` folder to Vercel/Netlify

3. Update API_URL in App.jsx to your backend URL

### Docker Deployment (Optional)

**Backend Dockerfile:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Frontend Dockerfile:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
CMD ["npm", "run", "preview"]
```

## 🔧 Configuration

### Adding More Knowledge
Edit `knowledge_base` dictionary in `backend/main.py`:
```python
knowledge_base = {
    "your_subject": {
        "topic": "explanation"
    }
}
```

### Adding More Quiz Questions
Edit `quiz_database` dictionary in `backend/main.py`:
```python
quiz_database = {
    "your_subject": [
        {
            "question": "Your question?",
            "options": ["A", "B", "C", "D"],
            "answer": "A"
        }
    ]
}
```

## 🎨 Customization

### Change Theme Colors
Edit `frontend/src/App.css`:
- Primary color: `#667eea`
- Secondary color: `#764ba2`

### Supported Languages
The chatbot supports 50+ languages including:
- English, Spanish, French, German, Italian
- Chinese, Japanese, Korean
- Arabic, Hindi, Portuguese
- And many more!

## 🔮 Future Improvements

1. **Database Integration**
   - Use PostgreSQL/MongoDB for persistent storage
   - Store user profiles and progress

2. **Advanced NLP**
   - Integrate OpenAI GPT or Google PaLM
   - Better context understanding
   - More accurate answers

3. **User Authentication**
   - Login/signup system
   - Personal learning dashboard
   - Track progress over time

4. **Enhanced Features**
   - Voice input/output
   - Image-based questions
   - PDF document upload for Q&A
   - Flashcard generation
   - Study reminders

5. **Analytics Dashboard**
   - Learning statistics
   - Performance tracking
   - Subject-wise progress

6. **Mobile App**
   - React Native version
   - Offline mode
   - Push notifications

7. **Gamification**
   - Points and badges
   - Leaderboards
   - Daily challenges

8. **Social Features**
   - Study groups
   - Share quizzes
   - Peer learning

## 🐛 Troubleshooting

### Backend Issues
- **Port already in use**: Change port in `main.py`
- **Translation errors**: Check internet connection (Google Translate API requires internet)
- **Module not found**: Reinstall dependencies

### Frontend Issues
- **API connection failed**: Ensure backend is running on port 8000
- **CORS errors**: Check CORS middleware in backend
- **Build errors**: Delete `node_modules` and reinstall

## 📄 License

MIT License - Feel free to use for learning and projects!

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add more subjects and questions
- Improve UI/UX
- Add new features
- Fix bugs

## 📧 Support

For issues and questions, please create an issue on GitHub.

---

**Built with ❤️ for learners worldwide**
