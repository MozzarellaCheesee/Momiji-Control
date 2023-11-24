import disnake
from disnake.ext import commands

from core.cog import BaseCog
from tools.ui.buttons.info import InfoButtons


class Developer(BaseCog):

    @commands.is_owner()
    @commands.command(name="инфо")
    async def info(self, ctx: commands.Context):
        await ctx.message.delete()
        await ctx.send(
            embed=disnake.Embed(
                title="Приветствуем тебя на нашем сервере поддержки <a:hello:1177626468545736785>",
                description="Рады видеть тебя на сервере комьюнити нашего бота <a:momiji_dance:1177628064474206319>"
                            "\nПо кнопкам ниже ты можешь ознакомиться с информацией о нашем комьюнити и проекте"
            ).set_image(
                url="https://cdn.discordapp.com/attachments/1123682099233300602/1177627495256838224/"
                    "Community_banner.jpg?ex=65733212&is=6560bd12&hm=98ebf336a1353be2ff7849ff2a9a4f9a"
                    "beead138abeca3d41ccb09beb8d02935&"
            ), view=InfoButtons()
        )


def setup(client: commands.InteractionBot):
    client.add_cog(Developer(client))
