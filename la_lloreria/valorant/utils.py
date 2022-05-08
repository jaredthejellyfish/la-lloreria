from asyncio import constants
from valorant_player_api import Player

def get_data_points_mmr(user, id):
    user = Player(user, id)
    
    history = user.mmr_history()
    
    return history

def get_elo(user, id):
    user = Player(user, id)
    
    elo = user.mmr_data()['elo']
    
    return {'elo':elo}

def get_data_points_matches(user, id):
    user = Player(user, id)
    
    history = user.match_history()
    
    return history

def get_account_data(user, id):
    user = Player(user, id)
    
    history = user.account_data()
    
    return history