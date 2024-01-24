from pyrogram import Client, filters
from config import LOG_CHANNEL

@Client.on_message(filters.command("feedback"))
async def feedback(client, message):
  await message.reply_text("/fp - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴘᴜʙʟɪᴠᴀʟʟʏ\n /fa - ᴛᴏ sᴇɴᴅ ʏᴏᴜʀ ғᴇᴇᴅʙᴀᴄᴋ ʙʏ ᴀɴᴏɴʏᴍᴏᴜsʟʏ")

@Client.on_message(filters.command("fp"))
async def feedback_p(client, message):
  fp = message.text.split(" ", 1)[1]
  await message.reply_text(f"ʜɪ {message.from_user.mention},\n ᴛʜᴀɴᴋ ᴜ ғᴏʀ ᴛʜᴇ ғᴇᴇᴅʙᴀᴄᴋ")

  await client.send_message(LOG_CHANNEL, text=f"#ɴᴇᴡ_ғᴇᴇᴅʙᴀᴄᴋ_ᴘᴜʙʟɪᴄ\nғᴇᴇᴅʙᴀᴄᴋ ғʀᴏᴍ {message.from_user.mention}\n ᴛʜᴇ ᴛᴇxᴛ ɪs : <code>{fp}</code>")

@Client.on_message(filters.command("fa"))
async def feedback_a(client, message):
  fa = message.text.split(" ", 1)[1]
  await message.reply_text(f"ʜɪ {message.from_user.mention},\n ᴛʜᴀɴᴋ ᴜ ғᴏʀ ᴛʜᴇ ғᴇᴇᴅʙᴀᴄᴋ")

  await client.send_message(LOG_CHANNEL, text=f"#ɴᴇᴡ_ғᴇᴇᴅʙᴀᴄᴋ_ᴀɴᴏɴʏᴍᴏᴜsʟʏ\n\nᴛʜᴇ ᴛᴇxᴛ ɪs : <code>{fa}</code>")
