import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from scipy.fft import fft2, fftshift

def display_caova_mission():
    print("\n=== Welcome to the Center of Adaptive Optics of Valparaíso (CAOVA) ===\n")
    print("We study Adaptive Optics (AO) to correct atmospheric turbulence for sharper telescope images.")

def simulate_and_analyze():
    # Generate a synthetic star image
    x = np.linspace(-5, 5, 256)
    y = np.linspace(-5, 5, 256)
    X, Y = np.meshgrid(x, y)
    star = np.exp(-(X**2 + Y**2))  # Ideal star (no turbulence)

    # Add simulated turbulence (random + spatial frequencies)
    turbulence = np.random.normal(0, 0.5, (256, 256)) 
    for _ in range(10):  # Add some low-frequency distortions
        turbulence += 0.1 * np.sin(0.5 * X + np.random.rand()) * np.sin(0.5 * Y + np.random.rand())
    blurred_star = np.clip(star + turbulence, 0, 1)  # Clip to avoid negative values

    # Simulate AO correction (partial correction)
    ao_correction = turbulence * 0.7  # AO removes 70% of turbulence
    corrected_star = np.clip(blurred_star - ao_correction, 0, 1)

    # --- Quantitative Analysis ---
    def calculate_metrics(original, distorted, corrected):
        # Peak Signal-to-Noise Ratio (PSNR)
        mse_blur = np.mean((original - distorted) ** 2)
        mse_ao = np.mean((original - corrected) ** 2)
        psnr_blur = 10 * np.log10(1 / mse_blur) if mse_blur > 0 else float('inf')
        psnr_ao = 10 * np.log10(1 / mse_ao) if mse_ao > 0 else float('inf')

        # Structural Similarity Index (SSIM)
        ssim_blur = ssim(original, distorted, data_range=1)
        ssim_ao = ssim(original, corrected, data_range=1)

        return {
            "PSNR (Blurred)": psnr_blur,
            "PSNR (AO Corrected)": psnr_ao,
            "SSIM (Blurred)": ssim_blur,
            "SSIM (AO Corrected)": ssim_ao
        }

    metrics = calculate_metrics(star, blurred_star, corrected_star)

    # --- Plotting ---
    fig = plt.figure(figsize=(18, 10))

    # Original, Blurred, and Corrected Images
    ax1 = plt.subplot(2, 3, 1)
    ax1.imshow(star, cmap='hot')
    ax1.set_title("Ideal Star (No Turbulence)")
    ax1.axis('off')

    ax2 = plt.subplot(2, 3, 2)
    ax2.imshow(blurred_star, cmap='hot')
    ax2.set_title(f"With Atmospheric Turbulence\nPSNR: {metrics['PSNR (Blurred)']:.2f} dB\nSSIM: {metrics['SSIM (Blurred)']:.2f}")
    ax2.axis('off')

    ax3 = plt.subplot(2, 3, 3)
    ax3.imshow(corrected_star, cmap='hot')
    ax3.set_title(f"After AO Correction\nPSNR: {metrics['PSNR (AO Corrected)']:.2f} dB\nSSIM: {metrics['SSIM (AO Corrected)']:.2f}")
    ax3.axis('off')

    # Intensity Profile Comparison
    ax4 = plt.subplot(2, 3, 4)
    ax4.plot(star[128, :], label='Ideal', linewidth=2)
    ax4.plot(blurred_star[128, :], label='Blurred', alpha=0.7)
    ax4.plot(corrected_star[128, :], label='AO Corrected', linestyle='--')
    ax4.set_title("Horizontal Intensity Profile (Center Row)")
    ax4.legend()
    ax4.grid()

    # Power Spectrum Analysis (FFT)
    ax5 = plt.subplot(2, 3, 5)
    fft_original = np.log10(fftshift(np.abs(fft2(star))) + 1)
    fft_blurred = np.log10(fftshift(np.abs(fft2(blurred_star)))) + 1
    ax5.imshow(fft_original, cmap='viridis')
    ax5.set_title("Power Spectrum (Ideal)")
    ax5.axis('off')

    ax6 = plt.subplot(2, 3, 6)
    ax6.imshow(fft_blurred, cmap='viridis')
    ax6.set_title("Power Spectrum (Blurred)")
    ax6.axis('off')

    plt.tight_layout()
    plt.show()

    print("\n=== Key Metrics ===")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")

# Run the functions
display_caova_mission()
simulate_and_analyze()
