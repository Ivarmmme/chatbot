from pyrogram import Client, filters
import openai

# Set your credentials (replace with your actual values)
api_id = '1623073'
api_hash = 'a6f2f0a7b2022f8ca7717d9101c5ff5c'
bot_token = '7078609429:AAFHgMvPwq4RCa_84xoZjiMEi2jELsbtI3Y'
openai_api_key = 'sk-proj-b3sDYwSPgJ7VHKjwNOumT3BlbkFJi4ql9AiMDl8IF9EMQ6bt'

# Initialize OpenAI
openai.api_key = openai_api_key

# Create Pyrogram Client with bot token
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Define the message handler
@app.on_message(filters.text & filters.command)
async def handle_message(client, message):
    prompt = message.text
    response = await generate_response(prompt)
    await message.reply_text(response)

# Function to generate response using OpenAI
async def generate_response(prompt):
    try:
        completion = openai.Completion.create(
            engine="text-davinci-003",  # or the latest model
            prompt=prompt,
            max_tokens=150  # Adjust as needed
        )
        return completion.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main function to run the bot
if __name__ == "__main__":
    app.run() 
