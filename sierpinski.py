import pygame

colors = [pygame.Color(0, 0, 0, 255),       # Black
          pygame.Color(255, 0, 0, 255),     # Red
          pygame.Color(0, 255, 0, 255),     # Green
          pygame.Color(0, 0, 255, 255),     # Blue
          pygame.Color(255, 255, 255, 255)] # White

BLACK = 0
RED = 1
GREEN = 2
BLUE = 3
WHITE = -1

# This function draws a triangle using the polygon function from pygames draw
# module.
# p1 - is the coordinates of the first vertex of the triangle
# p2 - is the coordinates of the second vertex of the triangle
# p3 - is the coordinates of the third vertex of the triangle
# All coordinates are given as a list of two floats, [x, y] that specify a
# position on the pygame screen.
# color - is an integer constant used to index into the colors list to select a
# pygame Color object to assign a color to this triangle.
# line_width - is an integer that determines the thickness of the lines used to
# draw the triangle. The larger the integer the thicker the line.
# If line-width is set to 0, then pygame will fill the triangle in with the 
# chosen color.
# screen - This variable stores a reference to the pygame screen object upon
# which the program will draw.
# This function has no return value.
def draw_triangle(p1, p2, p3, color, line_width, screen):
    pygame.draw.polygon(screen, colors[color], [p1, p2, p3], line_width)
    pygame.display.flip()

# This function returns a point that lies at the midpoint between the input
# points.
# p1 - the coordinates of the first point
# p2 - the coordinates of the second point
# Each point is a list of two floats, [x, y]
# The function should return coordinates--a list of two floats--that locate the
# point that is midway between p1 and p2.
def find_midpoint(p1, p2):
    x = (p1[0] + p2[0])/2.0
    y = (p1[1] + p2[1])/2.0
    return [x, y]

# This function draws a tringle, and then recursively calls itself to ensure
# that three smaller triangles are drawn within the new triangle, as described
# by the Sierpinski Triangle algorithm.
# degree - This describes the depth of recursion remaining--how many more levels
# of triangles are going to be drawn in this image.
# p1 - the coordinates of the first vertex of the new triangle
# p2 - the coordinates of the second vertex of the new triangle
# p3 - the coordinates of the third vertex of the new triangle
# color - the color of the new triangle
# line_width - The width of the line used to draw the triangle.
# screen - The pygame surface upon which the Sierpinski triangle will be drawn
def sierpinski(degree, p1, p2, p3, color, line_width, screen):
    #p1 is left botom point
    #p2 is middle top point
    #p3 is right bottom point
    draw_triangle(p1, p2, p3, color, line_width, screen)
    if(degree > 0):
        p1_p2_midpoint = find_midpoint(p1, p2)
        p2_p3_midpoint = find_midpoint(p2, p3)
        p3_p1_midpoint = find_midpoint(p3, p1)
        sierpinski(degree-1, p1, p1_p2_midpoint, p3_p1_midpoint, color, line_width, screen)
        sierpinski(degree-1, p1_p2_midpoint, p2, p2_p3_midpoint, color, line_width, screen)
        sierpinski(degree-1, p3_p1_midpoint, p2_p3_midpoint, p3, color, line_width, screen)
        
        

def main():
    # This call is necessary to initialize the resources in the pygame library.
    pygame.init()

    width = 640 # The size of the drawing surface in the horizontal dimension (y)
    height = 640 # The size of the drawing surface in the vertical dimension (x)
    # The size value is used by pygame to create the surface; it is a list of 
    # the values for the width and the height (in that order).
    size = [width, height] 

    # These coordinates identify the vertices of the first, outermost triangle.
    # They are set to center the triangle in the drawing surface, and set 5
    # pixels from the borders on each side.
    p1 = [5, height - 5]
    p2 = [(width - 10) / 2, 5]
    p3 = [width - 5, height - 5]
    initial_color = BLACK # The initial color assigned to the triangle.
    initial_line_width = 1 # The initial line_width assigned to the triangle.
                           # Set to 1 to tell pygame to draw the triangle with
                           # the thinnest possible line and leave the triangle
                           # unfilled.

    degree = 5 # The degree of the Sierpinski triangle. This indicates how many
               # levels of recursion to go down while drawing the triangle.
    
    # Sets a caption describing the contents of the drawing surface in the title
    # bar.
    pygame.display.set_caption("Sierpinski Triangle")
    
    # Creates the drawing surface of the specified size. A reference to that
    # surface is stored in the variable screen
    screen = pygame.display.set_mode(size)
    
    # Colors the background of the drawing surface white.
    screen.fill(WHITE)

    # Causes changes made to the screen object (so far just setting the
    # background to white) to become visible.
    pygame.display.flip()
    
    # Initial call to the recursive function. This will draw the first,
    # outermost triangle (the degree 0 triangle).
    sierpinski(degree, p1, p2, p3, initial_color, initial_line_width, screen)

    done = False
    count = 0
    while not done:
        count = count + 1
        if count % 1000000 == 0:
            print(".", end = "")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    print("\nNow Quitting")
    pygame.quit()
    
if __name__ == "__main__":
    main()
