import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

def select_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    image_path.set(file_path)

def extract_text():
    # Get the image file path
    file_path = image_path.get()

    if file_path:
        try:
            # Open the image file
            image = Image.open(file_path)

            # Convert the image to grayscale
            image = image.convert('L')

            # Use pytesseract to extract text from the image
            text = pytesseract.image_to_string(image)

            # Save the extracted text to a file
            save_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                     filetypes=[('Text Files', '*.txt')])
            if save_path:
                with open(save_path, 'w') as file:
                    file.write(text)
                status_label.config(text='Text saved to file successfully!')
            else:
                status_label.config(text='Text was not saved.')
        except Exception as e:
            status_label.config(text='An error occurred: ' + str(e))
    else:
        status_label.config(text='No image selected.')

# Create the main window
window = tk.Tk()
window.title('Image to Text Converter')

# Create a label for displaying the selected image path
image_path = tk.StringVar()
image_path_label = tk.Label(window, textvariable=image_path)
image_path_label.pack(pady=10)

# Create a button to select an image
select_button = tk.Button(window, text='Select Image', command=select_image)
select_button.pack(pady=10)

# Create a button to extract text from the selected image
extract_button = tk.Button(window, text='Extract Text', command=extract_text)
extract_button.pack(pady=10)

# Create a label for displaying the status
status_label = tk.Label(window, text='')
status_label.pack(pady=10)

# Start the main loop
window.mainloop()
