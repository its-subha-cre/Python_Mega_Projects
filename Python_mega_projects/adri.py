from sketchpy import canvas
obj=canvas.sketch_from_image('adri.jpeg')
obj.draw(threshold=145)
# import svgwrite

# # Create a new SVG drawing
# dwg = svgwrite.Drawing('cat.svg', profile='tiny')

# # Add elements to the drawing
# dwg.add(dwg.circle(center=(100, 100), r=50, fill='red'))

# # Save the drawing
# dwg.save()

# # Load and print the content of the new SVG file
# with open('cat.svg', 'r') as file:
#     svg_content = file.read()
#     print(svg_content)
