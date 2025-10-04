#!/usr/bin/env python3
import asyncio

from poke_env import Player
from poke_env import RandomPlayer
from poke_env.data import GenData
import sys
import random
from teams import TEAMS, RandomTeamBuilder, team
from poke_env.ps_client import AccountConfiguration 
# import mctsAgent

sys.path.append("../src")
class YourFirstAgent(Player):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.gen_data = GenData.from_gen(9)
    def choose_move(self, battle):
        for move in battle.available_moves:
            print("TYPE OF MOVE HERE: ", [type(k) for k in move], "\n")
            if move.base_power > 90:
                # A powerful move! Let's use it
                return self.create_order(move)

        # No available move? Let's switch then!
        for switch in battle.available_switches:
            if switch.current_hp_fraction > battle.active_pokemon.current_hp_fraction:
                # This other pokemon has more HP left... Let's switch it in?
                return self.create_order(switch)

        # Not sure what to do?
        return self.choose_random_move(battle)

battle_format = "gen9vgc2025regh"
team_ids = list(range(len(TEAMS[battle_format[-4:]])))
# random.Random(0).shuffle(team_ids)
# team1 = RandomTeamBuilder(team_ids[:1])
# team2 = RandomTeamBuilder(team_ids[1:2])
# print(team1)
# print(team2)
# RandomTeamBuilder(team_ids, battle_format)
firstAgent = YourFirstAgent(account_configuration=AccountConfiguration("wduhwiduhwi", "kyskyskys"), battle_format="gen9balancedhackmons", team = team)
second_player = RandomPlayer(account_configuration=AccountConfiguration("sduhiduhwidhine", "djiwjdiwjdoijwdojo"), battle_format="gen9balancedhackmons", team = team)
#for the project we are concerned with gen 9 vgc 2025 reg i format
#for testing purposes, we are going to use regulation G since someone already has team selection for that
async def battle():
    await firstAgent.battle_against(second_player, n_battles=1)
asyncio.run(battle())
print(
    f"Player {firstAgent.username} won {firstAgent.n_won_battles} out of {firstAgent.n_finished_battles} played"
)
print(
    f"Player {second_player.username} won {second_player.n_won_battles} out of {second_player.n_finished_battles} played"
)

# Looping over battles

for battle_tag, battle in firstAgent.battles.items():
    print(battle_tag, battle.won)


