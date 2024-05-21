from pyrogram import client, filters
import openai

# Configuration (Move to separate file or environment variables in production)
API_ID = 1623073
API_HASH = "a6f2f0a7b2022f8ca7717d9101c5ff5c"
BOT_TOKEN = "7078609429:AAFHgMvPwq4RCa_84xoZjiMEi2jELsbtI3Y"
OPENAI_API_KEY = "sk-proj-b3sDYwSPgJ7VHKjwNOumT3BlbkFJi4ql9AiMDl8IF9EMQ6bt"  # Be sure to keep your key secret
OPENAI_MODEL = "text-davinci-003"  # Set your preferred model

# Initialize clients
openai.api_key = OPENAI_API_KEY
app = client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Message handler
@app.on_message(filters.text & filters.command)
async def handle_message(client, message):
    prompt = message.text.strip()

    if prompt:
        try:
            response = await generate_response(prompt)
            await message.reply_text(response)
        except openai.OpenAIError as e:
            await message.reply_text(f"OpenAI Error: {e}")

# OpenAI response generation (Note async for better concurrency)
async def generate_response(prompt, max_tokens=150):
    completion = await openai.Completion.acreate(  
        engine=OPENAI_MODEL,
        prompt=prompt,
        max_tokens=max_tokens
    )
    return completion.choices[0].text.strip()

# Run the bot
if __name__ == "__main__":
    app.run()
    
