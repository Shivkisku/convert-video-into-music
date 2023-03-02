
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import requests

# Create the GUI window
root = tk.Tk()
root.title("Video to MP3 Converter")

# Define function to handle the file selection
def choose_file():
    file_path = filedialog.askopenfilename(title="Select Video File",
                                           filetypes=(("MP4 files", "*.mp4"), ("AVI files", "*.avi"),
                                                      ("MKV files", "*.mkv"), ("All files", "*.*")))
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Define function to handle the conversion
def convert():
    # Get the input file path
    input_path = file_entry.get()

    # Check if a file is selected
    if not input_path:
        messagebox.showerror("Error", "Please select a video file.")
        return

    # Create a moviepy video object
    video = mp.VideoFileClip(input_path)

    # Set the output file path
    output_path = input_path.replace(".mp4", ".mp3").replace(".avi", ".mp3").replace(".mkv", ".mp3")

    # Convert the video to audio and save the output file
    audio = video.audio
    audio.write_audiofile(output_path)

    # Show success message
    messagebox.showinfo("Success", "Conversion completed successfully.")

    # Offer to download the converted file
    download = messagebox.askyesno("Download", "Do you want to download the converted file?")
    if download:
        response = requests.get(output_path)
        open(output_path, 'wb').write(response.content)

# Create the GUI elements
file_label = tk.Label(root, text="Select Video File:")
file_entry = tk.Entry(root, width=50)
file_button = tk.Button(root, text="Browse", command=choose_file)
convert_button = tk.Button(root, text="Convert to MP3", command=convert)

# Add the elements to the window
file_label.pack()
file_entry.pack()
file_button.pack()
convert_button.pack()

# Run the GUI
root.mainloop()
