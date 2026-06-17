# 🎬 AI Video Generator

Generates a short cinematic video about an Indian freedom fighter using:
- **Google Gemini** — narration script generation
- **gTTS** — text-to-speech audio
- **Pollinations.ai** — AI image generation (no API key needed)
- **MoviePy + FFmpeg** — Ken Burns effect + audio/video muxing

## Demo

> *"Bhagat Singh, India's fiery revolutionary, sparked a nation's fight for freedom..."*

Ken Burns zoom effect across 3 AI-generated or custom images, synced to narrated audio. Output: `output/bhagat_singh_intro.mp4`

---

## Setup

```bash
git clone https://github.com/Aishwarya-J05/video-generator.git
cd video-generator
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

Create `.env`:
