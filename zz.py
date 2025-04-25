#z\in C | |Z|<3
#z \in C so that abs(z.re)<3
#Z in C so that =3< z.im<-1
#z IN c PI/6
#
#
#

import ComplexPygame as cp
import Color
import random
import cmath
import math
import time
def getPixelColor(z):
    """
    Gets the color of the pixel corresponding to the complex number z.

    Args:
        z (complex): The complex number.

    Returns:
        pygame.Color: The color of the specified pixel.
                       Returns Color.Black if coordinates are out of bounds.
    """
    # Use the internal _getIJ which correctly calculates screen (i, j) from z
    i, j = cp._getIJ(z)

    # Ensure coordinates are within the surface bounds
    if 0 <= i < cp.dim and 0 <= j < cp.dim:
        try:
           return cp.screen.get_at((i, j))
        except IndexError: # Safety check
            print(f"Warning: getPixelColor index ({i}, {j}) out of bounds for {z}")
            return cp.Color(Color.Black)
# def desRaza():
     
#      C.setXminXmaxYminYmax(-10, 10, -10, 10)
#      r = 3
#      for z in C.screenAffixes():
#           col = Color.Black
#           if(abs(z)<r):
#                col = Color.White
#           C.setPixel(z,col)
#           if(C.getHK(z)[0]%50 == 0):
#                C.refreshScreen()

# def desRegiuneReala():
#      C.setXminXmaxYminYmax(-10, 10, -10, 10)
#      for z in C.screenAffixes():
#           col = Color.Black
#           if(-3<z.real < 3):
#                col = Color.Green
#           C.setPixel(z,col)
#           if(C.getHK(z)[0]%50 == 0):
#                C.refreshScreen()

# def desRegiuneImaginara():
#      C.setXminXmaxYminYmax(-10, 10, -10, 10)
#      for z in C.screenAffixes():
#           col = Color.Black
#           if(-3<z.imag < -1):
#                col = Color.Greenyellow
#           C.setPixel(z,col)
#           if(C.getHK(z)[0]%50 == 0):
#                C.refreshScreen()

# def desCuArgument():
#      C.setXminXmaxYminYmax(-10, 10, -10, 10)
#      for z in C.screenAffixes():
#           col = Color.Black
#           if(z.real!=0 and (math.pi/6 < math.atan(z.imag/z.real) < math.pi/3)):
#                col = Color.Greenyellow
#           C.setPixel(z,col)
#           if(C.getHK(z)[0]%50 == 0):
#                C.refreshScreen()

# def desCuArgument2():
#      C.setXminXmaxYminYmax(-10, 10, -10, 10)
#      for z in C.screenAffixes():
#           col = Color.Black
          
#           if(z.real!=0 and (-math.pi/4<C.theta(z)< math.pi/4)):
#                col = Color.Greenyellow
#           C.setPixel(z,col)
#           if(C.getHK(z)[0]%250 == 0):
#                C.refreshScreen()
#                print(math.pi/4,math.pi - abs(math.atan(z.imag/z.real)))
def get_random_center(xmin, xmax, ymin, ymax):
    """Generates a random center point (as a complex number)."""
    random_x = random.uniform(xmin, xmax)
    random_y = random.uniform(ymin, ymax)
    return complex(random_x/2, random_y/2)

def get_random_radius(xmin, xmax, ymin, ymax, min_fraction=0.1, max_fraction=0.4):
    """Generates a random radius scaled relative to view size."""
    view_width = xmax - xmin
    view_height = ymax - ymin
    base_size = min(view_width, view_height)
    if base_size <= 0: return 0.1

    min_fraction = max(0.01, min_fraction)
    max_fraction = min(max_fraction, 0.5)
    if min_fraction >= max_fraction:
        min_fraction = 0.05
        max_fraction = 0.4

    min_radius = base_size * min_fraction
    max_radius = base_size * max_fraction
    return random.uniform(min_radius/2, max_radius/2)

def get_side_of_line(point, line_p1, line_p2, epsilon=1e-9):
    """
    Determines which side of the directed line (line_p1 -> line_p2) the point lies on.

    Args:
        point (complex): The point to check.
        line_p1 (complex): The start point of the line segment.
        line_p2 (complex): The end point of the line segment.
        epsilon (float): Tolerance for checking if point is on the line.

    Returns:
        int:  1 if the point is to the "left" of the line (p1->p2 vector).
             -1 if the point is to the "right" of the line.
              0 if the point is approximately on the line.
    """
    if abs(line_p1 - line_p2) < epsilon: # Avoid division by zero or issues with identical points
        return 0 # Or handle as a special case depending on needs

    # Using cross product: (p2.x-p1.x)*(p.y-p1.y) - (p2.y-p1.y)*(p.x-p1.x)
    # Sign determines the side.
    cross_product = (line_p2.real - line_p1.real) * (point.imag - line_p1.imag) - \
                    (line_p2.imag - line_p1.imag) * (point.real - line_p1.real)

    if abs(cross_product) < epsilon:
        return 0 # On the line
    elif cross_product > 0:
        return 1  # Left side
    else:
        return -1 # Right side

def draw_colored_regions_pixel_by_pixel():
    """
    Draws a random circle/triangle, extends lines, and colors the 7 screen
    regions distinctly using pixel-by-pixel evaluation.
    """
    start_time = time.time()

    # --- Define View Boundaries ---
    extent = 1.5
    xmin, xmax, ymin, ymax = -extent, extent, -extent, extent
    cp.setXminXmaxYminYmax(xmin, xmax, ymin, ymax)

    # --- Get Random Circle Parameters ---
    O = get_random_center(xmin, xmax, ymin, ymax)
    # Simplified radius logic for this example
    R = get_random_radius(xmin, xmax, ymin, ymax, min_fraction=0.2, max_fraction=0.4)

    # --- Choose 3 Random Points on the Circle ---
    triangle_vertices = []
    for _ in range(3):
        angle = random.uniform(0, 2 * math.pi)
        point = O + cmath.rect(R, angle)
        triangle_vertices.append(point)

    P1, P2, P3 = triangle_vertices[0], triangle_vertices[1], triangle_vertices[2]

    # --- Define Colors for Regions ---
    # We need up to 8 colors (2^3 combinations of sides)
    # Handle the case where a point is exactly on a line (side=0) later if needed
    colors = [
        Color.Lightcoral, Color.Lightskyblue, Color.Palegreen, Color.Lightyellow,
        Color.Orchid, Color.Aquamarine, Color.Orange, Color.Lightsteelblue
    ]
    # Assign a default color for points on lines?
    line_color = Color.Black

    # --- Color Pixels Based on Region ---
    print("Coloring pixels (this may take a moment)...")
    count = 0
    update_interval = cp.dim * cp.dim // 100 # Update progress roughly every 1%

    for h in range(cp.dim):
        for k in range(cp.dim):
            # Get coordinate for pixel (h, k) - remember cp flips y internally
            z = cp.getZ(h, k)

            # Determine side relative to each line
            side1 = get_side_of_line(z, P1, P2)
            side2 = get_side_of_line(z, P2, P3)
            side3 = get_side_of_line(z, P3, P1)

            # Assign color based on side combination
            pixel_color = line_color # Default if on a line
            if side1 != 0 and side2 != 0 and side3 != 0:
                # Create an index from 0 to 7 based on the sides (-1 -> 0, 1 -> 1)
                idx1 = (1 + side1) // 2 # 0 or 1
                idx2 = (1 + side2) // 2 # 0 or 1
                idx3 = (1 + side3) // 2 # 0 or 1
                color_index = idx1 * 4 + idx2 * 2 + idx3 * 1
                pixel_color = colors[color_index % len(colors)] # Use modulo for safety

            cp.setPixelHK(h, k, pixel_color)

            # --- Check for User Interrupt ---
            count += 1
            if count % update_interval == 0:
                # Update caption and check events less frequently for speed
                progress = int(100 * count / (cp.dim * cp.dim))
                # cp.display.set_caption(f"Coloring... {progress}%")
                if cp.mustClose():
                    print("Drawing cancelled.")
                    # Fill rest with a neutral color? Or just stop?
                    cp.fillScreen(Color.Gray)
                    cp.refreshScreen()
                    return # Exit the drawing function

    print(f"Pixel coloring finished in {time.time() - start_time:.2f} seconds.")

    # --- Optional: Overlay the Circle and Points ---
    # Draw the circle outline on top
    num_circle_points = 100
    circle_vertices = [O + cmath.rect(R, 2 * math.pi * i / num_circle_points) for i in range(num_circle_points)]
    cp.drawNgon(circle_vertices, Color.Darkslategray) # Thicker line

    # Mark the points
    point_color = Color.Black
    label_offset_val = 0.05 * R
    label_offset = complex(0, label_offset_val)
    for i, point in enumerate(triangle_vertices):
        # Draw a small filled circle for the point
        # Need a drawCircle function in ComplexPygame, approximating with ngon
        point_marker_verts = [point + cmath.rect(0.015, a) for a in [0, math.pi/2, math.pi, 3*math.pi/2]]
        cp.fillNgon(point_marker_verts, point_color)
        cp.setText(f"P{i+1}", point + label_offset, point_color, size=14)

    # --- Add Info Text ---
    info = f"Center: ({O.real:.2f}, {O.imag:.2f}), Radius: {R:.2f}"
    # Find suitable locations for text that might not overlap too much
    # cp.setTextIJ(info, 10, cp.dim - 40, Color.Black, size=14, background=Color.White) # Add background for legibility
    # cp.setTextIJ("Regions colored by line sides. Spacebar to redraw.", 10, cp.dim - 20, Color.Black, size=12, background=Color.White)
    for z in cp.screenAffixes():
        print(getPixelColor(z))
if __name__ == '__main__':
    cp.initPygame()
    cp.run(draw_colored_regions_pixel_by_pixel)
#     C.run(desRaza)
#     C.run(desRegiuneImaginara)
#     C.run(desRegiuneReala)
#     C.run(desCuArgument)
#     C.run(desCuArgument2)

