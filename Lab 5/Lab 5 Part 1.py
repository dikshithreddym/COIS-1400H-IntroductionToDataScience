import matplotlib.pyplot as plt
import numpy as np

# Load the image from the specified path
myImage = plt.imread("C:/Users/diksh/Desktop/COIS 1400H/Lab5/flower.png")

# Get the height and width of the image
height = myImage.shape[0]
width = myImage.shape[1]

# Create a copy of the image to preserve the original data
greyscale_image = np.copy(myImage)

for x in range(height):
    for y in range(width):
        # Get the RGB values
        R = greyscale_image[x, y, 0]
        G = greyscale_image[x, y, 1]
        B = greyscale_image[x, y, 2]

        # Calculate the average of the RGB values
        average = (R + G + B) / 3

        # Set the RGB values to the average for greyscale conversion
        greyscale_image[x, y, :3] = [average, average, average]

# Display the greyscale image
plt.imshow(greyscale_image, cmap='gray')
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()

# Save the greyscale image to the specified path
output_path = "C:/Users/diksh/Desktop/COIS 1400H/Lab5/flower_greyscale.png"
plt.imsave(output_path, greyscale_image, cmap='gray')
