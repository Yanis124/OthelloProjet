#display the data of the tournament in a graphs

import matplotlib.pyplot as plt

dict_ai = {0: 'easy', 1: 'normal', 2: 'hard'}
dict_ai_color = {0: '#1f77b4', 1: '#2ca02c', 2: '#ff7f0e'}
draw_color = '#808080'

def get_wins_result_tournament(file_path, first_ai, second_ai):
    """read the result of the tournament and return the number of matches, wins and draws for each AI"""
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_matches = 0
    total_wins_first_ai = 0
    total_wins_second_ai = 0
    total_draws = 0

    for line in lines:
        parts = line.strip().strip('()').split(', ')
        result = parts[0]
        
        if result == str(first_ai):
            total_wins_first_ai += 1
        elif result == str(second_ai):
            total_wins_second_ai += 1
        elif result == 'None':
            total_draws += 1
        
        total_matches += 1
        
    return (total_matches, total_wins_first_ai, total_wins_second_ai, total_draws)
        
def draw_circle_graph(first_ai, second_ai, total_matches, total_wins_first_ai, total_wins_second_ai, total_draws):
    """draw a circle graph with the percentage of wins and draws for each AI"""

    win_percentage_first_ai = (total_wins_first_ai / total_matches) * 100
    win_percentage_second_ai = (total_wins_second_ai / total_matches) * 100
    draw_percentage = (total_draws / total_matches) * 100

    # Plot the pie chart
    labels = [dict_ai[first_ai], dict_ai[second_ai], 'Draws']
    sizes = [win_percentage_first_ai, win_percentage_second_ai, draw_percentage]
    colors = [dict_ai_color[first_ai], dict_ai_color[second_ai], draw_color ]
    explode = (0.1, 0, 0)  
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  
    plt.title('AI Wins Percentage'+ '\n' + dict_ai[first_ai] + ' vs ' + dict_ai[second_ai] + ' - ' + str(total_matches) + ' matches')
    plt.show()
    
def get_average_score_per_game(file_path, first_ai, second_ai):
    """Read the result of the tournament and calculate the average win score for each AI."""
   
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_scores_first_ai = 0
    total_win_games_first_ai = 0
    total_scores_second_ai = 0
    total_win_games_second_ai = 0

    for line in lines:
        result, score_first_ai, score_second_ai = line.strip().strip('()').split(', ')
        if result != "None":
            
            if int(result) == first_ai :  
                total_win_games_first_ai += 1
                total_scores_first_ai += (int(score_first_ai) - int(score_second_ai))
            else:
                total_win_games_second_ai += 1
                total_scores_second_ai += (int(score_second_ai) - int(score_first_ai))

    average_win_score_first_ai = total_scores_first_ai / total_win_games_first_ai
    average_win_score_second_ai = total_scores_second_ai / total_win_games_second_ai

    return average_win_score_first_ai, average_win_score_second_ai

def plot_average_score_per_game(first_ai, second_ai, file_path):
    """Plot the average win score per game for each AI."""
    
    average_win_score_first_ai, average_win_score_second_ai = get_average_score_per_game(file_path, first_ai, second_ai)

    plt.bar([dict_ai[first_ai], dict_ai[second_ai]], [average_win_score_first_ai, average_win_score_second_ai], color=[dict_ai_color[first_ai], dict_ai_color[second_ai]])

    plt.xlabel('AI')
    plt.ylabel('score win gap')
    plt.title('The average score win gap between the two AIs')
    plt.xticks(rotation=45)
    plt.show()

# Example usage
first_ai = 0 
second_ai = 1
file_path = 'src/performance/'+dict_ai[first_ai]+"_vs_"+dict_ai[second_ai]+'.txt'
plot_average_score_per_game(first_ai, second_ai, file_path)
