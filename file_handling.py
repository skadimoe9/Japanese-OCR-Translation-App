import shutil
import cv2
import time

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
    except IOError as e:
        print(f"Unable to copy file. {e}")
    except:
        print("Unexpected error occurred while copying file.")

# Example usage
#source = "path/to/source/file.txt"
#destination = "path/to/destination/file_copy.txt"

#copy_file(source, destination)

def capture_picture():
    # Initialize the camera
    cap = cv2.VideoCapture(0)  # 0 is usually the default camera

    # Wait a moment to allow the camera to initialize
    time.sleep(2)

    #open camera view
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        text = "Press 'c' to capture picture or 'q' to quit"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('c'):
            filename = f"captured_image_{int(time.time())}.jpg"
            cv2.imwrite("./data/" + filename, frame)
            cap.release()
            return filename
        
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            return False
        
            
    
    

# Example usage
x = capture_picture()

if x:
    print(f"Picture saved as {x}")
else:
    print("Picture capture cancelled.")

    