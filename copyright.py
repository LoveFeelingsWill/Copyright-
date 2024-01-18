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
        text="""Certainly! Here's a description for your Telegram bot designed to protect against copyright messages or unauthorized links:

---

🛡️ **Link Protection Bot**

Guard your group against copyright infringement and unauthorized links with the Link Protection Bot! This intelligent bot is designed to maintain the integrity of your Telegram community by automatically detecting and handling copyright messages or suspicious links.

🚫 **Features:**
- **Copyright Message Detection:** The bot scans messages for potential copyright violations, ensuring a safe environment for your group members.
- **Link Protection:** Unauthorized links are promptly identified and managed to prevent spam, phishing, or any harmful activities.
- **Customizable Settings:** Tailor the bot's behavior to fit your group's unique needs. Adjust sensitivity levels and specify actions for different types of violations.

🤖 **How to Use:**
1. **Invite the Bot:** Add the Link Protection Bot to your group.
2. **Automated Protection:** The bot works silently in the background, identifying and handling copyright messages and unauthorized links.
3. **Configuration (Optional):** Fine-tune the bot's settings to align with your group's moderation preferences.

👮‍♂️ **Disclaimer:** This bot is your group's vigilant guardian, but human oversight is always recommended. Stay compliant with Telegram's terms of service and encourage your members to share content responsibly.

🚀 **Get Started:** [Invite the Link Protection Bot](#)

Secure your Telegram community today with the Link Protection Bot — because a safe and respectful environment is everyone's right!

---

Feel free to customize the description according to the specific features and tone you want to convey.""",
    )

#---------------------------------------------------------------------------
keywords_to_delete = ["www.", "https", "http" , "t.me", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]
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

app.run()
