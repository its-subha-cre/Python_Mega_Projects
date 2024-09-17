from sketchpy import canvas
class Canvas:
    def load_svg(self):
        res = None  # Default initialization
        try:
            # Your logic to load the SVG file
            # For example:
            with open(self.svg_file_path, 'r') as file:
                res = file.read()  # Assuming you are reading the SVG content
        except Exception as e:
            print(f"An error occurred while loading the SVG file: {e}")
            # Handle the error or set a default value for `res` if needed
        return res

obj=canvas.sketch_from_svg("D:\\Python_mega_projects\\pic (1).svg")
obj.draw()

