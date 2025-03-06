# Cross-sectional Area Volume Calculator

This Python script calculates the volume of a solid object using numerical integration by summing the volumes of square cross-sections at different points along its length.

## Mathematical Concept

The script uses the following approach:
1. Divides the solid into thin slices (thickness = 0.15 cm)
2. Calculates the side length of each square cross-section using the function: `-1/9 * x² + 9`
3. Computes the area of each cross-section
4. Approximates the total volume using numerical integration (sum of areas × slice thickness)

## Requirements

- Python 3.x
- NumPy

## Installation

```bash
pip install numpy
```

## Usage

Simply run the script:

```bash
python main.py
```

The script will output the approximate volume of the solid in cubic centimeters (cm³).

## How it Works

1. The script uses a slice thickness (Δx) of 0.15 cm
2. For each slice, it:
   - Calculates the x-coordinate at the midpoint of the slice
   - Determines the side length of the square cross-section at that point
   - Computes the area of the square cross-section
3. Finally, it sums up the volumes of all slices (area × thickness) to approximate the total volume