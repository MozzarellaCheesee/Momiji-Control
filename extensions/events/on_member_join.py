import disnake
from disnake.ext import commands

from core.settings import guild_id, role_id
from core.cog import BaseCog


class OnMemberJoin(BaseCog):

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):
        standart_role = self.client.get_guild(guild_id).get_role(role_id)
        await member.add_roles(standart_role)


def setup(client: commands.InteractionBot):
    client.add_cog(OnMemberJoin(client))
