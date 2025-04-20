from rembg import remove
from PIL import Image
input_path = 'input.png'
output_path = 'output.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print(f"Background removed and saved to {output_path}")

Image.open(output_path)
# This code snippet demonstrates how to use the rembg library to remove the background from an image.
# The above code uses the rembg library to remove the background from an image.
# It reads an image from 'input.png', processes it to remove the background, and saves the result to 'output.png'.
# The rembg library is a powerful tool for background removal, and it can be used in various applications such as e-commerce, photography, and graphic design.
# The code is simple and efficient, making it easy to integrate into larger projects or workflows.
# The rembg library is built on top of deep learning models, which allows it to achieve high accuracy in background removal.
# The library supports various image formats, including PNG, JPEG, and BMP.
# It also provides options for customizing the output, such as changing the background color or adding a new background.