import openai
from pyrogram import Client, filters
from pyrogram.types import Message # Import Message type

# Configuration (Move sensitive data to environment variables or a separate config file)
API_ID = 1623073  
API_HASH = "a6f2f0a7b2022f8ca7717d9101c5ff5c" 
BOT_TOKEN = "7078609429:AAFHgMvPwq4RCa_84xoZjiMEi2jELsbtI3Y"
OPENAI_API_KEY = "sk-proj-b3sDYwSPgJ7VHKjwNOumT3BlbkFJi4ql9AiMDl8IF9EMQ6bt" 
OPENAI_MODEL = "text-davinci-003"

# Initialize OpenAI client
openai.api_key = OPENAI_API_KEY

# Create Pyrogram Client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
    # Remove the plugins parameter
)

# Define the message handler
@app.on_message(filters.command(["command_name"]))  # Example command
async def handle_message(client: Client, message: Message):
    prompt = message.text.strip()

    if prompt:
        try:
            response = await generate_response(prompt)
            await message.reply(hey)  # Use message.reply instead of message.reply_text
        except openai.OpenAIError as e:
            await message.reply(f"OpenAI Error: {e}")  

# Function to generate response using OpenAI (async for efficiency)
async def generate_response(prompt: str, max_tokens: int = 150) -> str:
    completion = await openai.Completion.acreate(
        engine=OPENAI_MODEL,
        prompt=prompt,
        max_tokens=max_tokens
    )
    return completion.choices[0].text.strip()

# Start the bot
if __name__ == "__main__":
    app.run()
