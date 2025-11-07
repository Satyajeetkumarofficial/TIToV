import time, random
from moviepy.editor import TextClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont

def text_to_image(prompt):
    img = Image.new("RGB", (720, 480), (245, 245, 245))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((30, 200), prompt, fill=(0, 0, 0), font=font)
    filename = f"generated_{int(time.time())}.png"
    img.save(filename)
    return filename

def text_to_video(prompt):
    clips = []
    for i in range(3):
        txt = TextClip(f"{prompt} - scene {i+1}", fontsize=50, color='white', bg_color='black', size=(720,480))
        clips.append(txt.set_duration(2))
    final = concatenate_videoclips(clips)
    out_file = f"video_{int(time.time())}.mp4"
    final.write_videofile(out_file, fps=24)
    return out_file

def estimate_time():
    return random.randint(10, 30)
