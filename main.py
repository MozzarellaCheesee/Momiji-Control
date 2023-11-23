import disnake
from disnake.ext import commands
from core.settings import config
from tools.system_utils import load_extensions

client = commands.InteractionBot(intents=disnake.Intents.all())


async def main():
    load_extensions(client)
    await client.start(config["MOMIJI_CONTROL_TOKEN"])


if __name__ == "__main__":
    client.loop.run_until_complete(main())
