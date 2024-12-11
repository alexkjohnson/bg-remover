from rembg import remove
from PIL import Image

# Load input image
input_path = "input.jpg"
output_path = "output.png"

with open(input_path, "rb") as inp_file:
    input_image = inp_file.read()

# Remove background
output_image = remove(input_image)

# Save output image
with open(output_path, "wb") as out_file:
    out_file.write(output_image)

