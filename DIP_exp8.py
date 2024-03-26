import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_averaging_filter(input_path, output_path, kernel_size):
    try:
        # Read the input image
        img = cv2.imread(input_path)
        # Apply the averaging filter
        kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
        filtered_img = cv2.filter2D(img, -1, kernel)
        # Display the original and filtered images
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(filtered_img, cv2.COLOR_BGR2RGB))
        plt.title(f'Averaging Filter (Kernel Size {kernel_size})')
        plt.show()
        # Save the filtered image
        cv2.imwrite(output_path, filtered_img)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    input_path = "C:/Users//lagan//OneDrive//Desktop//2.jpg"
    output_path = "C:/Users//lagan//OneDrive//Desktop//filtered_image.jpg"
    kernel_size = 5  # Adjust the kernel size as needed
    # Apply averaging filter
    apply_averaging_filter(input_path, output_path, kernel_size)
