# 🏗️ Architecture Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER BROWSER                             │
│                     http://localhost:5173                        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP Requests
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                      FRONTEND (React + Vite)                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                       App.jsx                             │  │
│  │  ┌────────────────┐  ┌────────────────┐                 │  │
│  │  │  Chat Interface│  │ Quiz Interface │                 │  │
│  │  │  - Messages    │  │ - Questions    │                 │  │
│  │  │  - Input       │  │ - Options      │                 │  │
│  │  │  - Buttons     │  │ - Results      │                 │  │
│  │  └────────────────┘  └────────────────┘                 │  │
│  │                                                           │  │
│  │  State Management:                                       │  │
│  │  - messages, input, loading, quizMode, quiz, etc.       │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                       App.css                             │  │
│  │  - Gradient background                                    │  │
│  │  - Message bubbles                                        │  │
│  │  - Quiz styling                                           │  │
│  │  - Responsive design                                      │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ REST API Calls
                             │ (JSON)
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    BACKEND (FastAPI + Python)                    │
│                     http://localhost:8000                        │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                      main.py                              │  │
│  │                                                           │  │
│  │  ┌─────────────────────────────────────────────────┐    │  │
│  │  │            API Endpoints                        │    │  │
│  │  │  POST /chat      - Send message                 │    │  │
│  │  │  POST /quiz      - Generate quiz                │    │  │
│  │  │  GET /history    - Get chat history             │    │  │
│  │  │  DELETE /history - Clear history                │    │  │
│  │  │  GET /subjects   - List subjects                │    │  │
│  │  └─────────────────────────────────────────────────┘    │  │
│  │                                                           │  │
│  │  ┌─────────────────────────────────────────────────┐    │  │
│  │  │         Core Functions                          │    │  │
│  │  │  detect_language()  - Detect user language      │    │  │
│  │  │  translate_text()   - Translate text            │    │  │
│  │  │  find_answer()      - Search knowledge base     │    │  │
│  │  └─────────────────────────────────────────────────┘    │  │
│  │                                                           │  │
│  │  ┌─────────────────────────────────────────────────┐    │  │
│  │  │            Data Storage                         │    │  │
│  │  │  chat_history    - List of messages             │    │  │
│  │  │  knowledge_base  - Educational content          │    │  │
│  │  │  quiz_database   - Quiz questions               │    │  │
│  │  └─────────────────────────────────────────────────┘    │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                External Services                          │  │
│  │  - langdetect (Language Detection)                       │  │
│  │  - googletrans (Translation API)                         │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagrams

### 1. Chat Message Flow

```
┌──────────┐
│   User   │
│  Types   │
│ Message  │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│  Frontend       │
│  - Capture input│
│  - Show loading │
└────┬────────────┘
     │
     │ POST /chat
     │ { message: "¿Qué es Python?" }
     ▼
┌─────────────────────────────┐
│  Backend                    │
│  1. Detect language: "es"   │
│  2. Translate to English    │
│  3. Find answer             │
│  4. Translate back to "es"  │
│  5. Store in history        │
└────┬────────────────────────┘
     │
     │ Response
     │ { response: "...", translated_response: "...", language: "es" }
     ▼
┌─────────────────┐
│  Frontend       │
│  - Display msg  │
│  - Update UI    │
└─────────────────┘
     │
     ▼
┌──────────┐
│   User   │
│   Sees   │
│ Response │
└──────────┘
```

### 2. Quiz Generation Flow

```
┌──────────┐
│   User   │
│  Clicks  │
│Math Quiz │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│  Frontend       │
│  generateQuiz() │
└────┬────────────┘
     │
     │ POST /quiz
     │ { subject: "math", num_questions: 3 }
     ▼
┌─────────────────────────────┐
│  Backend                    │
│  1. Get quiz_database       │
│  2. Select random questions │
│  3. Return quiz object      │
└────┬────────────────────────┘
     │
     │ Response
     │ { subject: "math", questions: [...], total: 3 }
     ▼
┌─────────────────┐
│  Frontend       │
│  - Set quizMode │
│  - Display quiz │
└─────────────────┘
     │
     ▼
┌──────────┐
│   User   │
│ Answers  │
│Questions │
└────┬─────┘
     │
     ▼
┌─────────────────┐
│  Frontend       │
│  - Calculate    │
│  - Show results │
└─────────────────┘
```

---

## Component Interaction

```
┌─────────────────────────────────────────────────────────┐
│                    React App (App.jsx)                   │
│                                                          │
│  ┌──────────────┐         ┌──────────────┐            │
│  │   Header     │         │   Footer     │            │
│  │  - Title     │         │  - Info      │            │
│  └──────────────┘         └──────────────┘            │
│                                                          │
│  ┌────────────────────────────────────────────────┐   │
│  │            Main Container                      │   │
│  │                                                 │   │
│  │  IF quizMode = false:                          │   │
│  │  ┌──────────────────────────────────────┐     │   │
│  │  │        Chat Interface                │     │   │
│  │  │  ┌────────────────────────────┐     │     │   │
│  │  │  │   Message List             │     │     │   │
│  │  │  │   - User messages          │     │     │   │
│  │  │  │   - Bot messages           │     │     │   │
│  │  │  │   - Loading indicator      │     │     │   │
│  │  │  └────────────────────────────┘     │     │   │
│  │  │  ┌────────────────────────────┐     │     │   │
│  │  │  │   Input Area               │     │     │   │
│  │  │  │   - Text input             │     │     │   │
│  │  │  │   - Send button            │     │     │   │
│  │  │  └────────────────────────────┘     │     │   │
│  │  │  ┌────────────────────────────┐     │     │   │
│  │  │  │   Action Buttons           │     │     │   │
│  │  │  │   - Math Quiz              │     │     │   │
│  │  │  │   - Science Quiz           │     │     │   │
│  │  │  │   - Programming Quiz       │     │     │   │
│  │  │  │   - Clear History          │     │     │   │
│  │  │  └────────────────────────────┘     │     │   │
│  │  └──────────────────────────────────────┘     │   │
│  │                                                 │   │
│  │  IF quizMode = true:                           │   │
│  │  ┌──────────────────────────────────────┐     │   │
│  │  │        Quiz Interface                │     │   │
│  │  │  ┌────────────────────────────┐     │     │   │
│  │  │  │   Quiz Header              │     │     │   │
│  │  │  │   - Subject title          │     │     │   │
│  │  │  │   - Back button            │     │     │   │
│  │  │  └────────────────────────────┘     │     │   │
│  │  │  ┌────────────────────────────┐     │     │   │
│  │  │  │   Questions                │     │     │   │
│  │  │  │   - Question text          │     │     │   │
│  │  │  │   - Multiple options       │     │     │   │
│  │  │  │   - Selection state        │     │     │   │
│  │  │  └────────────────────────────┘     │     │   │
│  │  │  ┌────────────────────────────┐     │     │   │
│  │  │  │   Submit/Results           │     │     │   │
│  │  │  │   - Submit button          │     │     │   │
│  │  │  │   - Score display          │     │     │   │
│  │  │  └────────────────────────────┘     │     │   │
│  │  └──────────────────────────────────────┘     │   │
│  └────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## State Management Flow

```
┌─────────────────────────────────────────────────────────┐
│                   React State (useState)                 │
│                                                          │
│  messages: []                                            │
│    ↓                                                     │
│    User sends message                                    │
│    ↓                                                     │
│    setMessages([...messages, userMessage])              │
│    ↓                                                     │
│    API call to backend                                   │
│    ↓                                                     │
│    setMessages([...messages, userMessage, botMessage])  │
│    ↓                                                     │
│    UI re-renders with new messages                       │
│                                                          │
│  quizMode: false                                         │
│    ↓                                                     │
│    User clicks "Math Quiz"                               │
│    ↓                                                     │
│    setQuizMode(true)                                     │
│    ↓                                                     │
│    UI switches to quiz interface                         │
│                                                          │
│  userAnswers: {}                                         │
│    ↓                                                     │
│    User selects option                                   │
│    ↓                                                     │
│    setUserAnswers({...userAnswers, [index]: answer})    │
│    ↓                                                     │
│    UI updates selected option                            │
└─────────────────────────────────────────────────────────┘
```

---

## API Request/Response Format

### POST /chat

**Request:**
```json
{
  "message": "¿Qué es Python?",
  "language": null
}
```

**Response:**
```json
{
  "response": "Python is a high-level programming language...",
  "detected_language": "es",
  "translated_response": "Python es un lenguaje de programación...",
  "timestamp": "2024-01-15T10:30:00"
}
```

### POST /quiz

**Request:**
```json
{
  "subject": "math",
  "num_questions": 3
}
```

**Response:**
```json
{
  "subject": "math",
  "questions": [
    {
      "question": "What is 15 + 27?",
      "options": ["40", "42", "45", "52"],
      "answer": "42"
    }
  ],
  "total": 3
}
```

---

## Technology Stack Layers

```
┌─────────────────────────────────────────────────────────┐
│                    Presentation Layer                    │
│                    (User Interface)                      │
│  ┌────────────────────────────────────────────────┐    │
│  │  React Components (JSX)                        │    │
│  │  CSS3 Styling                                  │    │
│  │  Responsive Design                             │    │
│  └────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                    Application Layer                     │
│                    (Business Logic)                      │
│  ┌────────────────────────────────────────────────┐    │
│  │  React State Management                        │    │
│  │  Event Handlers                                │    │
│  │  API Integration                               │    │
│  └────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                      API Layer                           │
│                   (Communication)                        │
│  ┌────────────────────────────────────────────────┐    │
│  │  REST API (FastAPI)                            │    │
│  │  JSON Data Exchange                            │    │
│  │  CORS Middleware                               │    │
│  └────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                    Service Layer                         │
│                  (Core Functions)                        │
│  ┌────────────────────────────────────────────────┐    │
│  │  Language Detection (langdetect)               │    │
│  │  Translation (googletrans)                     │    │
│  │  Answer Matching                               │    │
│  │  Quiz Generation                               │    │
│  └────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                     Data Layer                           │
│                  (Storage)                               │
│  ┌────────────────────────────────────────────────┐    │
│  │  In-Memory Storage (Lists/Dicts)               │    │
│  │  - chat_history                                │    │
│  │  - knowledge_base                              │    │
│  │  - quiz_database                               │    │
│  └────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        Internet                          │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌───────────────┐         ┌───────────────┐
│   Frontend    │         │   Backend     │
│   (Vercel)    │◄───────►│   (Render)    │
│               │   API   │               │
│  React + Vite │  Calls  │    FastAPI    │
└───────────────┘         └───────┬───────┘
                                  │
                                  ▼
                          ┌───────────────┐
                          │   External    │
                          │   Services    │
                          │               │
                          │ - langdetect  │
                          │ - googletrans │
                          └───────────────┘
```

---

**This architecture provides:**
- ✅ Clear separation of concerns
- ✅ Scalable structure
- ✅ Easy to maintain
- ✅ Simple to understand
- ✅ Production-ready

