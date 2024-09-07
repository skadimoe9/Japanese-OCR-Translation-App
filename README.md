
# Japanese Translation App

This is an app that uses PaddleOCR to read images and translate Japanese text detected in the image into English.

## Overview

This readme provides an explanation of the necessary functions used in the app and how to use them, whether you run the app or use the functions separately.

## Requirements

Before using the app, install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

This command will install all the necessary packages used in the app.

## Features

1. Translation from Japanese to English.
2. Tracking the number of Japanese characters translated per account, displayed in a bar graph format.
3. Ability to either upload an image for translation or capture an image directly.
4. Deletion of all files used by the end of the session.
5. Option to save the image with translated text overlaid.
6. User registration and login.

---

# OCR Program (`ocr.py`)

This file processes images to extract, translate, and annotate Japanese text. It includes functions for OCR, tokenization, and drawing translated text on images.

## Functions Overview

### 1. `process_image(image_path)`

**Purpose:**  
Processes an input image, extracts Japanese text using OCR, tokenizes the text, and translates it into English.

**How to use:**

```python
your_image_path = './data/w.jpg'
df = process_image('your_image_path')
print(df)
```

The function returns a pandas DataFrame containing:
- `Box`: Bounding boxes of detected text.
- `Japanese`: Original Japanese text.
- `Translated`: Translated text in English.
- `Tokens`: Tokenized Japanese words.
- `Romaji`: Romanized versions of the words.
- `Translated_Tokens`: Translated tokens in English.

### 2. `draw_translated_text(image_path, df)`

**Purpose:**  
Draws the translated text onto the original image and saves it.

**How to use:**

```python
output_image_path = draw_translated_text('your_image_path', df)
print(f"Image saved at {output_image_path}")
```

- `image_path`: The original image file.
- `df`: DataFrame from `process_image()` containing the text to be added.
- The function saves the image with the translated text and returns the path to the saved image.

### 3. `delete_saved_image(file_path)`

**Purpose:**  
Deletes the specified image file.

**How to use:**

```python
delete_saved_image('your_image_path')
```

---

# File Handling and Image Processing Tool (`file_handling.py`)

This file includes functions for selecting image files, copying files, capturing pictures, creating bar graphs, and managing stored files. It also supports fetching data for graphing from a database.

## Functions Overview

### 1. `select_image_file()`

**Purpose:**  
Opens a file dialog for the user to select an image file (JPG, JPEG, PNG, or JFIF).

**How to use:**

```python
selected_file = select_image_file()
if selected_file != 400:
    print(f"Selected file: {selected_file}")
```

### 2. `copy_file(source_path, destination_path)`

**Purpose:**  
Copies a file from the source path to the destination path.

**How to use:**

```python
copy_file('path/to/source.jpg', 'path/to/destination.jpg')
```

### 3. `capture_picture()`

**Purpose:**  
Captures a picture using the default camera, displays the live feed, and saves the image when 'c' is pressed.

**How to use:**

```python
image_path = capture_picture()
if image_path:
    print(f"Picture saved as {image_path}")
```

### 4. `create_bar_graph(x, y)`

**Purpose:**  
Creates a bar graph from the provided data and saves it as an image file.

**How to use:**

```python
x = ['Date1', 'Date2', 'Date3']
y = [10, 20, 15]
create_bar_graph(x, y)
```

### 5. `delete_file()`

**Purpose:**  
Deletes files inside the `data`, `graph`, and `out_image` directories.

**How to use:**

```python
delete_file()
```

### 6. `fetch_graphing_data(username)`

**Purpose:**  
Fetches daily graphing data for the specified username from the SQLite database.

**How to use:**

```python
dates, values = fetch_graphing_data('username')
print(dates, values)
```

---

# User Authentication and Database Management Tool (`server.py`)

This file handles user registration, login, and management of daily data using SQLite and sockets.

## Functions Overview

### 1. `register(username, password)`

**Purpose:**  
Registers a new user by hashing their password and storing the username and hashed password in the SQLite database.

**How to use:**

```python
status = register('username', 'password')
if status:
    print("Registration successful")
else:
    print("Registration failed")
```

### 2. `login(username, password)`

**Purpose:**  
Verifies the user's credentials by comparing the hashed password stored in the database with the provided password.

**How to use:**

```python
status, user_id = login('username', 'password')
if status:
    print(f"Login successful. User ID: {user_id}")
else:
    print("Login failed")
```

### 3. `update_daily_data(username, data_date, data_value)`

**Purpose:**  
Updates the user's daily data by either inserting a new record or adding the new data to the existing record in the `daily_data` table.

**How to use:**

```python
status = update_daily_data('username', '2024-09-07', 50.0)
if status:
    print("Daily data updated")
else:
    print("Update failed")
```

### 4. `get_daily_data(username)`

**Purpose:**  
Fetches daily data for the specified user, returning the username, date, and data value.

**How to use:**

```python
data = get_daily_data('username')
print(data)
```

---

# Data Logging and Character Counting Tool (`datalog.py`)

This file processes the output from OCR, counts characters, and logs daily data. It interacts with other modules such as `ocr.py`, `file_handling.py`, and `server.py` for various functionalities.

## Functions Overview

### 1. `separate_and_count_characters(df)`

**Purpose:**  
Separates each character from the Japanese text and counts the total number of characters, including the successfully translated ones.

**How to use:**

```python
df = process_image('path_to_image.jpg')
chara_count, timestamp = separate_and_count_characters(df)
print(f"Character Count: {chara_count}, Timestamp: {timestamp}")
```

- `df`: A pandas DataFrame containing the OCR results, including Japanese text and translated text.
- Returns the total number of characters and the current timestamp.

### Integration with Other Modules

- `ocr.py`: The `process_image()` and `draw_translated_text()` functions are imported to process images and extract the text.
- `file_handling.py`: The `create_bar_graph()` function is used to create visual representations of the data.
- `server.py`: The `update_daily_data()` function is used to log the daily data into the SQLite database.

### Example Usage

1. **Process an image and count characters:**

```python
df = process_image('image_path.jpg')
chara_count, timestamp = separate_and_count_characters(df)
```

2. **Update daily data:**

```python
update_daily_data('username', timestamp, chara_count)
```

3. **Create a bar graph from the data:**

```python
x, y = fetch_graphing_data('username')
create_bar_graph(x, y)
```


# Main Backend Operations (`mainbackend.py`)

This file coordinates the backend processes such as user login, image selection, OCR translation, character counting, and graph creation. It ties together functionalities from various modules like `ocr.py`, `file_handling.py`, `server.py`, and `datalog.py`.

## Functions Overview

### 1. `pick_image_and_run_ocr(username)`

**Purpose:**  
Allows a user to pick an image file, run the OCR process, and display the translation results along with a character count and bar graph.

**How to use:**
```python
saved_path = pick_image_and_run_ocr('username')
```
- Returns the path to the saved image with translated text.

### 2. `save_image_decision(choice, saved_path)`

**Purpose:**  
Prompts the user with a decision to either save or delete the processed image file based on the user's input.

**How to use:**
```python
save_image_decision(1, saved_path)  # 1 to save, 0 to delete
```

### 3. `login_and_load_profile(username, password)`

**Purpose:**  
Handles user login, and if successful, loads the user's profile and displays their data in a bar graph.

**How to use:**
```python
status, user_id = login_and_load_profile('username', 'password')
if status:
    print(f"Login successful. User ID: {user_id}")
```

### 4. `capture_camera_ocr(username)`

**Purpose:**  
Captures an image from the camera, runs the OCR process, and displays the translation results along with character count and a bar graph.

**How to use:**
```python
saved_path = capture_camera_ocr('username')
```

---


# Contributions

### 1. Fadhli Ammar Taqiyuddin Hakim  
Worked on the Backend with the following tasks:
- Handled the process of overlaying text onto images using the `Pillow` library in the `draw_translated_text()` function in `ocr.py`.
- Managed the saving and deletion of files from the OCR process.
- Created more modular functions in `mainbackend.py` to facilitate easier integration with the Frontend.
- Developed data logging and character separation for generating graphs.
- Implemented the process of fetching data from the database to be used in graphs.
- Enhanced the login system functionality to ease its integration with the GUI.
- Developed the process for selecting image files from the user’s PC in `file_handling.py`.

### 2. Stanislaus David Aurelian  
Worked on the Frontend with the following tasks:
- Developed a comprehensive GUI for the app.
- Integrated Backend functions into the GUI created by the Frontend, particularly in `mainbackend.py`.
- Handled error management during the integration of files.

### 3. Dicky Osmond Sieliewangi  
Worked on the Backend with the following tasks:
- Created the database and database manipulation processes in `server.py`.
- Developed the key function `process_image()` in `ocr.py`, which serves as one of the main initiators responsible for OCR and Japanese text translation.
- Built several functions for file handling in `file_handling.py`.
- Assisted in the development of `mainbackend.py`.
