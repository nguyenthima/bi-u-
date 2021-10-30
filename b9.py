import matplotlib.pyplot as plt
import numpy as np

divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"]
divisions_average_marks = [70,82,73,65,68]

plt.bar(divisions, divisions_average_marks, color="green")
plt.title("Bar Graph")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()