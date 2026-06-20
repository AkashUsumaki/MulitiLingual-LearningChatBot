from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from langdetect import detect
from googletrans import Translator
import random
from datetime import datetime

app = FastAPI(title="Multilingual AI Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = Translator()
chat_history = []

# Comprehensive Knowledge Base
knowledge_base = {
    # Greetings & Basic
    "greeting": "Hello! I'm your multilingual AI assistant. I can help you with languages, education, general knowledge, and conversations. Ask me anything!",
    "help": "I can help you with: 1) Learn any language (Spanish, French, German, Italian, Portuguese, Mandarin, Japanese, Korean, Arabic, Russian, Hindi), 2) Answer questions about Math, Science, Programming, History, Geography, 3) Have conversations, 4) Translate between languages, 5) Provide information on any topic. Just ask!",
    
    # Languages
    "spanish": "Spanish (Español) is spoken by 500+ million people. Key phrases: Hola (Hello), Gracias (Thank you), ¿Cómo estás? (How are you?), Buenos días (Good morning), Te amo (I love you), Por favor (Please), Lo siento (Sorry). Grammar uses el/la for gender. Great for travel in Spain and Latin America!",
    "french": "French (Français) is spoken in 29 countries. Key phrases: Bonjour (Hello), Merci (Thank you), Comment allez-vous? (How are you?), Bonne journée (Good day), Je t'aime (I love you), S'il vous plaît (Please), Pardon (Sorry). Beautiful language of culture and diplomacy!",
    "german": "German (Deutsch) has 100+ million speakers. Key phrases: Guten Tag (Hello), Danke (Thank you), Wie geht es Ihnen? (How are you?), Guten Morgen (Good morning), Ich liebe dich (I love you), Bitte (Please), Entschuldigung (Sorry). Important for business!",
    "italian": "Italian (Italiano) is the language of art. Key phrases: Ciao (Hello), Grazie (Thank you), Come stai? (How are you?), Buongiorno (Good morning), Ti amo (I love you), Per favore (Please), Mi dispiace (Sorry). Perfect for food and culture!",
    "japanese": "Japanese (日本語) uses 3 writing systems. Key phrases: こんにちは (Konnichiwa - Hello), ありがとう (Arigatō - Thank you), お元気ですか? (Ogenki desu ka? - How are you?), おはよう (Ohayō - Good morning), 愛してる (Aishiteru - I love you). Rich culture!",
    "mandarin": "Mandarin Chinese (中文) is spoken by 1+ billion. Key phrases: 你好 (Nǐ hǎo - Hello), 谢谢 (Xièxie - Thank you), 你好吗? (Nǐ hǎo ma? - How are you?), 早上好 (Zǎoshang hǎo - Good morning), 我爱你 (Wǒ ài nǐ - I love you). Essential for Asia!",
    
    # Education
    "math": "Mathematics includes: Algebra (equations, variables), Calculus (derivatives, integrals), Geometry (shapes, angles), Statistics (data analysis), Trigonometry (sin, cos, tan). Math is the universal language of logic and problem-solving!",
    "science": "Science explores our world: Physics (matter, energy, motion), Chemistry (elements, reactions), Biology (life, cells, DNA), Astronomy (space, planets), Earth Science (geology, weather). Science explains how everything works!",
    "programming": "Programming languages: Python (AI, data science), JavaScript (web development), Java (enterprise), C++ (systems), SQL (databases). Programming powers all modern technology. Learn to code to create the future!",
    "history": "History teaches us: Ancient Civilizations (Egypt, Rome, Greece), Medieval Period, Renaissance (art, science), Industrial Revolution, World Wars, Modern Era. Understanding history helps us build a better future!",
    
    # General Knowledge
    "weather": "Weather is the atmospheric condition at a specific time and place. It includes temperature, humidity, precipitation, wind, and clouds. Climate is the long-term weather pattern. Weather affects our daily lives and activities!",
    "food": "Food provides energy and nutrients for our bodies. Different cultures have unique cuisines: Italian (pasta, pizza), Chinese (rice, noodles), Mexican (tacos, burritos), Indian (curry, naan), Japanese (sushi, ramen). Healthy eating is important!",
    "travel": "Travel broadens your horizons! Popular destinations: Paris (Eiffel Tower), Tokyo (culture), New York (city life), Rome (history), London (museums). Travel tips: learn basic phrases, respect local customs, try local food, stay safe!",
    "music": "Music is universal! Genres: Classical, Rock, Pop, Jazz, Hip-Hop, Electronic, Country, R&B. Music affects emotions, reduces stress, and brings people together. Every culture has unique musical traditions!",
    "sports": "Popular sports: Football/Soccer (most popular worldwide), Basketball, Tennis, Cricket, Baseball, Swimming, Athletics. Sports promote health, teamwork, and discipline. Exercise is essential for well-being!",
    "technology": "Modern technology: AI (Artificial Intelligence), Cloud Computing, Blockchain, IoT (Internet of Things), 5G, Virtual Reality, Quantum Computing. Technology is rapidly changing how we live, work, and communicate!",
}

class ChatRequest(BaseModel):
    message: str
    language: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    detected_language: str
    translated_response: str
    timestamp: str

class QuizRequest(BaseModel):
    subject: str
    num_questions: int = 3

def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return "en"

def translate_text(text: str, target_lang: str) -> str:
    try:
        if target_lang == "en":
            return text
        translated = translator.translate(text, dest=target_lang)
        return translated.text
    except:
        return text

def get_intelligent_response(question: str) -> str:
    q = question.lower()
    
    # Greetings
    if any(w in q for w in ["hello", "hi", "hey", "hola", "bonjour", "namaste", "konnichiwa"]):
        return knowledge_base["greeting"]
    
    # Help
    if any(w in q for w in ["help", "what can you do", "capabilities", "ayuda"]):
        return knowledge_base["help"]
    
    # Language learning
    if "spanish" in q or "español" in q:
        return knowledge_base["spanish"]
    if "french" in q or "français" in q or "francais" in q:
        return knowledge_base["french"]
    if "german" in q or "deutsch" in q:
        return knowledge_base["german"]
    if "italian" in q or "italiano" in q:
        return knowledge_base["italian"]
    if "japanese" in q or "日本語" in q:
        return knowledge_base["japanese"]
    if "mandarin" in q or "chinese" in q or "中文" in q:
        return knowledge_base["mandarin"]
    
    # Education
    if any(w in q for w in ["math", "mathematics", "algebra", "calculus", "geometry"]):
        return knowledge_base["math"]
    if any(w in q for w in ["science", "physics", "chemistry", "biology"]):
        return knowledge_base["science"]
    if any(w in q for w in ["programming", "code", "python", "javascript"]):
        return knowledge_base["programming"]
    if any(w in q for w in ["history", "historical", "ancient"]):
        return knowledge_base["history"]
    
    # General topics
    if any(w in q for w in ["weather", "climate", "temperature"]):
        return knowledge_base["weather"]
    if any(w in q for w in ["food", "eat", "cuisine", "recipe"]):
        return knowledge_base["food"]
    if any(w in q for w in ["travel", "trip", "vacation", "tourism"]):
        return knowledge_base["travel"]
    if any(w in q for w in ["music", "song", "melody"]):
        return knowledge_base["music"]
    if any(w in q for w in ["sport", "football", "basketball", "exercise"]):
        return knowledge_base["sports"]
    if any(w in q for w in ["technology", "tech", "ai", "computer"]):
        return knowledge_base["technology"]
    
    # Conversational responses
    if any(w in q for w in ["how are you", "how r u", "como estas", "comment allez"]):
        return "I'm doing great, thank you for asking! I'm here to help you with anything you need. How can I assist you today?"
    
    if any(w in q for w in ["your name", "who are you", "what are you"]):
        return "I'm a multilingual AI assistant created to help you learn languages, answer questions, and have conversations in any language. I can understand and respond in Spanish, French, German, Italian, Portuguese, Mandarin, Japanese, Korean, Arabic, Russian, Hindi, and many more!"
    
    if any(w in q for w in ["thank", "thanks", "gracias", "merci"]):
        return "You're very welcome! I'm happy to help. Feel free to ask me anything else!"
    
    if any(w in q for w in ["love you", "te amo", "je t'aime"]):
        return "That's very kind of you! I'm here to help you anytime. What would you like to know or learn today?"
    
    # Default intelligent response
    return f"That's an interesting question! While I don't have specific information about that exact topic in my knowledge base, I can help you with: languages (Spanish, French, German, Japanese, etc.), education (Math, Science, Programming, History), general topics (weather, food, travel, music, sports, technology), and conversations. What would you like to explore?"

@app.get("/")
def root():
    return {"message": "Multilingual AI Chatbot API", "status": "running"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        # Detect user's language
        detected_lang = detect_language(request.message)
        
        # Translate question to English for processing
        english_question = translate_text(request.message, "en") if detected_lang != "en" else request.message
        
        # Get intelligent response in English
        english_answer = get_intelligent_response(english_question)
        
        # Translate answer back to user's language
        translated_answer = translate_text(english_answer, detected_lang)
        
        response = ChatResponse(
            response=english_answer,
            detected_language=detected_lang,
            translated_response=translated_answer,
            timestamp=datetime.now().isoformat()
        )
        
        chat_history.append({
            "user_message": request.message,
            "bot_response": translated_answer,
            "language": detected_lang,
            "timestamp": response.timestamp
        })
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/quiz")
def generate_quiz(request: QuizRequest):
    quiz_db = {
        "math": [
            {"question": "What is 15 + 27?", "options": ["40", "42", "45", "52"], "answer": "42"},
            {"question": "What is 12 × 8?", "options": ["84", "96", "104", "88"], "answer": "96"},
        ],
        "science": [
            {"question": "What is H2O?", "options": ["Water", "Oxygen", "Hydrogen", "Carbon"], "answer": "Water"},
            {"question": "Closest planet to Sun?", "options": ["Venus", "Earth", "Mercury", "Mars"], "answer": "Mercury"},
        ],
        "programming": [
            {"question": "What is Python?", "options": ["Snake", "Programming Language", "Math Tool", "Game"], "answer": "Programming Language"},
            {"question": "HTML stands for?", "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Home Tool Markup Language", "None"], "answer": "Hyper Text Markup Language"},
        ],
    }
    
    subject = request.subject.lower()
    if subject not in quiz_db:
        return {"error": f"Subject not available. Choose: math, science, programming"}
    
    questions = quiz_db[subject]
    selected = random.sample(questions, min(request.num_questions, len(questions)))
    return {"subject": subject, "questions": selected, "total": len(selected)}

@app.get("/history")
def get_history():
    return {"history": chat_history[-20:], "total": len(chat_history)}

@app.delete("/history")
def clear_history():
    chat_history.clear()
    return {"message": "Chat history cleared"}

@app.get("/subjects")
def get_subjects():
    return {"subjects": list(knowledge_base.keys())}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
