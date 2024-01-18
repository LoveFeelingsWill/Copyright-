from pyrogram import Client, filters

#---------------------------------------------------------------------------
API_ID = '6435225'
API_HASH = '4e984ea35f854762dcde906dce426c2d'
BOT_TOKEN = '6914162477:AAE0zSnpICIB7gkMtksj17f7MBhIE9Zzo2A' #BOT_TOKEN

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


#-----
@Client.on_message(filters.command("start"))
def start_command(client, message):
    client.send_message(
        chat_id=message.chat.id,
        text="Hello! I am your bot. Welcome to the chat!",
    )

#---------------------------------------------------------------------------
keywords_to_delete = ["www.", "https", "http" , "t.me", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
@Client.on_message(filters.group & filters.text & ~filters.me)
async def delete_links(client, message):
    if any(keyword in message.text for keyword in keywords_to_delete) and len(message.text.split()) > 20:
        await message.delete()

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@Client.on_edited_message(filters.group & filters.text & ~filters.me)
async def delete_edited_links(client, edited_message):
    if any(keyword in edited_message.text for keyword in keywords_to_delete) and len(edited_message.text.split()) > 20:
        await edited_message.delete()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

@Client.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    if len(message.text.split()) >= 20:
        await message.delete()
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
@Client.on_edited_message(filters.group & filters.text & ~filters.me)
async def delete_edited_long_messages(client, edited_message):
    if len(edited_message.text.split()) >= 20:
        await edited_message.delete()


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

Client.run()
