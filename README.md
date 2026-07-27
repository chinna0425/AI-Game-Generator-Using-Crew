# 🎮 AI Game Studio

> **Generate complete Python Pygame games using a team of AI agents powered by CrewAI, Google Gemini, and Serper.**

AI Game Studio is a multi-agent AI application that transforms a simple game idea into a fully playable **Python Pygame game**. Instead of relying on a single AI model, it uses a specialized team of AI agents that collaborate to design, develop, and review the game before presenting the final output.

---

## ✨ Features

- 🤖 Multi-Agent AI workflow using CrewAI
- 🎨 Automatic game design generation
- 👨‍💻 Complete Python (Pygame) code generation
- 🧪 AI-powered code review and validation
- 📄 Gameplay instructions generation
- 📦 Dependency recommendations
- 💻 Modern Gradio web interface
- 📥 Download generated Python game
- 🐳 Docker support
- ☁️ Deployment-ready

---

# 🏗️ Architecture

```
                   User
                     │
                     ▼
             Gradio Web Interface
                     │
                     ▼
             Game Generator Module
                     │
                     ▼
             CrewAI Orchestrator
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Game Designer   Python Developer   QA Engineer
      │              │              │
      └──────────────┼──────────────┘
                     ▼
              Output Parser
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
 generated_game.py      generated_game.txt
```

---

# 🧠 AI Workflow

### 🎨 Game Designer

Responsible for:

- Designing game mechanics
- Defining gameplay rules
- Creating objectives
- Planning player interactions

---

### 👨‍💻 Python Developer

Responsible for:

- Implementing the game using Pygame
- Writing clean and modular Python code
- Following the game design
- Producing executable code

---

### 🧪 QA Engineer

Responsible for:

- Reviewing generated code
- Checking for logical errors
- Improving output quality
- Preparing the final structured response

---

# 📂 Project Structure

```text
AI-Game-Studio/
│
├── app.py                  # Gradio Application
├── generator.py            # Game Generation Logic
├── agents.py               # AI Agents
├── tasks.py                # Crew Tasks
├── crew_builder.py         # Crew Configuration
├── output_parser.py        # Parses AI Output
│
├── generated/
│   ├── generated_game.py
│   └── generated_game.txt
│
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

## AI & LLM

- CrewAI
- Google Gemini
- Serper API

## Backend

- Python
- Regular Expressions
- python-dotenv

## Frontend

- Gradio

## Game Engine

- Pygame

## Deployment

- Docker
- Vercel

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/chinna0425/AI-Game-Generator-Using-Crew.git
```

```bash
cd AI-Game-Studio
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the project root.

```env
Google Gemini_API_KEY=YOUR_Google Gemini_API_KEY
SERPER_API_KEY=YOUR_SERPER_API_KEY
```

---

## 4. Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:7860
```

---

# 📖 How to Use

### Step 1

Enter a game idea.

Example:

```
A Snake game with power-ups and increasing difficulty.
```

---

### Step 2

Click:

```
🚀 Generate Game
```

---

### Step 3

The AI agents collaborate to generate:

- 📄 Game Design
- 💻 Python Code
- 📝 How to Play
- 📦 Requirements

---

### Step 4

Download:

```
generated_game.py
```

Run it using:

```bash
python generated_game.py
```

---

# 📌 Example

### Input

```
A Space Shooter where the player collects power-ups and defeats alien bosses.
```

### Output

- ✅ Game Design Document
- ✅ Complete Pygame Source Code
- ✅ Gameplay Instructions
- ✅ Required Dependencies

---

# 🎯 Skills Demonstrated

This project demonstrates experience with:

- Multi-Agent AI Systems
- CrewAI Framework
- LLM Orchestration
- Prompt Engineering
- Python Development
- Pygame
- Modular Software Architecture
- Gradio UI Development
- Docker
- Environment Variable Management

# 🐳 Docker

Build the Docker image:

```bash
docker build -t ai-game-studio .
```

Run the container:

```bash
docker run -p 7860:7860 ai-game-studio
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

# 👨‍💻 Author

**Kiran Kumar Kandula**

- GitHub: https://github.com/YOUR_USERNAME
- LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future development.

---

# 🙏 Acknowledgements

- CrewAI
- Google Gemini
- Gradio
- Pygame
- Serper API
