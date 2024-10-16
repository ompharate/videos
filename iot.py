import cv2
import pytesseract
import time

# Set the tesseract cmd path if necessary (uncomment and modify the line below if needed)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Function to process the frame and extract text
def process_frame(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply some image processing for better OCR
    # You can adjust the parameters as needed
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    # Use pytesseract to do OCR on the processed image
    text = pytesseract.image_to_string(thresh)
    
    return text

def main():
    # Initialize the camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()
        
        if not ret:
            print("Error: Failed to capture image.")
            break

        # Display the frame in a window
        cv2.imshow('Camera', frame)

        # Process the frame to extract text
        text = process_frame(frame)
        if text.strip():  # Only print if text is found
            print("Extracted Text:", text.strip())

        # Press 'q' to quit the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
