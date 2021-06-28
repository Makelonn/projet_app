import matplotlib.pyplot as plt
import pandas as pd
from math import pi

def radar_graph(data):
    """Generates a radar graph from inputed data"""

    # Set data
    df = pd.DataFrame({
        'Force': data[0],
        'Intelligence': data[1],
        'Dextérité': data[2],
        'Sagesse': data[3],
        'Constitution': data[4],
        'Charisme': data[5]
    }, index=[0])
    
    # number of variable
    categories=list(df)
    N = len(categories)
    
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values=df.values.flatten().tolist()
    values += values[:1]

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([5,10,15, 20], ["5","10","15", "20"], color="grey", size=7)
    plt.ylim(0,20)
    
    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    return ax
