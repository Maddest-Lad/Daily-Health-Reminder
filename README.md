# Daily-Health-Reminder
Sends a message once  a day reminding students to fill out the RIT health screen

# Setup
Add the bot to the Discord server in question using this link (it only needs send message permissions):
https://discord.com/api/oauth2/authorize?client_id=738557873801527357&permissions=2048&scope=bot

Then create some sort of channel for the bot to send messages in and yell at Sam to hardcode that channel id into the bot.

Finally, yell at Sam some more to start the bot up at the wanted reminder time
(I didn't want to use the scheduler cause I'm lazy so it just waits 60 * 60 * 24 seconds)

