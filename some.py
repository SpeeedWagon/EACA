import ComplexPygame as C
import Color
import cmath
import math # For pi, fmod if needed
import bisect # For a more robust searchsorted equivalent


def paint_bisector_regions(z1, z2, z3, region_colors_input):
    global dim, mustPainting # mustPainting to check if we should continue

    # 1. Calculate side lengths
    a = abs(z3 - z2)
    b = abs(z1 - z3)
    c = abs(z2 - z1)

    # Check for degenerate triangle (collinear points or zero-length side)
    # Using triangle inequality: sum of two sides must be greater than the third
    eps = 1e-9
    if not (a + b > c - eps and a + c > b - eps and b + c > a - eps and a > eps and b > eps and c > eps):
        print("Degenerate triangle, cannot compute incenter robustly.")
        C.fillScreen(Color.Black) 
        C.drawNgon([z1, z2, z3], Color.Black)
        # C.setTextIJ("Degenerate Triangle", 10, 30, Color.Black, 20)
        C.refreshScreen()
        return

    # 2. Calculate Incenter
    incenter = (a * z1 + b * z2 + c * z3) / (a + b + c)

    # 3. Determine angles of bisector lines from incenter
    v_I_z1 = z1 - incenter
    v_I_z2 = z2 - incenter
    v_I_z3 = z3 - incenter

    if abs(v_I_z1) < eps or abs(v_I_z2) < eps or abs(v_I_z3) < eps:
        print("Incenter very close to a vertex.") # Should be caught by degeneracy check
        C.fillScreen(Color.Gray)
        C.drawNgon([z1, z2, z3], Color.Black)
        # setTextIJ("Incenter near vertex", 10, 30, Colo, 20)
        C.refreshScreen()
        return

    boundary_angles_rad_list = [
        cmath.phase(v_I_z1), cmath.phase(v_I_z2), cmath.phase(v_I_z3),
        cmath.phase(v_I_z1) + cmath.pi, cmath.phase(v_I_z2) + cmath.pi, cmath.phase(v_I_z3) + cmath.pi,
    ]

    # 4. Normalize angles to [0, 2*pi) and sort
    two_pi = 2 * cmath.pi
    normalized_angles = sorted([(val % two_pi + two_pi) % two_pi for val in boundary_angles_rad_list])
    
    deduplicated_angles = []
    if normalized_angles:
        deduplicated_angles.append(normalized_angles[0])
        for i in range(1, len(normalized_angles)):
            diff = normalized_angles[i] - deduplicated_angles[-1]
            if abs(diff) > 1e-7:
                 deduplicated_angles.append(normalized_angles[i])
            # Check wrap-around for last vs first if they are too close (e.g. 0 and almost 2pi)
            if i == len(normalized_angles) - 1:
                 first_angle_diff_abs = abs((deduplicated_angles[-1] - deduplicated_angles[0]) - two_pi)
                 if first_angle_diff_abs < 1e-7 and len(deduplicated_angles) > 1: # if last is like 2pi & first is 0
                    deduplicated_angles.pop() # remove the "2pi-like" one, it's redundant with 0

    normalized_angles = deduplicated_angles

    if not normalized_angles:
        print("Error: No boundary angles found after processing.")
        return
    if len(normalized_angles) != 6 and len(normalized_angles) != 0 : # Allow 0 if it failed entirely
         print(f"Warning: Expected 6 distinct boundary angles, found {len(normalized_angles)}. Colors might be off.")


    # 5. Color regions by iterating through pixels
    pixels_per_refresh_row = 10 # Refresh screen every N rows for responsiveness

    for h_pixel_idx in range(dim):
        if not mustPainting or C.mustClose(): # Check for interruption
            print("Drawing interrupted by user.")
            return
        for k_pixel_idx in range(dim):
            zp_complex = C.getZ(h_pixel_idx, k_pixel_idx)
            vec_to_zp = zp_complex - incenter

            if abs(vec_to_zp) < eps: # Point is the incenter itself
                color_idx = 0 # Default to first color
            else:
                angle_zp_rad = cmath.phase(vec_to_zp)
                normalized_angle_zp_rad = (angle_zp_rad % two_pi + two_pi) % two_pi
                
                idx_after = bisect.bisect_right(normalized_angles, normalized_angle_zp_rad)
                current_sector_idx = (idx_after - 1 + len(normalized_angles)) % len(normalized_angles)
                color_idx = current_sector_idx % len(region_colors_input) # Ensure valid index

            C.setPixelHK(h_pixel_idx, k_pixel_idx, region_colors_input[color_idx])
        
        if h_pixel_idx % pixels_per_refresh_row == 0:
             C.refreshScreen()

    # 6. Draw the triangle on top
    C.drawNgon([z1, z2, z3], Color.Black)
    # Optional: Draw incenter
    # setPixel(incenter, COLOR_RED)
    C.refreshScreen() # Final refresh

def drawing_task_bisectors():
    # Vertices similar to the input image, assuming image center is (0,0) and extends to +/-1 approx
    # From original analysis: z1 ~ (-0.3, 0.6), z2 ~ (-0.5, -0.4), z3 ~ (0.7, 0.1)
    z1_v = complex(-0.3, 0.6)
    z2_v = complex(-0.5, -0.4)
    z3_v = complex(0.7, 0.1)
    all_z_coords = [z1_v, z2_v, z3_v]
    
    min_x = min(z.real for z in all_z_coords)
    max_x = max(z.real for z in all_z_coords)
    min_y = min(z.imag for z in all_z_coords)
    max_y = max(z.imag for z in all_z_coords)
    
    padding_x = (max_x - min_x) * 0.25
    padding_y = (max_y - min_y) * 0.25
    if padding_x < 0.2: padding_x = 0.5 # Min padding if triangle is small/flat
    if padding_y < 0.2: padding_y = 0.5

    C.setXminXmaxYminYmax(
        min_x - padding_x, max_x + padding_x,
        min_y - padding_y, max_y + padding_y
    )
    
    paint_bisector_regions(z1_v, z2_v, z3_v, C.region_color_list_rgb)


if __name__ == '__main__':
    C.initPygame()
    C.run(drawing_task_bisectors)
    C.quit()