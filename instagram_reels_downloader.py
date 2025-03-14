<<<<<<< HEAD
import instaloader

def download_reel(reel_url):
    loader = instaloader.Instaloader()
    try:
        shortcode = reel_url.split('/')[-2]  # Extract shortcode from URL
        loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target="Instagram_Reels")
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    reel_url = input("Enter Instagram reel URL: ")
    download_reel(reel_url)
=======
import instaloader

def download_reel(reel_url):
    loader = instaloader.Instaloader()
    try:
        shortcode = reel_url.split('/')[-2]  # Extract shortcode from URL
        loader.download_post(instaloader.Post.from_shortcode(loader.context, shortcode), target="Instagram_Reels")
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    reel_url = input("Enter Instagram reel URL: ")
    download_reel(reel_url)
>>>>>>> 985d5032247e56e7b1fe74b8cd8eddf8e7487784
