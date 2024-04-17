#display the data of the tournament in a graphs

import matplotlib.pyplot as plt

dict_ai = {0: 'easy', 1: 'normal', 2: 'hard'}
dict_ai_color = {0: '#1f77b4', 1: '#2ca02c', 2: '#ff7f0e'}
draw_color = '#808080'

def get_result_tournament(file_path, first_ai, second_ai):
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

# Example usage
first_ai = 1
second_ai = 2
file_path = 'src/performance/'+dict_ai[first_ai]+"_vs_"+dict_ai[second_ai]+'.txt'  # Path to your data file
results = get_result_tournament(file_path, first_ai, second_ai)
draw_circle_graph(first_ai, second_ai, results[0], results[1], results[2], results[3])
