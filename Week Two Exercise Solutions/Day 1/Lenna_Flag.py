import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the Lenna image
lenna_image_path = r'C:\Users\9tyle\OneDrive\Documents\GitHub\ROAR-Academy\samples\lenna.bmp'
lenna_image = Image.open(lenna_image_path).convert('RGB')
lenna_array = np.array(lenna_image)

# Load the national flag image
flag_image_path = r'C:\Users\9tyle\OneDrive\Documents\GitHub\ROAR-Academy\Week Two Exercise Solutions\us_flag.png'
flag_image = Image.open(flag_image_path).convert('RGB')
flag_array = np.array(flag_image)

# Resize the flag image to fit into the top right corner of the Lenna image
flag_height, flag_width, _ = flag_array.shape
lenna_height, lenna_width, _ = lenna_array.shape

if flag_height > lenna_height or flag_width > lenna_width:
    flag_image = flag_image.resize((min(flag_width, lenna_width), min(flag_height, lenna_height)))
    flag_array = np.array(flag_image)
    flag_height, flag_width, _ = flag_array.shape

# Replace the top right corner of the Lenna image with the flag image
lenna_array[:flag_height, -flag_width:, :] = flag_array

# Display the modified Lenna image
modified_lenna_image = Image.fromarray(lenna_array)
plt.imshow(modified_lenna_image)
plt.axis('off')  # Hide axis
plt.show()
