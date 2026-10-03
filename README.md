# LLM-Powered Prompt Router

A lightweight, containerized prompt routing system that classifies user intent and routes requests to specialized expert personas. Built with Python and Ollama, it demonstrates a practical **two-stage architecture** for AI applications: **classify then respond**.

---

## ✨ Features

- **Intent Classification** – Local LLM (via Ollama) analyzes user input and returns an intent label (`code`, `data`, `writing`, `career`, or `unclear`) with confidence score
- **Four Expert Personas** – Dedicated system prompts for:
  - **Code Expert** – Production-ready code with error handling and idiomatic style
  - **Data Analyst** – Interprets patterns and suggests visualizations
  - **Writing Coach** – Feedback on clarity, structure, and tone (no rewriting)
  - **Career Advisor** – Concrete, actionable career advice
- **Unclear Intent Handling** – Politely asks for clarification when confidence is low
- **JSON Logging** – Every interaction logged in JSON Lines format (`route_log.jsonl`)
- **Dockerized** – Fully containerized with Docker and Docker Compose

---

## 📋 Prerequisites

| Requirement | Purpose |
|-------------|---------|
| [Docker](https://www.docker.com/products/docker-desktop/) | Containerized run |
| [Python 3.10+](https://www.python.org/) | Local development |
| [Ollama](https://ollama.com/) | Local LLM inference |


```markdown
# LLM-Powered Prompt Router

A lightweight, containerized prompt routing system that classifies user intent and routes requests to specialized expert personas. Built with Python and Ollama, it demonstrates a practical two-stage architecture for AI applications: **classify then respond**.

***

## ✨ Features

- **Intent Classification** – A local LLM (via Ollama) analyzes user input and returns an intent label (`code`, `data`, `writing`, `career`, or `unclear`) with a confidence score.
- **Four Expert Personas** – Each intent is handled by a dedicated system prompt:
  - **Code Expert** – Provides production-ready code with error handling and idiomatic style.
  - **Data Analyst** – Interprets data patterns and suggests visualizations.
  - **Writing Coach** – Gives feedback on clarity, structure, and tone (without rewriting).
  - **Career Advisor** – Offers concrete, actionable career advice.
- **Unclear Intent Handling** – When intent is unclear or confidence is low, the system politely asks for clarification.
- **JSON Logging** – Every interaction is logged in JSON Lines format (`route_log.jsonl`), including timestamp, intent, confidence, original message, and response.
- **Dockerized** – Fully containerized with Docker and Docker Compose for consistent execution anywhere.

***

## 📋 Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/) (for containerized run)
- **OR** [Python 3.10+](https://www.python.org/) and [Ollama](https://ollama.com/) for local run
- At least 4 GB of free disk space (for the LLM model)

***

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/prompt-router.git
cd prompt-router
```
## 2. (Optional) Set Up Environment Variables

Copy the example environment file and adjust if needed:

```bash
cp .env.example .env
```
## the defaults are:
```
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.2
```
### Running with Docker
## 1. Build and Start the Container
```
docker-compose up --build
```
## 2. Verify the Logs
```
wc -l route_log.jsonl
```
### 📁 Project Structure
```
promp-router
├── app/
│   ├── __init__.py
│   ├── classifier.py      # Intent classification using Ollama
│   ├── logger.py          # JSON Lines logging
│   ├── main.py            # Entry point with 15 test messages
│   ├── prompts.py         # Four expert system prompts
│   ├── router.py          # Routes to expert and generates response
│   └── utils.py           # JSON parsing with fallback
├── .env.example            # Example environment variables
├── .gitignore
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile              # Docker build instructions
├── README.md               # This file
├── requirements.txt        # Python dependencies (ollama, python-dotenv)
└── route_log.jsonl         # Generated log file (after first run)
```
###  Test Messages
```
1. how do i sort a list of objects in python?
2. explain this sql query for me
3. This paragraph sounds awkward, can you help me fix it?
4. I'm preparing for a job interview, any tips?
5. what's the average of these numbers: 12, 45, 23, 67, 34
6. Help me make this better.
7. I need to write a function that takes a user id and returns their profile, but also i need help with my resume.
8. hey
9. Can you write me a poem about clouds?
10. Rewrite this sentence to be more professional.
11. I'm not sure what to do with my career.
12. what is a pivot table
13. fix this bug pls: for i in range(10) print(i)
14. How do I structure a cover letter?
15. My boss says my writing is too verbose.
```
