import instaloader

def download_instagram_video(url):
    loader = instaloader.Instaloader()
    try:
        # Login if you need to access private profiles
        # loader.interactive_login("your_username")

        post = instaloader.Post.from_shortcode(loader.context, url)
        loader.download_post(post, target="#{shortcode}")
        print("Video downloaded successfully.")
    except Exception as e: print(f"Error: {str(e)}")


with open('download.txt') as f:
        for i in f.readlines():
            try:download_instagram_video(i)
            except:print('FAILED')

  



