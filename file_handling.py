import shutil
import cv2
import time
import matplotlib.pyplot as plt
import os

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
        # buat output directory untuk save file
        output_dir = "data"
        os.makedirs(output_dir, exist_ok=True)
    
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
#x = capture_picture()
#if x:
#    print(f"Picture saved as {x}")
#else:
#    print("Picture capture cancelled.")

def create_bar_graph(x,y):

    # buat output directory untuk save file
    output_dir = "graph"
    os.makedirs(output_dir, exist_ok=True)

    # Create bar graph
    plt.bar(x, y)

    # Add title and labels
    plt.title("Bar Graph")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # Save the graph
    filename = "datalog.png"
    plt.savefig("./graph/" + filename)

    return filename

def delete_file():
    # Delete files inside data folder
    data_dir = "data"
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Delete files inside graph folder
    graph_dir = "graph"
    for file in os.listdir(graph_dir):
        file_path = os.path.join(graph_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Delete files inside out_image folder
    out_image_dir = "out_image"
    for file in os.listdir(out_image_dir):
        file_path = os.path.join(out_image_dir, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
