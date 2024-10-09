from customtkinter import *
import json,time
import yt_dlp

videosPATH = '~/Desktop/videos/'

def mainapp():
    root = CTk()
    root.title("Downloader")
    root.minsize(height = 800,width = 700)

    main = CTkFrame(root,height = 760,width = 660,corner_radius=25)
    main.place(relx = 0.5,rely = 0.5, anchor = CENTER)

    CTkLabel(main,text = "yt Downloader",font = ('comfortaa',40,'bold')).place(relx = .5,rely = .065,anchor='center')

    frame = CTkFrame(main,height = 650,width = 640,corner_radius=25)
    frame.place(relx = 0.5,rely = 0.56, anchor = CENTER)

    link = CTkEntry(frame,placeholder_text="Enter link",height=50,width=560,corner_radius=30)
    link.place(relx = .5,rely = .1,anchor='center')

    tabview = CTkTabview(frame,width = 620,height = 540,corner_radius=25)
    tabview.place(relx = 0.5,rely = 0.567,anchor = CENTER)

    audio = tabview.add("Audio")
    video = tabview.add("Video")

    def download(link,frmt,res):
        yt_opts3 = {
            'verbose': True,
            'extract_audio': True,
            'format': 'bestaudio',
            'outtmpl': '%(title)s.mp3'
        }

        with yt_dlp.YoutubeDL() as video:
            info_dict = video.extract_info(link, download = True)
            video_title = info_dict['title']
            print(video_title)
            video.download(link)    
            print("Successfully Downloaded - see local folder on Google Colab")



    def run0(ytlink):
        with yt_dlp.YoutubeDL() as ydl:
                '''info = ydl.extract_info(ytlink, download=False)
                print(type(info),ytlink)
                with open ('data.json','w') as file:
                    json.dump(info,file)'''
                download(ytlink,frmt='mp4',res=1080)





    
    
    CTkButton(frame,text='Dnlod',command=lambda:run0(link.get())).place(relx = .8,rely = 0.567,anchor = CENTER)


  

    root.mainloop()

if __name__ == '__main__':
    set_appearance_mode('dark')
    set_default_color_theme('color theme.json')
    deactivate_automatic_dpi_awareness()

    mainapp()