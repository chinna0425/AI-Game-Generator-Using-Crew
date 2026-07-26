# 🎮 AI Game Generator using CrewAI

An AI-powered multi-agent application built using **CrewAI** that automatically designs, develops, and reviews complete 2D Python games from a simple natural language prompt.

Instead of relying on a single LLM, this project simulates a real software development team where multiple AI agents collaborate to produce high-quality game code.

---

## 🚀 Features

- Multi-Agent AI workflow using CrewAI
- Automatic Game Design Document generation
- Complete Pygame code generation
- Automated code review and quality assurance
- Google Gemini LLM integration
- Google Search using Serper API
- Generates runnable Python game code

---

## 🏗️ Architecture

```
            User
              │
              ▼
     Game Designer Agent
              │
              ▼
     Game Design Document
              │
              ▼
 Senior Python Developer Agent
              │
              ▼
 Complete Pygame Source Code
              │
              ▼
      QA Engineer Agent
              │
              ▼
      Final Improved Game
```

---

## 🤖 AI Agents

### 🎨 Game Designer

Responsible for:

- Designing game mechanics
- Defining gameplay rules
- Creating objectives
- Defining controls
- Creating entities

---

### 👨‍💻 Senior Python Developer

Responsible for:

- Writing complete Pygame code
- Implementing gameplay
- Event handling
- Collision detection
- Game loop
- Rendering

---

### ✅ QA Engineer

Responsible for:

- Reviewing generated code
- Finding bugs
- Improving gameplay
- Improving readability
- Producing the final version

---

## 🛠 Tech Stack

- Python
- CrewAI
- Google Gemini
- Serper API
- Pygame

---

## 📂 Project Structure

```
AI-Game-Generator-CrewAI/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Game-Generator-CrewAI.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=your_api_key
SERPER_API_KEY=your_api_key
```

Run

```bash
python app.py
```

---

## 💬 Example Prompt

```
A fun endless runner where a character jumps over obstacles.
```

---

## 📌 Future Improvements

- Web UI using Gradio
- FastAPI backend
- Download generated game automatically
- Multiplayer game generation
- Additional AI agents
- Memory-enabled agents
- Docker support

---
