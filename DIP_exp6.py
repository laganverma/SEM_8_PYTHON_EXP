import cv2

def crop_image(input_path,output_path,x,y,width,height):
    try:
        # Read the input image
        img=cv2.imread(input_path)
        # Crop the image
        cropped_img=img[y:y+height,x:x+width]
        # Display and save the cropped image
        cv2.imshow("Cropped Image",cropped_img)
        cv2.imwrite(output_path,cropped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")


def resize_image(input_path,output_path,new_width,new_height):
    try:
        # Read the input image
        img=cv2.imread(input_path)
        # Resize the image
        resized_img=cv2.resize(img,(new_width,new_height))
        # Display and save the resized image
        cv2.imshow("Resized Image",resized_img)
        cv2.imwrite(output_path,resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")


def scale_image(input_path,output_path,scale_factor):
    try:
        # Read the input image
        img=cv2.imread(input_path)
        # Scale the image
        scaled_img=cv2.resize(img,None,fx=scale_factor,fy=scale_factor)
        # Display and save the scaled image
        cv2.imshow("Scaled Image",scaled_img)
        cv2.imwrite(output_path,scaled_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")


def flip_image(input_path,output_path,flip_code):
    try:
        # Read the input image
        img=cv2.imread(input_path)
        # Flip the image
        flipped_img=cv2.flip(img,flip_code)
        # Display and save the flipped image
        cv2.imshow("Flipped Image",flipped_img)
        cv2.imwrite(output_path,flipped_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Error: {e}")


if __name__=="__main__":
    # Example usage
    input_path="C:/Users//lagan//OneDrive//Desktop//2.jpg"
    output_path_cropped="C:/Users//lagan//OneDrive//Desktop//cropped_image.jpg"
    output_path_resized="C:/Users//lagan//OneDrive//Desktop//resized_image.jpg"
    output_path_scaled= "C:/Users//lagan//OneDrive//Desktop//scaled_image.jpg"
    output_path_flipped="C:/Users//lagan//OneDrive//Desktop//flipped_image.jpg"

    # Crop the image
    crop_image(input_path,output_path_cropped,x=50,y=50,width=300,height=200)
    # Resize the image
    resize_image(input_path,output_path_resized,new_width=400,new_height=300)
    # Scale the image
    scale_image(input_path,output_path_scaled,scale_factor=0.5)
    # Flip the image (flip_code: 0 - horizontal, 1 - vertical, -1 - both)
    flip_image(input_path,output_path_flipped,flip_code=1)
