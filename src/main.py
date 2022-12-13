# Importing libraries
import youtube_dl


def download_video(url):
    # Create a YouTube Downloader object
    ydl = youtube_dl.YoutubeDL()

    # Download the video
    with ydl:
        ydl.download([url])


# Enter the URL of the YouTube video you want to download
video_url = input("Enter a youtube url: ")

# Call the download_video() function with the user-specified URL
download_video(video_url)