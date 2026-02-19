# University Admissions Assistant Chatbot

An AI-powered, context-aware chatbot that helps students explore university admission details — academic programs, eligibility criteria, fees, entrance exams, specializations, and career scope — through natural conversation.

Built with **Flask** and the **Groq API** — designed to behave like a real university admissions counselor rather than a rigid FAQ or menu-based system.

---

## Project Overview

Students often struggle to navigate admission-related information due to fragmented program details, complex eligibility rules, and static help systems.

This project addresses that problem by providing an interactive admissions assistant that understands conversational queries and responds accurately using structured academic data. All responses are generated strictly from a predefined knowledge base — eliminating hallucination and ensuring factual correctness.

---

## Key Features

### 🤖 AI-Powered Conversations
- Uses the **Groq API** for intelligent, natural language responses
- All answers are grounded in structured university data — no hallucination
- Warm, counselor-like tone with well-formatted responses

### 💬 Multi-Turn Conversation Memory
- Remembers previously discussed departments and programs via session-based history
- Supports follow-up questions without requiring repetition
- History capped at 20 turns to balance context and performance

### 📚 Comprehensive University Coverage
Supports programs across **7 university departments**:

| Department | Programs |
|--------|----------|
| Architecture | B.Arch, M.Arch |
| Engineering | B.Tech, M.Tech |
| Humanities & Social Sciences | BA, MA |
| Law | BA LL.B., LL.M. |
| Management | BBA, MBA |
| Pharmacy | B.Pharm, M.Pharm |
| Science | B.Sc, M.Sc |

### 📱 Responsive UI
- Chat-style interface with clear user/bot message distinction
- Typing indicator with animated dots
- Responsive design for mobile, tablet, and desktop

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| AI Engine | Groq API |
| Frontend | HTML, CSS, JavaScript |
| Data Storage | JSON |
| Environment Config | python-dotenv |

---

## Installation and Setup

### Prerequisites
- Python 3.10 or above
- A free Groq API key — [Get one here](https://console.groq.com)

### Quick Start

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

# Configure your API key — edit the .env file:
# GROQ_API_KEY=your_key_here

# Run the application
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## Project Structure

```
university-admissions-bot/
├── app.py                      # Flask backend server
├── chatbot.py                  # AI chatbot logic (Groq / Llama integration)
├── requirements.txt            # Python dependencies
├── .env                        # API key configuration (gitignored)
├── .gitignore                  # Git exclusion rules
├── data/
│   └── university_data.json    # Structured academic knowledge base
├── templates/
│   └── index.html              # Chat interface
├── static/
│   └── style.css               # Styling and responsive design
└── docs/
    └── PROJECT_DOCUMENTATION.md  # Detailed project documentation
```

---

## Example Interactions

### Exploring Engineering

> **User:** I want to know about engineering
>
> **Bot:** Engineering primarily offers the Bachelor of Technology (B.Tech). It is a 4-year undergraduate program with multiple specializations.
>
> **User:** What are the specializations?
>
> **Bot:** B.Tech specializations include Computer Science and Engineering, AI and ML, Data Science, Cyber Security, ECE, Mechanical, Civil, and EEE.
>
> **User:** What about eligibility?
>
> **Bot:** To be eligible for B.Tech, students must have completed 10+2 with Physics and Mathematics and qualify through an entrance exam.

### Context Switching

> **User:** career scope of btech
>
> **Bot:** Career opportunities include Software Engineer, AI Engineer, Core Engineering roles, and Research positions.
>
> **User:** What about MBA eligibility?
>
> **Bot:** Candidates must have a bachelor's degree and a valid management entrance exam score.

### Minimal Input with Memory

> **User:** arch
>
> **Bot:** Bachelor of Architecture is a 5-year program with NATA as the entrance exam.
>
> **User:** fees?
>
> **Bot:** The total fee ranges between 14 and 15 Lakhs.

---

## How It Works

1. The university knowledge base (`university_data.json`) is loaded at startup
2. The entire dataset is formatted and embedded into the LLM's **system prompt**
3. When a user sends a message, it's combined with conversation history and sent to the **Groq API**
4. The model generates a grounded response using only the provided data
5. Conversation history is maintained server-side via Flask sessions

---

## Scalability and Extensibility

- **Add programs** — Update `university_data.json`; no code changes needed
- **Add fields** — Scholarships, deadlines, placements — supported without modifying chatbot logic
- **Swap models** — Change the model parameter in `chatbot.py` to use any Groq-supported model
- **Scale data** — Migrate to RAG (Retrieval-Augmented Generation) for larger knowledge bases

---

## Limitations

- Responds only to information present in the knowledge base
- No user authentication or personalization
- Context resets on page refresh
- Requires an active internet connection for API calls

---

## License

This project is intended for academic and demonstration use.

---

## Author

**Rajarshi Ghosh**
B.Tech – Computer Science and Engineering

[GitHub](https://github.com/itsrajarshi) · [LinkedIn](https://linkedin.com/in/itsrajarshi)
