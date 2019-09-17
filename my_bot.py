

# This is a very simple example showing how to use the game data
# It is highly recomended that you update this logic with your own
# 
# This method is the entry point for the bot, but you may add however
# many methods you would like. If chsnging the name of this method
# make sure to update it on the server (app.py) import as well.
#
# Gets bot from game_state
# If you have two of a kind raises for twice the minimum amount
# Otherwise calls
def get_bet(game_state):
    gs = game_state['state']
    p = gs['players']
    me = p[gs['me']]

    rank = 0

    if me['cards'][0]['rank'] == '8':
        rank += 8
    elif me['cards'][0]['rank'] == '9':
        rank += 9
    elif me['cards'][0]['rank'] == '10':
        rank += 10
    elif me['cards'][0]['rank'] == 'J':
        rank += 11
    elif me['cards'][0]['rank'] == 'Q':
        rank += 12
    elif me['cards'][0]['rank'] == 'K':
        rank += 13
    elif me['cards'][0]['rank'] == 'A':
        rank += 14

    if me['cards'][1]['rank'] == '8':
        rank += 8
    elif me['cards'][1]['rank'] == '9':
        rank += 9
    elif me['cards'][1]['rank'] == '10':
        rank += 10
    elif me['cards'][1]['rank'] == 'J':
        rank += 11
    elif me['cards'][1]['rank'] == 'Q':
        rank += 12
    elif me['cards'][1]['rank'] == 'K':
        rank += 13
    elif me['cards'][1]['rank'] == 'A':
        rank += 14

    if rank >= 24 and me['chips'] >= gs['minimumRaiseAmount'] * 2:
        return gs['minimumRaiseAmount'] * 1.5
    elif rank >= 20 and me['chips'] >= gs['minimumRaiseAmount'] * 1.5:
        return gs['minimumRaiseAmount'] * 1.5
    elif rank >= 24 and me['chips'] >= gs['minimumRaiseAmount']:
        return gs['minimumRaiseAmount']
    return gs['callAmount']
