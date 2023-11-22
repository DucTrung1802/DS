
import os
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Make sure 2 file are in the same directory
# RUN "data_gen.py" FIRST then RUN this file

x_vals = []
y_vals = []

index = count()

current_folder = os.path.dirname(os.path.realpath(__file__))
csv_file_name = os.path.join(current_folder,"data_part_9.csv")

def animate(i):
    data = pd.read_csv(csv_file_name)
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()