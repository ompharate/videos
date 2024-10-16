import cv2
import pytesseract
import time
import picamera
import picamera.array

# Set the tesseract cmd path if necessary (uncomment and modify the line below if needed)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Function to process the frame and extract text
def process_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply some image processing for better OCR
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Use pytesseract to do OCR on the processed image
    text = pytesseract.image_to_string(thresh)

    return text

def main():
    # Initialize the Pi Camera
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)  # Set the resolution
        camera.framerate = 30            # Set the frame rate
        time.sleep(2)                    # Allow the camera to warm up

        # Create an array to hold the camera frames
        with picamera.array.PiRGBArray(camera) as output:
            print("Press 'q' to quit.")
            
            for frame in camera.capture_continuous(output, format="bgr", use_video_port=True):
                image = frame.array  # Get the current frame
                
                # Process the frame to extract text
                text = process_frame(image)
                if text.strip():  # Only print if text is found
                    print("Extracted Text:", text.strip())

                # Show the frame
                cv2.imshow('Pi Camera', image)

                # Clear the output array for the next frame
                output.truncate(0)

                # Press 'q' to quit the window
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
