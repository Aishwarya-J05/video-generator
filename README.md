# 🎬 AI Freedom Fighter Video Generator

Generates a short cinematic video about an Indian freedom fighter using:

* **Google Gemini** — narration script generation
* **gTTS** — text-to-speech audio
* **Pollinations.ai** — AI image generation (no API key required)
* **MoviePy + FFmpeg** — Ken Burns effect and video rendering

---

## ✨ Features

* Generate a concise narration script using Gemini
* Convert narration into realistic speech with gTTS
* Generate AI images automatically or use custom images
* Apply cinematic Ken Burns zoom effects
* Combine images and narration into a professional MP4 video
* Simple end-to-end pipeline

---

## 🎥 Demo

> *"Bhagat Singh, India's fiery revolutionary, sparked a nation's fight for freedom through courage, sacrifice, and unwavering determination..."*

The project creates a cinematic video with animated image transitions synchronized to AI-generated narration.

**Output:** `output/bhagat_singh_intro.mp4`

---

## 🚀 Setup

### Clone the Repository

```bash
git clone https://github.com/Aishwarya-J05/video-generator.git
cd video-generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get a free Gemini API key from:

https://aistudio.google.com

---

## 📖 Usage

### Option 1 — AI-Generated Images (Pollinations.ai)

Set:

```python
IMAGE_PATHS = None
```

and enable the image generation section in `main.py`.

Then run:

```bash
python main.py
```

---

### Option 2 — Use Your Own Images

Place images inside an `images/` folder:

```text
images/
├── bhagat1.jpg
├── bhagat2.png
└── bhagat3.png
```

Update:

```python
IMAGE_PATHS = [
    "images/bhagat1.jpg",
    "images/bhagat2.png",
    "images/bhagat3.png"
]
```

Run:

```bash
python main.py
```

---

## 🔄 Pipeline

```text
Google Gemini
      │
      ▼
Narration Script (~60 words)
      │
      ▼
gTTS
      │
      ▼
Narration Audio (.mp3)
      │
      ▼
Images (Custom or AI Generated)
      │
      ▼
MoviePy
(Ken Burns Effect)
      │
      ▼
Silent Video
      │
      ▼
FFmpeg
(Audio + Video Muxing)
      │
      ▼
Final MP4 Video
```

---

## 🛠 Tech Stack

| Component         | Technology              |
| ----------------- | ----------------------- |
| Script Generation | Google Gemini 2.5 Flash |
| Text-to-Speech    | gTTS                    |
| Image Generation  | Pollinations.ai         |
| Video Processing  | MoviePy v2              |
| Video Rendering   | FFmpeg                  |
| Configuration     | python-dotenv           |

---

## 📂 Project Structure

```text
video-generator/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── images/
└── output/
```

### Description

| File/Folder        | Purpose                            |
| ------------------ | ---------------------------------- |
| `main.py`          | Complete video generation pipeline |
| `requirements.txt` | Python dependencies                |
| `.env`             | API key configuration              |
| `images/`          | Optional custom images             |
| `output/`          | Generated videos and audio         |

---

## 📦 Output

Generated files are saved inside:

```text
output/
├── narration.mp3
├── silent_video.mp4
└── bhagat_singh_intro.mp4
```

---

## 🎯 Use Cases

* Freedom fighter educational videos
* Historical storytelling
* Social media shorts and reels
* AI-generated documentary snippets
* School and college presentations

---

## 📄 License

This project is intended for educational and demonstration purposes.

---

## 👩‍💻 Author

**Aishwarya N. Joshi**

AI/ML Engineer | Computer Vision | NLP | Generative AI

GitHub: https://github.com/Aishwarya-J05

LinkedIn: https://www.linkedin.com/in/aishwaryajoshiaiml

---

Built as a screening assignment for **Sabr Intelligence – Junior AI Developer Role**.
