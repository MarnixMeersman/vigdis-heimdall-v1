#!/usr/bin/env python3

import curses
import math
import time
from Helios import HeliosDAC, HeliosPoint, HELIOS_MAX_POINTS

# Generate a filled square (grid of points + outline)
def generate_filled_square(cx, cy, size):
    border = []
    half = size / 2
    # Outline corners (closed loop)
    corners = [
        (cx - half, cy - half),
        (cx + half, cy - half),
        (cx + half, cy + half),
        (cx - half, cy + half),
        (cx - half, cy - half),
    ]
    for x, y in corners:
        border.append(HeliosPoint(int(x), int(y)))

    # Number of interior points we can use
    interior_max = HELIOS_MAX_POINTS - len(border)
    grid_n = int(math.floor(math.sqrt(interior_max)))
    if grid_n < 2:
        grid_n = 2

    grid_points = []
    # Uniform grid fill
    for i in range(grid_n):
        for j in range(grid_n):
            x = cx - half + i * (size / (grid_n - 1))
            y = cy - half + j * (size / (grid_n - 1))  # corrected to use cy
            grid_points.append(HeliosPoint(int(x), int(y)))

    # Draw fill first, then outline last
    return grid_points + border

# Main loop with arrow-key controls
def main(stdscr):
    curses.curs_set(False)
    stdscr.nodelay(False)
    stdscr.keypad(True)

    # Initial parameters
    cx, cy = 2048, 2048    # Center coordinates
    size = 1000            # Side length of the square
    step = 100             # Movement step per key press
    pps = 10000  # 50 kpps   # Points-per-second for DAC

    # Initialize DAC and start queue thread
    dac = HeliosDAC()
    dac.runQueueThread()

    stdscr.addstr(0, 0, "Arrow keys to move, q to quit")
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP:
            cy = min(cy + step, 4095)
        elif key == curses.KEY_DOWN:
            cy = max(cy - step, 0)
        elif key == curses.KEY_LEFT:
            cx = max(cx - step, 0)
        elif key == curses.KEY_RIGHT:
            cx = min(cx + step, 4095)
        elif key == ord('q'):
            break

        # Generate and send one frame
        pts = generate_filled_square(cx, cy, size)
        dac.newFrame(pps, pts)

        # Display current center
        stdscr.addstr(1, 0, f"Center: ({cx}, {cy})      ")

if __name__ == "__main__":
    curses.wrapper(main)
