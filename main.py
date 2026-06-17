import os
import subprocess
import numpy as np
import imageio_ffmpeg
from pathlib import Path
from gtts import gTTS
from google import genai
from moviepy import VideoClip, AudioFileClip, concatenate_videoclips
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

IMAGE_PATHS = [
    Path("images/bhagat1.jpg"),
    Path("images/bhagat2.png"),
    Path("images/bhagat3.png"),
]

def generate_script() -> str:
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="""Write a powerful 10-second video narration script about Bhagat Singh.
Requirements:
- Exactly 3 sentences
- Punchy, cinematic tone
- Cover: who he was, what he did, why he matters
- No more than 60 words total
Return ONLY the narration text, nothing else."""
    )
    script = response.text.strip()
    print(f"[Script]\n{script}\n")
    return script

def generate_audio(script: str) -> Path:
    audio_path = OUTPUT_DIR / "narration.mp3"
    tts = gTTS(text=script, lang="en", slow=False)
    tts.save(str(audio_path))
    print(f"[Audio] Saved → {audio_path}")
    return audio_path

def make_ken_burns_clip(image_path: Path, duration: float, zoom_start=1.0, zoom_end=1.3) -> VideoClip:
    img = np.array(Image.open(image_path).convert("RGB").resize((1280, 720)))
    h, w = img.shape[:2]

    def make_frame(t):
        progress = t / duration
        zoom = zoom_start + (zoom_end - zoom_start) * progress
        new_w = int(w / zoom)
        new_h = int(h / zoom)
        x1 = (w - new_w) // 2
        y1 = (h - new_h) // 2
        cropped = img[y1:y1+new_h, x1:x1+new_w]
        return np.array(Image.fromarray(cropped).resize((w, h)))

    return VideoClip(make_frame, duration=duration)

def assemble_video(image_paths: list, audio_path: Path) -> Path:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    audio = AudioFileClip(str(audio_path))
    total_duration = audio.duration
    duration_each = total_duration / len(image_paths)

    zoom_configs = [(1.0, 1.3), (1.3, 1.0), (1.0, 1.3)]
    clips = [
        make_ken_burns_clip(p, duration_each, *zoom_configs[i % len(zoom_configs)])
        for i, p in enumerate(image_paths)
    ]

    video = concatenate_videoclips(clips, method="compose")

    # Write silent video first
    silent_path = OUTPUT_DIR / "silent.mp4"
    video.write_videofile(str(silent_path), fps=24, codec="libx264", logger=None)

    # Mux audio via ffmpeg directly — bypasses MoviePy v2 audio bug
    out = OUTPUT_DIR / "bhagat_singh_intro.mp4"
    subprocess.run([
        ffmpeg, "-y",
        "-i", str(silent_path),
        "-i", str(audio_path),
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "44100",        # force standard sample rate
        "-ac", "2",            # force stereo
        "-movflags", "+faststart",  # web-compatible MP4
        "-shortest",
        str(out)
    ], check=True)

    silent_path.unlink()
    print(f"\n[Video] Saved → {out}")
    return out

if __name__ == "__main__":
    print("=== Bhagat Singh AI Video Generator ===\n")
    script = generate_script()
    audio_path = generate_audio(script)
    assemble_video(IMAGE_PATHS, audio_path)