from project import Guild
from project import Player

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.kick_player(player.name))
print(guild.guild_info())