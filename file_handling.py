import shutil
import cv2
import time
import matplotlib.pyplot as plt
import mplcursors
import sqlite3
import os 
from server import get_daily_data
import numpy as np
import tkinter as tk
from tkinter import filedialog

def select_image_file():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Open file dialog and allow user to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.jfif")]
    )
    if file_path:
        return file_path
    else:
        print("No file selected")

# Example usage
# if __name__ == "__main__":
#     selected_file = select_image_file()
#     if selected_file:
#         print("Selected file:", selected_file)
#     else:
#         print("No file selected")

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
            cv2.destroyAllWindows()
            return False

# Example usage
#x = capture_picture()
#if x:
#    print(f"Picture saved as {x}")
#else:
#    print("Picture capture cancelled.")

def create_bar_graph(x,y):
    os.environ['QT_AUTO_SCREEN_SCALE_FACTOR'] = '1'
    os.environ['QT_SCREEN_SCALE_FACTORS'] = '1'
    os.environ['QT_SCALE_FACTOR'] = '1'

    # buat output directory untuk save file
    output_dir = "graph"
    os.makedirs(output_dir, exist_ok=True)

    # Create bar graph
    plt.figure(figsize=(8, 4))
    bars = plt.bar(x, y, color='#b0802626', width=0.5)

    # Add title and labels
    plt.title("Kanji App Used")
    plt.xlabel("Date")
    plt.ylabel("Character(s) Translated") 
    
    cursor = mplcursors.cursor(bars, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'{y[sel.index]}'))
    cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set(fc="white"))

    # Save the graph
    filename = "datalog.png"
    plt.savefig("./graph/" + filename)
    plt.show()

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

def fetch_graphing_data(username):
    # Connect to the SQLite database
    conn = sqlite3.connect('account_database.db')
    cursor = conn.cursor()
    
    # Execute the query to fetch date and data_value columns
    rows = get_daily_data(username)
    
    # Close the database connection
    conn.close()
    
    # Separate the fetched data into two lists
    dates = [row[1] for row in rows]
    data_values = [row[2] for row in rows]
    
    # Convert the lists to NumPy arrays
    dates_array = np.array(dates)
    data_values_array = np.array(data_values)
    
    return dates_array, data_values_array