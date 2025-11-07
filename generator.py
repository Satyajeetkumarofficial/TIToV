import os
import time
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont

OUT_FOLDER = "outputs"
os.makedirs(OUT_FOLDER, exist_ok=True)

def estimate_time(text):
    return len(text) * 0.2  # fake estimation UI

def text_to_image(text):
    img_path = f"{OUT_FOLDER}/image_{int(time.time())}.png"
    img = Image.new("RGB", (1280, 720), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 350), text, fill="black", font=font)
    img.save(img_path)
    return img_path

def text_to_video(text):
    est = estimate_time(text)

    clips = []
    for i in range(3):
        img_path = text_to_image(text)
        clip = ImageClip(img_path).set_duration(2)
        clips.append(clip)

    video = concatenate_videoclips(clips)
    output = f"{OUT_FOLDER}/video_{int(time.time())}.mp4"
    video.write_videofile(output, fps=24, codec="libx264", audio=False)

    return output
