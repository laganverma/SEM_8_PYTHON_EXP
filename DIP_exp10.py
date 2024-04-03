import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, sigma=25):
    """
    Add Gaussian noise to the input image.
    """
    row, col, ch = image.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    noisy = np.clip(image + gauss, 0, 255)
    return noisy.astype(np.uint8)

def apply_filters(image):
    """
    Apply different filters to remove noise.
    """
    # Median Filter
    median_filtered = cv2.medianBlur(image, 5)
    # Bilateral Filter
    bilateral_filtered = cv2.bilateralFilter(image, 9, 75, 75)
    # Gaussian Filter
    gaussian_filtered = cv2.GaussianBlur(image, (5, 5), 0)
    return median_filtered, bilateral_filtered, gaussian_filtered

def main():
    # Read a sample image
    input_image = cv2.imread("C:/Users/lagan/OneDrive/Desktop/4.jpeg")
    # Add Gaussian noise to the image
    noisy_image = add_gaussian_noise(input_image)
    # Apply different filters
    median_filtered, bilateral_filtered, gaussian_filtered = apply_filters(noisy_image)
    # Display original and filtered images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 4, 1)
    plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(1, 4, 2)
    plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
    plt.title('Noisy Image')
    plt.subplot(1, 4, 3)
    plt.imshow(cv2.cvtColor(median_filtered, cv2.COLOR_BGR2RGB))
    plt.title('Median Filter')
    plt.subplot(1, 4, 4)
    plt.imshow(cv2.cvtColor(bilateral_filtered, cv2.COLOR_BGR2RGB))
    plt.title('Bilateral Filter')
    plt.show()
    # Display Gaussian Filtered Image
    plt.figure(figsize=(5, 5))
    plt.imshow(cv2.cvtColor(gaussian_filtered, cv2.COLOR_BGR2RGB))
    plt.title('Gaussian Filter')
    plt.show()

if __name__ == "__main__":
    main()
