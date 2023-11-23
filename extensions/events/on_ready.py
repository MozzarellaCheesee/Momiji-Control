import disnake
from disnake.ext import commands

from core.cog import BaseCog
from core.settings import guild_id

import logging


class OnReady(BaseCog):

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Загрузка клиента")

        guild = self.client.get_guild(guild_id)

        await self.client.change_presence(
            status=disnake.Status.online, activity=disnake.Activity(name=f"за {len(guild.members)} ёкаями",
                                                                  type=disnake.ActivityType.watching))

        print(
            f"\033[38;5;38m[CLIENT] \033[38;5;67m⌗ \033[38;5;105m{self.client.user}\033[0;0m is worked stable.\n"
            f"----------------------------------------------"
        )
        logging.info("Бот был запущен")


def setup(client: commands.InteractionBot):
    client.add_cog(OnReady(client))
