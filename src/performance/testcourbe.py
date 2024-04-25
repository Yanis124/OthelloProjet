import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def approximate_curve(x, y, degree=3):

    coeffs = np.polyfit(x, y, degree)
    
    polynomial_func = np.poly1d(coeffs)
    

    x_new = np.linspace(min(x), max(x), 100)
 
    y_new = polynomial_func(x_new)
    
    return x_new, y_new

file_path = "/home/yassfkh/Desktop/OthelloProjet/OthelloProjet/src/performance/explored_nodes.txt"
with open(file_path, "r") as file:
    all_results = []
    current_game_results = []

    for line in file:
   
        if any(char.isdigit() for char in line):
        
            current_game_results.append(int(line.split(",")[0][1:])) 
        else:
  
            if current_game_results:
    
                all_results.append(current_game_results)
                current_game_results = [] 
    if current_game_results:
        all_results.append(current_game_results)

sns.set(style="dark", rc={"figure.figsize": (12, 8), "axes.grid": False})

colors = sns.color_palette("husl", 10) 
for i, game_results in enumerate(all_results):
    moves_played = range(1, len(game_results) + 1)
    plt.fill_between(moves_played, game_results, color=colors[i], alpha=0.3) 
    sns.lineplot(x=moves_played, y=game_results, color=colors[i], linewidth=1.0, label=f'Partie {i+1}')


    x_new, y_new = approximate_curve(moves_played, game_results)
    plt.plot(x_new, y_new, linestyle='--', color='gray', linewidth=1.0)


plt.xlabel('Coup joué', fontsize=14)
plt.ylabel('Nombre de nœuds visités', fontsize=14)
plt.title('Évolution du nombre de nœuds visités', fontsize=18, pad=20)


sns.despine()


plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), fontsize=12)


plt.savefig('explored_nodes_with_approximation.png', dpi=300, bbox_inches='tight')


plt.show()
