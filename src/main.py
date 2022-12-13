# Importing necessary libraries
import youtube_dl
import os
import curses

# Function to download a video from YouTube
def download_video(url):
    # Create a YouTube Downloader object
    ydl = youtube_dl.YoutubeDL()

    # Download the video
    with ydl:
        ydl.download([url])

# Function to move downloaded videos to a new folder
def move_videos():
    # Check if the "videos" folder already exists
    if not os.path.exists("videos"):
        # If not, create the folder
        os.makedirs("videos")

    # Move all downloaded videos to the "videos" folder
    for file in os.listdir():
        if file.endswith(".mp4") or file.endswith(".webm"):
            os.rename(file, "videos/" + file)

# Enter the URL of the YouTube video you want to download
video_url = input("Enter a youtube url: ")

# Call the download_video() function with the user-specified URL
download_video(video_url)

# Call the move_videos() function to move the downloaded videos to the "videos" folder
move_videos()