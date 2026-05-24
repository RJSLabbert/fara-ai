# FARA → Ryuu 竜 🐉

**F.A.R.A**  Fully Autonomous Remote Artificial Intelligence → **Ryuu 竜** Local AI Dragon

FARA is a fully local AI assistant running on your own machine — no cloud, no API costs, no external dependency. She uses **Ollama** as the language model backend, a **FastAPI** Python server, and a **browser-based frontend** for chat interaction.

FARA is the foundation. Ryuu is what she becomes.

→ [Read the full story on RSC](https://rocksolidcode.co.za/ryuu-local-ai-dragon/)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-backend-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Ollama](https://img.shields.io/badge/Ollama-local_AI-black?logo=ollama&logoColor=white)](https://ollama.com)
[![Status](https://img.shields.io/badge/Status-Active_Development-orange?style=flat-square)](https://github.com/RJSLabbert/fara-ai)

---

## 🐉 Why I built this

I wanted to build my own AI. Not use someone else's API, not pay for cloud tokens. Actually build something that runs entirely on my own hardware. FARA was the proof of concept. She runs, she talks, she thinks locally. But she had no memory, no identity, no home.

Ryuu is the answer to that. A local AI dragon with an animated character, emotion states wired to the backend, and a Raspberry Pi 5 as his dedicated hardware home. Built from curiosity, stubbornness, and a YouTube video that changed everything.

---

## ✨ Features

### 🖥️ Local AI Core
- Runs entirely on your machine, no cloud required
- FastAPI backend connecting chat interface to Ollama
- Works with Ollama CLI (`phi3:mini` model)

### 💬 Chat Interface
- Browser-based frontend with clean chat UI
- Response spinner and elapsed time display
- Short-term conversation memory within session

### 🐉 Ryuu Evolution (In Progress)
- Animated character frontend with emotion states
- Emotion states wired to FastAPI backend in real time
- Raspberry Pi 5 deployment with Ollama AI HAT 2
- RAG persistent memory system (in progress)
- TTS voice output matching emotion state (in progress)

---

## 🛠️ Tech Stack

- Python 3.11+
- FastAPI · Uvicorn
- Ollama (`phi3:mini`)
- HTML · CSS · JavaScript
- Raspberry Pi 5 · AI HAT 2 (Ryuu phase)

---

## 🚀 Quick Setup

1. Install [Ollama](https://ollama.com) and pull the model:
```bash
ollama pull phi3:mini
```
2. Clone the repo:
```bash
git clone https://github.com/RJSLabbert/fara-ai.git
cd fara-ai
```
3. Install dependencies:
```bash
pip install fastapi uvicorn requests
```
4. Start Ollama:
```bash
ollama serve
```
5. Run FARA:
```bash
python run_app.py
```
Opens automatically at `http://localhost:5500`

---

## 📁 Project Structure

```
fara-ai/
├── backend/
│   └── main.py          # FastAPI server — connects chat to Ollama
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js        # Chat interface
├── run_app.py           # Launches backend + frontend together
└── README.md
```

---

## 📋 Version History

| Version | Status | Notes |
|---|---|---|
| FARA v1 | ✅ Complete | Local AI, FastAPI backend, browser chat |
| Ryuu v1 | 🔄 In Progress | Character frontend, emotion states, Pi 5 deployment |
| Ryuu v2 | 📋 Planned | RAG memory, TTS voice, full hardware integration |

---

## 👤 Author

**RJ SLabbert**

- GitHub: [@RJSLabbert](https://github.com/RJSLabbert)
- Blog: [rocksolidcode.co.za](https://rocksolidcode.co.za)

---
