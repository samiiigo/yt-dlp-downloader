# Import neccessary libraries
from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
import io

# Define function to fetch images from url and exception handling
def display_image_from_url(url):
   root = tk.Tk()
   root.title("Displaying Images from URL in Tkinter")
   root.geometry("700x400")
   try:
      with urllib.request.urlopen(url) as u:
         raw_data = u.read()
   except Exception as e:
      print(f"Error fetching image: {e}")
      return

   try:
      image = Image.open(io.BytesIO(raw_data))
      photo = ImageTk.PhotoImage(image)
   except Exception as e:
      print(f"Error opening image: {e}")
      return
# creating labels and Run the Tkinter event loop 
   
   label = tk.Label(root, image=photo)
   label.pack()
   root.mainloop()

# Example usage
display_image_from_url("https://i.ytimg.com/vi/kfsKda_lNWs/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAcv-25xm9D1FgjAVEyKbTBzvGP2g")