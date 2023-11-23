from disnake.ext import commands
from core.settings import guild_id, role_id


class BaseCog(commands.Cog):

    def __init__(self, client: commands.InteractionBot):
        self.client: commands.InteractionBot = client

    async def cog_load(self) -> None:
        print(
            f"\033[38;5;38m[LOAD] \033[38;5;67m⌗ Cog: \033[38;5;105m{self.__cog_name__}\033[0;0m has been loaded.\n"
            f"----------------------------------------------"
        )

    def cog_unload(self) -> None:
        print(
            f"\033[38;5;38m[UNLOAD] \033[38;5;67m⌗ Cog \033[38;5;105m{self.__cog_name__}\033[0;0m has been unloaded.\n"
            f"----------------------------------------------"
        )