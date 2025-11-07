import os, time, asyncio
from pyrogram import Client, filters
from fastapi import FastAPI
from generator import text_to_image, text_to_video, estimate_time

app = FastAPI()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = Client("TextToVideoBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.get("/")
def home():
    return {"status": "running", "bot": "TextToVideoBot"}

@bot.on_message(filters.command("start"))
async def start(_, m):
    await m.reply_text("👋 Namaste! Mujhe text bhejo, main uska image/video bana dunga.\n\nCommands:\n📸 /img <text>\n🎬 /video <text>")

@bot.on_message(filters.command("img"))
async def make_img(_, m):
    if len(m.command) < 2:
        return await m.reply("Usage: /img <text>")
    prompt = " ".join(m.command[1:])
    wait = estimate_time()
    msg = await m.reply_text(f"🧠 Processing your image... (ETA: {wait}s)")
    img = text_to_image(prompt)
    await asyncio.sleep(wait)
    await msg.edit_text("✅ Done!")
    await m.reply_photo(photo=img, caption=f"🖼 Prompt: {prompt}")
    os.remove(img)

@bot.on_message(filters.command("video"))
async def make_vid(_, m):
    if len(m.command) < 2:
        return await m.reply("Usage: /video <text>")
    prompt = " ".join(m.command[1:])
    wait = estimate_time() + 10
    msg = await m.reply_text(f"🎬 Generating video... (ETA: {wait}s)")
    vid = text_to_video(prompt)
    await asyncio.sleep(wait)
    await msg.edit_text("✅ Video ready!")
    await m.reply_video(video=vid, caption=f"🎬 Prompt: {prompt}")
    os.remove(vid)

if __name__ == "__main__":
    import threading
    threading.Thread(target=lambda: bot.run()).start()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
