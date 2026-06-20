import { useState, useEffect, useRef } from 'react'
import './App.css'

function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [quizMode, setQuizMode] = useState(false)
  const [quiz, setQuiz] = useState(null)
  const [userAnswers, setUserAnswers] = useState({})
  const [showResults, setShowResults] = useState(false)
  const messagesEndRef = useRef(null)

  const API_URL = 'http://localhost:8000'

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const sendMessage = async () => {
    if (!input.trim()) return

    const userMessage = { type: 'user', text: input }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      })

      const data = await response.json()
      const botMessage = {
        type: 'bot',
        text: data.translated_response,
        language: data.detected_language,
        original: data.response
      }
      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      setMessages(prev => [...prev, { type: 'bot', text: 'Error connecting to server. Please try again.' }])
    }

    setLoading(false)
  }

  const generateQuiz = async (subject) => {
    setLoading(true)
    try {
      const response = await fetch(`${API_URL}/quiz`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ subject, num_questions: 3 })
      })

      const data = await response.json()
      if (data.error) {
        alert(data.error)
      } else {
        setQuiz(data)
        setQuizMode(true)
        setUserAnswers({})
        setShowResults(false)
      }
    } catch (error) {
      alert('Error generating quiz')
    }
    setLoading(false)
  }

  const handleAnswerSelect = (questionIndex, answer) => {
    setUserAnswers(prev => ({ ...prev, [questionIndex]: answer }))
  }

  const submitQuiz = () => {
    setShowResults(true)
  }

  const calculateScore = () => {
    let correct = 0
    quiz.questions.forEach((q, index) => {
      if (userAnswers[index] === q.answer) correct++
    })
    return correct
  }

  const clearHistory = async () => {
    try {
      await fetch(`${API_URL}/history`, { method: 'DELETE' })
      setMessages([])
    } catch (error) {
      console.error('Error clearing history')
    }
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🌍 Multilingual Learning Chatbot</h1>
        <p>Ask questions in any language • Get instant answers • Take quizzes</p>
      </header>

      <div className="container">
        {!quizMode ? (
          <>
            <div className="chat-box">
              {messages.length === 0 && (
                <div className="welcome">
                  <h2>👋 Welcome!</h2>
                  <p>Ask me about Math, Science, Programming, History, or Languages</p>
                  <p>I'll detect your language and respond accordingly!</p>
                </div>
              )}

              {messages.map((msg, index) => (
                <div key={index} className={`message ${msg.type}`}>
                  <div className="message-content">
                    {msg.text}
                    {msg.language && msg.language !== 'en' && (
                      <span className="language-tag">{msg.language}</span>
                    )}
                  </div>
                </div>
              ))}

              {loading && (
                <div className="message bot">
                  <div className="message-content typing">Thinking...</div>
                </div>
              )}

              <div ref={messagesEndRef} />
            </div>

            <div className="input-area">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
                placeholder="Type your question in any language..."
                disabled={loading}
              />
              <button onClick={sendMessage} disabled={loading || !input.trim()}>
                Send
              </button>
            </div>

            <div className="actions">
              <button onClick={() => generateQuiz('math')} className="quiz-btn">
                📊 Math Quiz
              </button>
              <button onClick={() => generateQuiz('science')} className="quiz-btn">
                🔬 Science Quiz
              </button>
              <button onClick={() => generateQuiz('programming')} className="quiz-btn">
                💻 Programming Quiz
              </button>
              <button onClick={clearHistory} className="clear-btn">
                🗑️ Clear History
              </button>
            </div>
          </>
        ) : (
          <div className="quiz-container">
            <div className="quiz-header">
              <h2>📝 {quiz.subject.toUpperCase()} Quiz</h2>
              <button onClick={() => setQuizMode(false)} className="back-btn">
                ← Back to Chat
              </button>
            </div>

            {quiz.questions.map((q, index) => (
              <div key={index} className="quiz-question">
                <h3>Question {index + 1}: {q.question}</h3>
                <div className="options">
                  {q.options.map((option, optIndex) => (
                    <label
                      key={optIndex}
                      className={`option ${
                        showResults
                          ? option === q.answer
                            ? 'correct'
                            : userAnswers[index] === option
                            ? 'incorrect'
                            : ''
                          : userAnswers[index] === option
                          ? 'selected'
                          : ''
                      }`}
                    >
                      <input
                        type="radio"
                        name={`question-${index}`}
                        value={option}
                        checked={userAnswers[index] === option}
                        onChange={() => handleAnswerSelect(index, option)}
                        disabled={showResults}
                      />
                      {option}
                    </label>
                  ))}
                </div>
              </div>
            ))}

            {!showResults ? (
              <button
                onClick={submitQuiz}
                className="submit-btn"
                disabled={Object.keys(userAnswers).length !== quiz.questions.length}
              >
                Submit Quiz
              </button>
            ) : (
              <div className="results">
                <h2>🎉 Results</h2>
                <p className="score">
                  You scored {calculateScore()} out of {quiz.questions.length}
                </p>
                <button onClick={() => setQuizMode(false)} className="back-btn">
                  Back to Chat
                </button>
              </div>
            )}
          </div>
        )}
      </div>

      <footer className="footer">
        <p>Powered by FastAPI + React • Supports 50+ languages</p>
      </footer>
    </div>
  )
}

export default App
