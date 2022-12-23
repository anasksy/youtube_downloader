# Importing necessary libraries
import youtube_dl
import os


# https://www.youtube.com/watch?v=QTBWTZF7Nv0
# https://www.youtube.com/watch?v=S3Dpfyc15qQ
# https://www.youtube.com/watch?v=QC8iQqtG0hg
# Function to download video/audio of a YouTube video
def download_media(option):
    # Set the download options
    ydl_options = {}
    if option == 'v':
        ydl_options['format'] = 'bestvideo[ext=mp4]/best[ext=mp4]/best'
    elif option == 'a':
        ydl_options['format'] = 'bestaudio/best'
    else:
        print("Invalid choice. Exiting.")
        exit()

    # Prompt the user for the URL of the video to download
    url = input("Enter the URL of the video to download: ")

    # Download the video or audio
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])


# Function to move downloaded videos to a new folder
def move_media(option):
    if option == 'v':
        if not os.path.exists('videos'):
            os.makedirs('videos')
        filename = os.listdir()[0]
        destination = './videos/' + filename
        i = 1
        # Check if the file already exists in the destination directory
        while os.path.exists(destination):
            # If it does, add a number to the file name and try again
            filename = f"{os.path.splitext(filename)[0]} ({i}){os.path.splitext(filename)[1]}"
            destination = './videos/' + filename
            i += 1
        # If the file doesn't already exist, move it to the destination directory
        os.rename(os.listdir()[0], destination)
    elif option == 'a':
        if not os.path.exists('audios'):
            os.makedirs('audios')
        filename = os.listdir()[0]
        destination = './audios/' + filename
        i = 1
        # Check if the file already exists in the destination directory
        while os.path.exists(destination):
            # If it does, add a number to the file name and try again
            filename = f"{os.path.splitext(filename)[0]} ({i}){os.path.splitext(filename)[1]}"
            destination = './audios/' + filename
            i += 1
        # If the file doesn't already exist, move it to the destination directory
        os.rename(os.listdir()[0], destination)


# Prompt the user to choose between video and audio
user_option = input("Enter 'v' for video or 'a' for audio: ")

# Call the download_media() function to download video/audio of a yt video
download_media(user_option)

# Call the move_videos() function to move the downloaded files to the videos/audio folder
move_media(user_option)
