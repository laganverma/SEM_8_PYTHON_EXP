import cv2
import matplotlib.pyplot as plt

def display_image(input_path):
    try:
        # Read the input image
        img = cv2.imread(input_path)
        # Display the image using OpenCV
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")

def show_image_attributes(input_path):
    try:
        # Read the input image
        img = cv2.imread(input_path)
        # Get image attributes
        height, width, channels = img.shape
        # Display image attributes
        print(f"Image Dimensions: {width} x {height}")
        print(f"Number of Channels: {channels}")
    except Exception as e:
        print(f"Error: {e}")

def show_image_histogram(input_path):
    try:
        # Read the input image in grayscale
        img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        # Calculate histogram
        histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
        # Display the histogram using Matplotlib
        plt.plot(histogram)
        plt.title("Image Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    input_path = "C:/Users//lagan//OneDrive//Desktop//7.jpg"
    # Display the image
    display_image(input_path)
    # Show image attributes
    show_image_attributes(input_path)
    # Show image histogram
    show_image_histogram(input_path)
