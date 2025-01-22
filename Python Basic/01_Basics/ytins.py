import yt_dlp
def download_video(video_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'outtmpl': 'D:/Videos/random.mp4', 
        'merge_output_format': 'mp4',  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except Exception as e:
            print(f"Error: {e}")

# Example usage
video_url = input("Enter the link of the YouTube video: ")
download_video(video_url)




# from pytube import YouTube

# link = input("Enter the link of the video: ")
# yt = YouTube(link)

# downloader = yt.streams.get_highest_resolution()
# print("Downloading...")

# downloader.download(filename="video.mp4")
# print("Downloaded successfully!") 