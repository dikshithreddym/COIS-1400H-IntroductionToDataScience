import matplotlib.pyplot as plt
from pydataset import data
import datetime

# Load the iris data
iris = data('iris')

# Get today's date in the format YYYY-MM-DD
today_date = datetime.date.today().strftime("%Y-%m-%d")

# Set up the figure for subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 12))

# Custom title with your name, student ID, and today's date
title_with_details = f"Dikshith Reddy Macherla, 0789055, {today_date}"

# Scatterplot 1: Sepal Length vs Sepal Width
axs[0, 0].scatter(iris['Sepal.Length'], iris['Sepal.Width'])
axs[0, 0].set_xlabel('Sepal Length')
axs[0, 0].set_ylabel('Sepal Width')
axs[0, 0].set_title(f'Scatter Plot of Sepal Dimensions\n{title_with_details}')

# Scatterplot 2: Petal Length vs Petal Width
axs[0, 1].scatter(iris['Petal.Length'], iris['Petal.Width'])
axs[0, 1].set_xlabel('Petal Length')
axs[0, 1].set_ylabel('Petal Width')
axs[0, 1].set_title(f'Scatter Plot of Petal Dimensions\n{title_with_details}')

# Pie Chart for Iris Species Distribution
labels = 'Virginica', 'Setosa', 'Versicolor'
sizes = [50, 50, 50]  # Assuming equal distribution
axs[1, 0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
axs[1, 0].set_title(f'Iris Species Distribution\n{title_with_details}')
axs[1, 0].axis('equal')  # Ensure the pie chart is drawn as a circle

# Histogram: Histogram of Sepal Length
axs[1, 1].hist(iris['Sepal.Length'])
axs[1, 1].set_xlabel('Sepal Length')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title(f'Histogram of Sepal Length\n{title_with_details}')

# Adjust layout for a better fit
plt.tight_layout()

# Adjust spacings between the subplots
fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.4, wspace=0.4)

# Show the plot
plt.show()
