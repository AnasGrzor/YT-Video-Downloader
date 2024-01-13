#!/usr/bin/env python3
import subprocess
import tkinter as tk
from tkinter import filedialog

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

        # Open the file explorer dialog to select the directory
        save_path = filedialog.askdirectory(title="Select the directory where you want to save the video")

        # Check if the user has selected a directory
        if not save_path:
            print("No directory selected, try again.")
            continue

        # Command to download the highest quality video using yt-dlp with the original title as the filename
        command = ['yt-dlp', '-o', f'{save_path}/%(title)s.%(ext)s', '-f', 'bestvideo+bestaudio/best', '--merge-output-format', 'mkv', url]

        # Run the command
        subprocess.run(command)

if __name__ == "__main__":
    download_video()
