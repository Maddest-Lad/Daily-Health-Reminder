import asyncio
import discord


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    # This Runs On Bot Startup
    @staticmethod
    async def on_ready():
        print("starting up")

    # Runs Once a Day, Lazy Way (Waits 60*60*24 Seconds)
    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(738558729255125004)  # <- Notification Channel ID

        while not self.is_closed():
            message = "Do The Health Screen: https://www.rit.edu/ready/daily-health-screen"
            await channel.send(message)
            await asyncio.sleep(86400)  # Task Runs Once A Day


client = MyClient()
client.run(open("token.txt", "r").read())  # Token Is Stored Locally
