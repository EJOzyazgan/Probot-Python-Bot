

# Gets bot from game_state
# If you have two of a kind raises for twice the minimum amount
# Otherwise calls
def get_bet(game_state):
    gs = game_state['state']
    p = gs['players']
    me = p[gs['me']]

    if me['cards'][0]['rank'] == me['cards'][1]['rank']:
        return gs['minimumRaiseAmount'] * 2
    elif me['chipsBet'] > 0:
        return gs['callAmount']
    return 0

