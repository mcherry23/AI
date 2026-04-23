import discord

TOKEN = "YOUR_BOT_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_response(message: str):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! 👋"

    elif "how are you" in message:
        return "I'm doing great!"

    elif "price" in message:
        return "Prices start at $9.99."

    elif "help" in message:
        return "I can respond to greetings, help, and pricing questions."

    else:
        return "I didn't understand that."

@client.event
async def on_ready():
    print(f"Bot is online as {client.user}")

@client.event
async def on_message(message):
    # prevent bot from replying to itself
    if message.author == client.user:
        return

    response = get_response(message.content)
    await message.channel.send(response)

client.run(TOKEN)
