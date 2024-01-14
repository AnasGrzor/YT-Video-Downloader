
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog

def get_available_qualities(url):
    # Get the list of available formats and their details
    process = subprocess.Popen(['yt-dlp', '-F', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    # Decode the output to a string and split by lines
    output_lines = out.decode().split('\n')

    # Define the desired video qualities
    desired_qualities = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p']

    # Filter out lines that contain the desired quality and format information
    quality_lines = [line for line in output_lines if any(quality in line for quality in desired_qualities)]

    # Return the list of available qualities
    return quality_lines


def download_video():
    # Initialize the Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    while True:
        # Prompt the user for the video URL
        url = input("Enter the YouTube video URL (or type 'exit' to quit): ")

        # Check if the user wants to exit the program
        if url.lower() == 'exit':
            break

        # Get the available qualities for the video
        qualities = get_available_qualities(url)

        # Check if there are available qualities
        if not qualities:
            print("No available qualities found, try again.")
            continue

        # Display the available qualities and prompt the user to select one
        quality = simpledialog.askstring("Quality Selection", "Available qualities:\n" + "\n".join(qualities) + "\nEnter the format code of the desired quality:")

        # Check if the user has entered a quality
        if not quality:
            print("No quality selected, try again.")
            continue

        # Open the file explorer dialog to select the directory
        save_path = filedialog.askdirectory(title="Select the directory where you want to save the video")

        # Check if the user has selected a directory
        if not save_path:
            print("No directory selected, try again.")
            continue

        # Command to download the video using yt-dlp with the selected quality and original title as the filename
        command = ['yt-dlp', '-o', f'{save_path}/%(title)s.%(ext)s', '-f', (f"{quality}+bestaudio/best"), '--merge-output-format', 'mkv', url]

        # Run the command
        subprocess.run(command)

if __name__ == "__main__":
    download_video()
