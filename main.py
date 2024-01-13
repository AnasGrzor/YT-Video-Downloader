#!/usr/bin/env python3
import subprocess


def download_video():
    while True:
      # Prompt the user for the video URL
      url = input("Enter the YouTube video URL (or type 'exit' to quit): ")

      # Check if the user wants to exit
      if url.lower() == 'exit':
        print("Exiting...")
        break

      # Command to download the highest quality video using yt-dlp with the original title as the filename
      command = ['yt-dlp', '-o', '%(title)s.%(ext)s', '-f', 'bestvideo+bestaudio/best', '--merge-output-format', 'mkv', url]

      # Run the command
      subprocess.run(command)

if __name__ == "__main__":
    download_video()
