from dotenv import dotenv_values

config = dotenv_values()

commands_ = {}

events = {
    "extensions.events.on_ready",
    "extensions.events.on_member_join"
}

guild_id = 972517659285540935
role_id = 978236172738392134
