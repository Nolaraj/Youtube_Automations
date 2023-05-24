import pyautogui
from time import sleep
import os
from tkinter import Tk, filedialog

#Install Pyautogui, opencv_python, pillow and tkinter packages

timer_a=2
max_image_wait = 5
print(f'Swiftly open the browser window showing required icons')
sleep(timer_a)


#Extract Folder path from the dialog box
def folder_path(title="Enter the file path"):
    root = Tk()             # pointing root to Tk() to use it as Tk() in program.
    root.withdraw()         # Hides small tkinter window.
    root.title()
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    # root.attributes()
    open_file = filedialog.askdirectory(title = title) #,filetypes = (("Excel files", ".xlsx .xls"),))   # Returns opened path as str
    return open_file
icons_file = folder_path()
os.chdir(icons_file)


def image_checkpoint_return_location(image, confidence = 0.5):
    try:
        location = pyautogui.locateOnScreen(image, confidence=confidence) #For Confidence to be used in Code pip install opencv-python is needed
        if location is not None:
            return (location)
        else:
            print(f'{image} position is None during runtime')
            return (location)
    except:
        print(f'{image} is not available in the screen during runtime, So Scrolling Down')
        return("Scroll Down")




def Wait_Until_Image_Appears_and_Click(image, confidence = 0.5):
    wait = 1
    while image_checkpoint_return_location(image) is None and wait <= max_image_wait:
        sleep(1)
        wait+=1
    pyautogui.click(image_checkpoint_return_location(image, confidence))

def Sleep_Until_Image_Disappears(image):
    while image_checkpoint_return_location(image) != None:
        sleep(1)



while image_checkpoint_return_location('rows_per_page.png', 0.9) == None:
    # Wait_Until_Image_Appears_and_Click('edit_draft.png', 0.96)pnolaraj@gmail.com
    sleep(1)

    pyautogui.click(image_checkpoint_return_location('private.png', 0.9))

    Wait_Until_Image_Appears_and_Click('share_privately.png')
    # Wait_Until_Image_Appears_and_Click('text_box.png')
    pyautogui.write("pnolaraj@gmail.com")


    Wait_Until_Image_Appears_and_Click('notify.png', 0.95)


    Wait_Until_Image_Appears_and_Click('done.png', 0.9)

    Wait_Until_Image_Appears_and_Click('save.png', 0.95)


    Wait_Until_Image_Appears_and_Click('rover.png',0.8 )


    for i  in range(0, 10):
        pyautogui.scroll(-10)

    sleep(6)





