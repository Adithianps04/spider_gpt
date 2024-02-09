import logging
from pyrogram import Client, filters
import g4f
import nest_asyncio

# Apply nest_asyncio
nest_asyncio.apply()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Your G4F, Telegram bot token, api_id, and api_hash
TELEGRAM_BOT_TOKEN = '6950907552:AAEx6O4WOx9G9VUYoXyqhxI3VVsDU-NZqBk'
API_ID = '22923523'
API_HASH = 'd52c7824d0e66903a0724b800a16ce2c'
g4f_model = g4f.models.gpt_35_turbo
g4f_provider = g4f.Provider.Bing

# Initialize Pyrogram client
app = Client(
    "my_bot",
    bot_token=TELEGRAM_BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)

# Define the /start command handler
@app.on_message(filters.command("start"))
async def start_command(_, message):
    await message.reply_text("Hi I am a spider gpt  made by  @AI_spide. Ask me Anything .")

# Define the message handler
@app.on_message(filters.text)
async def echo_message(_, message):
    if not message.command:
        user_input = message.text

        # Use G4F to generate a response
        response = g4f.ChatCompletion.create(
            model=g4f_model,
            provider=g4f_provider,
            messages=[{"role": "user", "content": user_input}],
        )

        # Check if the G4F-generated response is valid
        if response and response[0]:
            try:
                # Join the characters into a single string
                response_text = ''.join(response)
                
                # Send the G4F-generated response to the user
                await message.reply_text(response_text)
            except Exception as e:
                logging.error(f"Error sending message: {e}")
        else:
            logging.warning("G4F response is empty or invalid.")

# Start the Pyrogram client
app.run()
