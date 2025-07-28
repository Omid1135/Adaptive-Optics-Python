Adaptive Optics Python Simulation (adaptive_optics_demo.py)
---------------------------------------------------------

This Python script demonstrates how Adaptive Optics (AO) systems correct atmospheric turbulence in astronomical observations.

PHYSICS CONCEPTS:

1. Atmospheric Turbulence:
- Caused by varying refractive indices in Earth's atmosphere (Kolmogorov turbulence)
- Creates wavefront distortions that blur star images
- Simulated using:
  * High-frequency noise (Gaussian random)
  * Low-frequency distortions (sine waves)

2. Adaptive Optics Correction:
- Models real AO systems that:
  1) Measure distortions with wavefront sensors
  2) Correct using deformable mirrors
- Simulates 70% correction efficiency
- Maintains physical pixel value ranges [0,1]

CODE IMPLEMENTATION:

Key Components:
- Synthetic star generation (2D Gaussian)
- Turbulence simulation:
  np.random.normal(0, 0.5) + 0.1*np.sin() terms
- AO correction:
  corrected = blurred - (turbulence * 0.7)

ANALYSIS METRICS:
1. PSNR - Signal/noise ratio (dB)
2. SSIM - Structural similarity index

VISUAL OUTPUTS:
Generates 6-panel figure showing:
- Ideal, blurred, and corrected images
- Intensity profile comparisons
- Fourier power spectra

TECHNICAL DETAILS:
- Image size: 256x256 pixels
- Requires: Python, NumPy, Matplotlib, SciPy
- Run with: python adaptive_optics_demo.py

The complete simulation code is provided in the accompanying adaptive_optics_demo.py file.
----------------
# Atmospheric Optics Simulation (atmospheric_optics_simulator.py)

This Python script simulates atmospheric turbulence effects on astronomical images and demonstrates basic correction principles used in Adaptive Optics (AO) systems.

## Physics Concepts

### Atmospheric Turbulence
- Caused by refractive index variations in Earth's atmosphere (Kolmogorov turbulence theory)
- Two main effects simulated:
  1. High-frequency distortions: Small-scale refractive index fluctuations (Gaussian noise)
  2. Low-frequency distortions: Large-scale wavefront bending (simulated with blurring)

### Adaptive Optics Principles
- AO systems correct distortions by:
  1. Measuring wavefront errors (simulated here with noise estimation)
  2. Applying conjugate corrections (70% correction in this model)
- Limited by correction bandwidth and partial phase reconstruction

## Code Overview

### Key Functions
1. load_and_preprocess_image(): 
   - Loads astronomical images
   - Converts to grayscale and normalizes

2. simulate_atmospheric_effects():
   # Combines turbulence and blur effects
   turbulence = np.random.normal(0, strength, image.shape)
   blurred = gaussian_filter(image + turbulence, sigma=blur_sigma)

3. calculate_image_metrics():
   - Computes MSE and PSNR for quality assessment

4. visualize_comparison():
   - Generates side-by-side image comparison

## Usage
1. Place astronomical images in project folder
2. Update path in main() function
3. Run script:
   python atmospheric_optics_simulator.py

## Example Output
Image Quality Metrics:
MSE: 0.0482 (Lower is better)
PSNR: 13.24 dB (Higher is better)

## Technical Specifications
- Input: Astronomical images (JPG/PNG)
- Processing:
  - 256×256 pixel resolution
  - Turbulence strength: 0.3 (adjustable)
  - Blur sigma: 1.0 (adjustable)
- Dependencies: NumPy, Matplotlib, Pillow, SciPy

## Educational Applications
- Demonstrates atmospheric effects in astronomy
- Visualizes AO correction principles
- Provides quantitative image quality analysis

> The complete simulation code is available in atmospheric_optics_simulator.py
> ----------------------
