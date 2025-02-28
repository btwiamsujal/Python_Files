import yt_dlp
import os

def download_video(video_url, download_folder="D:/Videos/"):
    print("\n🚀 Downloading...")

    # Create folder if it doesn't exist
    os.makedirs(download_folder, exist_ok=True)

    # Download options
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # Save with original title
        'merge_output_format': 'mp4',  
        'noplaylist': True,  # Download only a single video, not playlists
        'quiet': False,  # Show progress info
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print("✅ Download completed successfully!\n")
        except Exception as e:
            print(f"❌ Error: {e}")

# Main program loop
if __name__ == "__main__":
    while True:
        video_url = input("🔗 Enter video link (or type 'exit' to quit): ").strip()
        if video_url.lower() == "exit":
            print("👋 Exiting program.")
            break
        download_video(video_url)

