# Import required libraries
import numpy as np  # For numerical operations and array handling
import matplotlib.pyplot as plt  # For data visualization
from PIL import Image  # For image processing
from scipy.ndimage import gaussian_filter  # For more realistic blur simulation

def load_and_preprocess_image(image_path):
    """
    Load and preprocess an image for analysis.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        numpy.ndarray: Preprocessed grayscale image normalized to [0,1]
    """
    # Open image and convert to grayscale
    image = Image.open(image_path).convert('L')
    # Convert to numpy array and normalize
    return np.array(image) / 255.0

def simulate_atmospheric_effects(image, turbulence_strength=0.3, blur_sigma=1.0):
    """
    Simulate atmospheric effects on an astronomical image.
    
    Args:
        image (numpy.ndarray): Input image
        turbulence_strength (float): Amount of noise to add (0-1)
        blur_sigma (float): Standard deviation for Gaussian blur
        
    Returns:
        numpy.ndarray: Image with simulated atmospheric effects
    """
    # Add Gaussian noise for turbulence
    turbulence = np.random.normal(0, turbulence_strength, image.shape)
    # Apply Gaussian blur for light scattering
    blurred = gaussian_filter(image + turbulence, sigma=blur_sigma)
    # Ensure pixel values stay in valid range
    return np.clip(blurred, 0, 1)

def calculate_image_metrics(original, processed):
    """
    Calculate quality metrics between original and processed images.
    
    Args:
        original (numpy.ndarray): Reference image
        processed (numpy.ndarray): Modified image
        
    Returns:
        dict: Dictionary of calculated metrics
    """
    # Mean Squared Error
    mse = np.mean((original - processed) ** 2)
    # Peak Signal-to-Noise Ratio
    psnr = 10 * np.log10(1 / mse) if mse > 0 else float('inf')
    return {'MSE': mse, 'PSNR': psnr}

def visualize_comparison(original, processed, metrics):
    """
    Create comparison plot of original vs processed images.
    
    Args:
        original (numpy.ndarray): Original image
        processed (numpy.ndarray): Processed image
        metrics (dict): Calculated quality metrics
    """
    plt.figure(figsize=(15, 6))
    
    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Observation\n(Shahrekord University)')
    plt.axis('off')
    
    # Processed image
    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap='gray')
    plt.title(f"Simulated Atmospheric Effects\nMSE: {metrics['MSE']:.4f}, PSNR: {metrics['PSNR']:.2f} dB")
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    """Main function to execute the image analysis pipeline."""
    try:
        # Load and preprocess image
        image_path = r"C:\Users\moh\Downloads\moon.jpg"  # Raw string for Windows paths
        original_image = load_and_preprocess_image(image_path)
        
        # Simulate atmospheric effects
        processed_image = simulate_atmospheric_effects(original_image,
                                                     turbulence_strength=0.3,
                                                     blur_sigma=1.0)
        
        # Calculate quality metrics
        metrics = calculate_image_metrics(original_image, processed_image)
        
        # Display results
        print("\nImage Quality Metrics:")
        print(f"MSE: {metrics['MSE']:.4f} (Lower is better)")
        print(f"PSNR: {metrics['PSNR']:.2f} dB (Higher is better)")
        
        visualize_comparison(original_image, processed_image, metrics)
        
    except FileNotFoundError:
        print("Error: Image file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
