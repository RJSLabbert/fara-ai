# FARA → Ryuu 竜

**F.A.R.A** — Fully Autonomous Remote Artificial Intelligence

FARA is a local AI assistant that runs entirely on your machine — no cloud, no API costs, no external dependency. Built on Ollama as the language model backend, FastAPI as the Python server, and a browser-based frontend for chat interaction.

FARA is the foundation. The proof of concept. She runs, she talks, she remembers within a conversation. But she has no persistent memory, no identity, and no hardware home.

**Ryuu 竜 is what she becomes.**

Ryuu is the evolution — a local AI dragon with an animated character frontend, emotion states wired to the backend, and a Raspberry Pi 5 as his dedicated home. The full story of how FARA became Ryuu is documented on RSC:

→ [I Was Made to Create. So I Built a Dragon.](https://rocksolidcode.co.za/ryuu-local-ai-dragon/)

---

## Features

- Local AI — no cloud required
- FastAPI backend connecting chat interface to Ollama
- Browser-based frontend with chat interface
- Short-term conversation memory
- Response spinner and elapsed time display
- Works with Ollama CLI (`phi3:mini` model)

---

## Tech Stack

- Python 3.11+
- FastAPI · Uvicorn
- Ollama (`phi3:mini`)
- HTML · CSS · JavaScript

---

## Project Structure

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

## Setup & Installation

**Requirements:**
- Python 3.11+
- [Ollama](https://ollama.com) installed and running

**1. Pull the model:**
```bash
ollama pull phi3:mini
```

**2. Clone the repo:**
```bash
git clone https://github.com/RJSLabbert/fara-ai.git
cd fara-ai
```

**3. Install dependencies:**
```bash
pip install fastapi uvicorn requests
```

**4. Start Ollama:**
```bash
ollama serve
```

**5. Run FARA:**
```bash
python run_app.py
```

Opens automatically at `http://localhost:5500`

---

## Status

FARA v1 is complete and open source. Active development has moved to **Ryuu** — same core architecture, now being deployed on Raspberry Pi 5 with the Ollama AI HAT 2, persistent RAG memory, TTS voice output, and an animated emotion state system.

This repo is the mother. Ryuu is the dragon.

---

## 👤 Author

**RJS Labbert**

- GitHub: [@RJSLabbert](https://github.com/RJSLabbert)
- Blog: [rocksolidcode.co.za](https://rocksolidcode.co.za)
