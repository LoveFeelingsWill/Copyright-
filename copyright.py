from pyrogram import Client, filters

#---------------------------------------------------------------------------
API_ID = '6435225'
API_HASH = '4e984ea35f854762dcde906dce426c2d'
BOT_TOKEN = '6914162477:AAF2x0zR-MNYErmkL8OwUau64jUcAXrDjZk' #BOT_TOKEN

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


#-----
@app.on_message(filters.command("start"))
def start_command(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="""Lɪɴᴋ Pʀᴏᴛᴇᴄᴛɪᴏɴ Bᴏᴛ

Gᴜᴀʀᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɢᴀɪɴsᴛ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴғʀɪɴɢᴇᴍᴇɴᴛ ᴀɴᴅ ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪɴᴋs ᴡɪᴛʜ ᴛʜᴇ Lɪɴᴋ Pʀᴏᴛᴇᴄᴛɪᴏɴ Bᴏᴛ! Tʜɪs ɪɴᴛᴇʟʟɪɢᴇɴᴛ ʙᴏᴛ ɪs ᴅᴇsɪɢɴᴇᴅ ᴛᴏ ᴍᴀɪɴᴛᴀɪɴ ᴛʜᴇ ɪɴᴛᴇɢʀɪᴛʏ ᴏғ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ᴄᴏᴍᴍᴜɴɪᴛʏ ʙʏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴅᴇᴛᴇᴄᴛɪɴɢ ᴀɴᴅ ʜᴀɴᴅʟɪɴɢ ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴇssᴀɢᴇs ᴏʀ sᴜsᴘɪᴄɪᴏᴜs ʟɪɴᴋs.

🚫 Fᴇᴀᴛᴜʀᴇs:
- Cᴏᴘʏʀɪɢʜᴛ Mᴇssᴀɢᴇ Dᴇᴛᴇᴄᴛɪᴏɴ: Tʜᴇ ʙᴏᴛ sᴄᴀɴs ᴍᴇssᴀɢᴇs ғᴏʀ ᴘᴏᴛᴇɴᴛɪᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ᴠɪᴏʟᴀᴛɪᴏɴs, ᴇɴsᴜʀɪɴɢ ᴀ sᴀғᴇ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs.
- Lɪɴᴋ Pʀᴏᴛᴇᴄᴛɪᴏɴ: Uɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪɴᴋs ᴀʀᴇ ᴘʀᴏᴍᴘᴛʟʏ ɪᴅᴇɴᴛɪғɪᴇᴅ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴅ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ sᴘᴀᴍ, ᴘʜɪsʜɪɴɢ, ᴏʀ ᴀɴʏ ʜᴀʀᴍғᴜʟ ᴀᴄᴛɪᴠɪᴛɪᴇs.
- Cᴜsᴛᴏᴍɪᴢᴀʙʟᴇ Sᴇᴛᴛɪɴɢs: Tᴀɪʟᴏʀ ᴛʜᴇ ʙᴏᴛ's ʙᴇʜᴀᴠɪᴏʀ ᴛᴏ ғɪᴛ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴜɴɪǫᴜᴇ ɴᴇᴇᴅs. AᴅJᴜsᴛ sᴇɴsɪᴛɪᴠɪᴛʏ ʟᴇᴠᴇʟs ᴀɴᴅ sᴘᴇᴄɪғʏ ᴀᴄᴛɪᴏɴs ғᴏʀ ᴅɪғғᴇʀᴇɴᴛ ᴛʏᴘᴇs ᴏғ ᴠɪᴏʟᴀᴛɪᴏɴs.

🤖 Hᴏᴡ ᴛᴏ Usᴇ:
𝟷. Iɴᴠɪᴛᴇ ᴛʜᴇ Bᴏᴛ: Aᴅᴅ ᴛʜᴇ Lɪɴᴋ Pʀᴏᴛᴇᴄᴛɪᴏɴ Bᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸. Aᴜᴛᴏᴍᴀᴛᴇᴅ Pʀᴏᴛᴇᴄᴛɪᴏɴ: Tʜᴇ ʙᴏᴛ ᴡᴏʀᴋs sɪʟᴇɴᴛʟʏ ɪɴ ᴛʜᴇ ʙᴀᴄᴋɢʀᴏᴜɴᴅ, ɪᴅᴇɴᴛɪғʏɪɴɢ ᴀɴᴅ ʜᴀɴᴅʟɪɴɢ ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴇssᴀɢᴇs ᴀɴᴅ ᴜɴᴀᴜᴛʜᴏʀɪᴢᴇᴅ ʟɪɴᴋs.
𝟹. Cᴏɴғɪɢᴜʀᴀᴛɪᴏɴ (Oᴘᴛɪᴏɴᴀʟ): Fɪɴᴇ-ᴛᴜɴᴇ ᴛʜᴇ ʙᴏᴛ's sᴇᴛᴛɪɴɢs ᴛᴏ ᴀʟɪɢɴ ᴡɪᴛʜ ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ᴘʀᴇғᴇʀᴇɴᴄᴇs.

👮‍♂️ Dɪsᴄʟᴀɪᴍᴇʀ: Tʜɪs ʙᴏᴛ ɪs ʏᴏᴜʀ ɢʀᴏᴜᴘ's ᴠɪɢɪʟᴀɴᴛ ɢᴜᴀʀᴅɪᴀɴ, ʙᴜᴛ ʜᴜᴍᴀɴ ᴏᴠᴇʀsɪɢʜᴛ ɪs ᴀʟᴡᴀʏs ʀᴇᴄᴏᴍᴍᴇɴᴅᴇᴅ. Sᴛᴀʏ ᴄᴏᴍᴘʟɪᴀɴᴛ ᴡɪᴛʜ Tᴇʟᴇɢʀᴀᴍ's ᴛᴇʀᴍs ᴏғ sᴇʀᴠɪᴄᴇ ᴀɴᴅ ᴇɴᴄᴏᴜʀᴀɢᴇ ʏᴏᴜʀ ᴍᴇᴍʙᴇʀs ᴛᴏ sʜᴀʀᴇ ᴄᴏɴᴛᴇɴᴛ ʀᴇsᴘᴏɴsɪʙʟʏ.

🚀 Gᴇᴛ Sᴛᴀʀᴛᴇᴅ: Iɴᴠɪᴛᴇ ᴛʜᴇ Lɪɴᴋ Pʀᴏᴛᴇᴄᴛɪᴏɴ Bᴏᴛ

Sᴇᴄᴜʀᴇ ʏᴏᴜʀ Tᴇʟᴇɢʀᴀᴍ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴛᴏᴅᴀʏ ᴡɪᴛʜ ᴛʜᴇ Lɪɴᴋ Pʀᴏᴛᴇᴄᴛɪᴏɴ Bᴏᴛ — ʙᴇᴄᴀᴜsᴇ ᴀ sᴀғᴇ ᴀɴᴅ ʀᴇsᴘᴇᴄᴛғᴜʟ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ ɪs ᴇᴠᴇʀʏᴏɴᴇ's ʀɪɢʜᴛ!

-

Fᴇᴇʟ ғʀᴇᴇ ᴛᴏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜᴇ ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴛʜᴇ sᴘᴇᴄɪғɪᴄ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴛᴏɴᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴᴠᴇʏ. """,
    )

#---------------------------------------------------------------------------
keywords_to_delete = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(keyword in message.text for keyword in keywords_to_delete) and len(message.text.split()) > 20:
        await message.delete()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@app.on_edited_message(filters.group & filters.text & ~filters.me)
async def delete_edited_links(client, edited_message):
    if any(keyword in edited_message.text for keyword in keywords_to_delete) and len(edited_message.text.split()) > 20:
        await edited_message.delete()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    if len(message.text.split()) >= 20:
        await message.delete()
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & filters.text & ~filters.me)
async def delete_edited_long_messages(client, edited_message):
    if len(edited_message.text.split()) >= 20:
        await edited_message.delete()


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
async def delete_long_messages(message):
    if len(message.text.split()) > 20:
        await message.delete()

@app.on_message(filters.group & filters.text & ~filters.me)
async def handle_messages(client, message):
    await delete_long_messages(message)

@app.on_edited_message(filters.group & filters.text & ~filters.me)
async def handle_edited_messages(client, edited_message):
    await delete_long_messages(edited_message)

#-----------
#-----------


app.run()
