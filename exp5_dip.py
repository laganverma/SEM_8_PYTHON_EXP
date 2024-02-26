import cv2
import numpy as np

def threshold_image(input_path, output_path, threshold_values):
    try:
        # Read the input image
        img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        # Apply thresholding with three different values
        thresholded_images = [cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)[1] for threshold in threshold_values]
        # Display and save the thresholded images
        for i, thresholded_img in enumerate(thresholded_images):
            cv2.imshow(f"Threshold {i+1}", thresholded_img)
            cv2.imwrite(output_path.format(i+1), thresholded_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    input_path = "C:/Users//lagan//OneDrive//Desktop//1.jpg"
    output_path_template = "C//Users//lagan//OneDrive//Desktop//2.jpg"
    threshold_values = [100, 150, 200]
    # Threshold the image with three different values
    threshold_image(input_path, output_path_template, threshold_values)
