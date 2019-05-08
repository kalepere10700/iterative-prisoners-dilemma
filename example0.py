####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
def move(my_history, their_history, my_score, their_score):
    while their_history[-1] == "c":
        return 'c'
    return "b"