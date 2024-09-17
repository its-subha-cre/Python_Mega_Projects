from wand.image import Image
from .api import library
# Import the image
with Image(filename ='../pic.jpeg') as image:
    # Clone the image in order to process
    with image.clone() as sketch:
        # Invoke sketch function 
        sketch.sketch(15, 5, 10)
        # Save the image
        sketch.save(filename ='sketch1.jpg')