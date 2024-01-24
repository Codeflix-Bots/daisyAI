from pyrogram import Client, filters
import requests
from Config import LOG_CHANNEL, GOOGLE_API_KEY, 
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

@Client.on_message(filters.command('ask') & filters.chat(SUPPORT_CHAT_ID)) # support work only added 
async def ai_generate(client, message):
   user_input = message.text.split()[1:]

   if not user_input:
       await message.reply_text("command incomplete provide /ask hello")
       return

   user_input = " ".join(user_input)

   generation_config = {
       "temperature": 0.9,
       "top_p": 1,
       "top_k": 1,
       "max_output_tokens": 2048,
   }

   safety_settings = [
       {
           "category": "HARM_CATEGORY_HARASSMENT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_HATE_SPEECH",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
       {
           "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
           "threshold": "BLOCK_MEDIUM_AND_ABOVE"
       },
   ]

   model = genai.GenerativeModel(
       model_name="gemini-pro",
       generation_config=generation_config,
       safety_settings=safety_settings
   )

   prompt_parts = [user_input]
   response = model.generate_content(prompt_parts)
   await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\n ǫᴜᴇʀʏ ɪs:- {user_input}\n\nResults:\n\n{response.text}")         
   await client.send_message(LOG_CHANNEL, text=f"#ask ʀᴇǫᴜᴇsᴛ ғʀᴏᴍ {message.from_user.mention}\nǫᴜᴇʀʏ ɪs:- {user_input}")
   await s.delete()

@Client.on_message(filters.command("ask"))
async def ai_generate_private(client, message):
  buttons = [[
    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ", url="https://t.me/weebs_support")
  ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await message.reply_text(text=f"ʜᴇʏ {message.from_user.mention}\nᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ɪn sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ  👇 ", reply_markup=reply_markup)
