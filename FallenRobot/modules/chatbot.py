from pyrogram import filters, Client
import requests

API_ID = 22370845   # Your API_ID from telegram.org
API_HASH = "32b5d61ace7a682fd093c41c7eacd69f"        # Your API_HASH from telegram.org
BOT_TOKEN = "6674687335:AAE4GB0oS-581jYS9ZZFSzg0vlYi275I_jw"       # Your Bot Token from BOT FATHER
BOT_ID = int(BOT_TOKEN.split(':')[0])

app = Client("eva", API_ID, API_HASH, bot_token=BOT_TOKEN)

BLUE_URL = "https://blue-api.vercel.app/chatbot1"
BLUE_AI = "BLUE-AI-black-22130744-2067727121-alice-2067727121-456"   # Get you Blue-AI token from @HackiaBot by sending /token


def get_response(user_id, query):
    params = {
        "user_id": user_id,     # Replace with the user ID you want to use
        "query": query,         # Replace with your query
        "BOT_ID": BOT_ID        # Your Bot's ID
    }
    headers = {
        "api_key": BLUE_AI      # Replace with your API key
    }
    response = requests.get(BLUE_URL, params=params, headers=headers)
    return response.json()


@app.on_message(filters.reply)
async def chatbot_handler(client, msg):
    if msg.reply_to_message.from_user.id != BOT_ID:
        return
    user_id = msg.from_user.id
    query = msg.text
    result = get_response(user_id, query)
    if result["status"] == 200:
        text = result["result"]["text"]
        await msg.reply_text(text)
    else:
        await msg.reply_text(result["msg"])


print("started!")
app.run()
