# Project Documentation
University Admissions Assistant Chatbot

---

## 1. Introduction

The University Admissions Assistant Chatbot is a conversational web application designed to help students explore university admission information through natural language interaction.

Powered by the **Groq API**, the chatbot delivers intelligent, context-aware responses grounded in a structured academic knowledge base — ensuring every answer is accurate and data-driven.

The project focuses on correctness, scalability, and usability rather than rule-heavy or hard-coded responses.

---

## 2. Objectives

The primary objectives of this project are:

- To simplify access to university admission information
- To allow students to interact using natural language
- To avoid rigid, menu-driven chatbot flows
- To ensure all responses are accurate, data-grounded, and hallucination-free
- To design a scalable system that can grow with additional data

---

## 3. System Overview

The system consists of four main layers:

1. **Frontend** — Chat-based web UI (HTML, CSS, JavaScript)
2. **Backend** — Application server (Flask)
3. **AI Engine** — LLM-powered response generation (Groq API)
4. **Knowledge Base** — Structured university data (JSON)

Each layer is decoupled to ensure maintainability and extensibility.

---

## 4. System Architecture

### 4.1 High-Level Architecture

```
User (Web Browser)
      ↓
Frontend (HTML, CSS, JavaScript)
      ↓  POST /chat
Flask Backend (app.py)
      ↓  Session-based conversation history
Chatbot Logic (chatbot.py)
      ↓  System prompt + university data + history
Groq API
      ↓
Structured Academic Data (JSON)
```

---

### 4.2 Data Flow

1. User enters a message in the chat interface
2. Message is sent to the Flask backend via a `POST /chat` request
3. Backend retrieves the session-based conversation history
4. Chatbot logic:
   - Constructs a system prompt containing the full university knowledge base
   - Appends conversation history for multi-turn context
   - Sends the combined prompt to Groq's Llama 3.3 70B model
5. The LLM generates a grounded, natural language response
6. Response is returned to the frontend and rendered in the chat interface
7. Conversation history is updated in the session (capped at 20 turns)

---

## 5. Knowledge Base Design

### 5.1 Data Format

The academic information is stored in a structured JSON format (`data/university_data.json`) with the following hierarchy:

- **Department** (e.g., Engineering, Architecture, Law)
  - **Programs** (e.g., B.Tech, B.Arch, MBA)
    - Attributes:
      - Name
      - Duration
      - Eligibility
      - Fees
      - Specializations (if applicable)
      - Entrance Exams (if applicable)
      - Career Scope (if applicable)

### 5.2 Covered Departments

| Department | Programs |
|------------|----------|
| Architecture | B.Arch, M.Arch |
| Engineering | B.Tech, M.Tech |
| Humanities & Social Sciences | BA, MA |
| Law | BA LL.B., LL.M. |
| Management | BBA, MBA |
| Pharmacy | B.Pharm, M.Pharm |
| Science | B.Sc, M.Sc |

### 5.3 Design Rationale

- JSON was chosen for simplicity and readability
- Enables easy modification without changing application logic
- Prevents data duplication
- Ensures a single source of truth
- The entire JSON is injected into the LLM system prompt, keeping all responses grounded

---

## 6. AI Chatbot Logic

### 6.1 LLM Integration

The chatbot uses the **Groq API** to generate responses. Key design decisions:

- **Grounded generation** — The entire university knowledge base is formatted and embedded in the system prompt, ensuring the LLM only responds with factual data
- **Strict instructions** — The system prompt includes explicit rules: no hallucination, no guessing, suggest available topics when asked about uncovered information
- **Temperature** — Set to `0.7` for a balance between accuracy and natural-sounding responses
- **Token limit** — Max 1024 tokens per response for concise answers

### 6.2 System Prompt Design

The system prompt instructs the LLM to:
1. Only answer using the provided university data
2. Politely decline questions not covered by the data
3. Keep responses concise, clear, and well-formatted
4. Use bullet points for lists
5. Be warm and encouraging — like a real admissions counselor
6. Introduce itself on greeting and suggest topics

### 6.3 Conversation Context

Multi-turn context is managed via Flask sessions:

- Each user gets an isolated conversation history stored server-side
- History is passed to the LLM as prior messages, enabling follow-up questions about programs, departments, and university information
- History is capped at **20 turns** (40 messages) to prevent token overflow
- Session resets when the user refreshes the page

### 6.4 Error Handling

- If the API key is missing or invalid, the chatbot displays a helpful configuration message
- If the Groq API fails (network issues, rate limits), a user-friendly fallback message is shown
- All errors are logged server-side for debugging

---

## 7. Backend Design

### 7.1 Flask Application (`app.py`)

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Serves the chat UI and resets conversation history |
| `/chat` | POST | Accepts user message, returns AI-generated response |

### 7.2 Environment Configuration

- API key is managed via a `.env` file using `python-dotenv`
- `.env` is excluded from version control via `.gitignore`

---

## 8. Frontend Design

### 8.1 User Interface

- Chat-style interface with message bubbles
- Clear visual distinction between user (purple) and bot (light blue) messages
- Typing indicator with animated dots for realistic interaction
- Keyboard (Enter) and button-based message submission
- Input is disabled during API calls to prevent duplicate messages
- Gradient background with modern card-based layout

### 8.2 Responsiveness

The UI is fully responsive and adapts to:

| Device | Behavior |
|--------|----------|
| Mobile (< 480px) | Full screen, no border radius |
| Tablet (481–768px) | Wider card (520px) |
| Desktop | Centered card (420px), 90vh height |
| Large screen (> 1440px) | Fixed 520px card |

Responsive design is implemented using CSS media queries.

---

## 9. Technology Stack

| Component | Technology |
|-----------|------------|
| Backend | Python, Flask |
| AI Engine | Groq API |
| Frontend | HTML, CSS, JavaScript |
| Data Storage | JSON |
| Environment Config | python-dotenv |
| Version Control | Git, GitHub |

---

## 10. Installation and Execution

### 10.1 Prerequisites

- Python 3.10 or above
- A free Groq API key ([Get one here](https://console.groq.com))
- Web browser

### 10.2 Setup Steps

```bash
# Clone the repository
git clone https://github.com/itsrajarshi/university-admissions-bot.git
cd university-admissions-bot

# (Recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Configure your API key
# Edit the .env file and add your Groq API key:
# GROQ_API_KEY=your_key_here

# Run the application
python app.py
```

Access the application at: **http://127.0.0.1:5000**

---

## 11. Project Structure

```
university-admissions-bot/
├── app.py                  # Flask backend server
├── chatbot.py              # AI chatbot logic (Groq/Llama integration)
├── requirements.txt        # Python dependencies
├── .env                    # API key configuration (gitignored)
├── .gitignore              # Git exclusion rules
├── README.md               # Project overview and usage guide
├── data/
│   └── university_data.json  # Structured academic knowledge base
├── templates/
│   └── index.html          # Chat interface HTML
├── static/
│   └── style.css           # UI styling and responsive design
└── docs/
    └── PROJECT_DOCUMENTATION.md  # This file
```

---

## 12. Limitations

- The chatbot responds only to information available in the knowledge base
- No authentication or user personalization
- Context is session-based and resets on page refresh
- No persistent storage for chat history
- Requires an active internet connection for Groq API calls

---

## 13. Scalability and Extensibility

The project is designed to be easily extensible:

- New programs can be added by updating the JSON file — no code changes required
- Additional fields such as scholarships, deadlines, or placements can be introduced seamlessly
- The knowledge base can be migrated to a database for larger datasets
- The AI model can be swapped by changing the model parameter in `chatbot.py`
- The architecture supports future enhancements like RAG (Retrieval-Augmented Generation) for larger knowledge bases

---

## 14. Future Enhancements

Potential future improvements include:

- Voice-based interaction
- Cloud deployment (e.g., Render, Railway, AWS)
- Admission deadline reminders and notifications
- RAG-based retrieval for scaling beyond system prompt limits
- Analytics dashboard for commonly asked queries
- User authentication and personalized recommendations

---

## 15. Conclusion

The University Admissions Assistant Chatbot demonstrates how a well-structured knowledge base combined with modern LLM capabilities can deliver an intelligent, data-grounded conversational experience.

By prioritizing accuracy, usability, and extensibility, the project provides a strong foundation for real-world academic information systems.

---

## 16. Author

**Rajarshi Ghosh**
B.Tech – Computer Science and Engineering

GitHub: [github.com/itsrajarshi](https://github.com/itsrajarshi)
LinkedIn: [linkedin.com/in/itsrajarshi](https://linkedin.com/in/itsrajarshi)