from file_handling import select_image_file, create_bar_graph, fetch_graphing_data, copy_file, capture_picture
from ocr import process_image, draw_translated_text, delete_saved_image 
from datalog import separate_and_count_characters
from server import login, register, update_daily_data
import time

# Buat button untuk milih gambar yang mau ditranslate
def pick_image_and_run_ocr(username): # butuh username dari login page
    image_path = select_image_file()
    while True:
        if type(image_path) == str:
            break
        if type(image_path) == int:
            print("No image selected.")
            break
    if type(image_path) == int:
        return None

    temp_path = "./data/temp_image.jpg" 
    copy_file(image_path,temp_path)
    df2 = process_image(temp_path)

    saved_path = draw_translated_text(temp_path, df2) 
    image_to_show = "./out_image/showfinalimage.jpg" # Ini ditampilin di hasil
    copy_file(saved_path, image_to_show)

    characters, tstamps = separate_and_count_characters(df2)

    try: 
        update_daily_data(username, tstamps, characters)
    except:
        print("Error updating data.")
    
    x, y = fetch_graphing_data(username)
    create_bar_graph(x, y) # function ini bakal ngeshow grafik juga, bikin box buat ini
    print("Translation succeed")
    
    return saved_path

def save_image_decision(choice, saved_path): 
    # ini buat pop up mau ngesave atau gak, ini harus jalan setelah pick image/capture image and run ocr
    # choice itu berdasarkan lu klik ya atau gak di pop up screennya
    if choice:
        print("Picture saved.")
    if saved_path == None:
        print("No image saved.")
    if choice == 0 and saved_path != None:
        delete_saved_image(saved_path)

def login_and_load_profile(username, password): # buat login
    status, user_id = login(username, password)
    if status:
        print('Login success')
        x, y = fetch_graphing_data(username)
        create_bar_graph(x, y) # function ini bakal ngesave/show grafik user saat ini
        return True, user_id
    else:
        print('Login failed')
        return False, None

def capture_camera_ocr(username): 
    # dijalanin bareng save image, urutannya ini dluan, buat capture image dan run ocr
    # tolong tambahin teks "click 'c' to capture image and 'q' to quit" di UI
    image_path = capture_picture()
    if image_path == False:
        return None 
    try:
        image_path = capture_picture() 
        df2 = process_image(image_path)

        saved_path = draw_translated_text(image_path, df2) # function ini bakal ngeshow gambar bikin box buat ini
        image_to_show = "./out_image/showfinalimage.jpg"
        copy_file(saved_path, image_to_show)

        characters, tstamps = separate_and_count_characters(df2)

        try: 
            update_daily_data(username, tstamps, characters)
        except:
            print("Error updating data.")
        
        x, y = fetch_graphing_data(username)
        create_bar_graph(x, y) # function ini bakal ngeshow grafik juga bikin box buat ini
        print("Translation succeed")
        return saved_path
    
    except TypeError :
        print("No character detected")
        return None 


# Tolong buat ketika klik tombol buat pick image dan ngerun OCR, nanti setelah function itu selesai 
# bakal ada pop up yang nanya mau save gambar atau nggak, kalo iya nanti choice = 1, dan kalau gak 
# nanti choice = 0, lalu jalanin save_image_decision. Nah saved_path di function saved_image_decision 
# itu asalnya dari return function pick_image_and_run_ocr 

# Example
# pathfiles = capture_camera_ocr("admin1")
# pathfiles = pick_image_and_run_ocr("admin1")
# save_image_decision(0, pathfiles)
