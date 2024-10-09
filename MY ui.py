from tkinter.font import BOLD
from customtkinter import * # type: ignore
import json,time
import yt_dlp
from PIL import Image
import urllib.request
import io

set_appearance_mode('dark')
set_default_color_theme('asssets\\color theme.json')
deactivate_automatic_dpi_awareness()

curinfo = {}

root = CTk()
root.title("Downloader")
root.minsize(height = 800,width = 700)

main = CTkFrame(root,height = 760,width = 660,corner_radius=25)
main.place(relx = 0.5,rely = 0.5, anchor = CENTER)

CTkLabel(main,text = "Video Downloader",font = ('Montserrat Medium',40,'bold')).place(relx = .5,rely = .065,anchor='center')

frame = CTkFrame(main,height = 650,width = 640,corner_radius=25)
frame.place(relx = 0.5,rely = 0.56, anchor = CENTER)

def void():
    entry.configure(state='normal')
    entry.delete(0,'end')
    void_ = CTkFrame(frame,width = 620,height = 540,corner_radius=25)
    void_.place(relx = 0.5,rely = 0.567,anchor = CENTER)
    void_res = CTkLabel(void_,height=80,width=200,text='Please input valid link.',text_color='red')
    void_res.place(relx = 0.5,rely = 0.5,anchor = CENTER)
    frame.after(2500,lambda:void_.destroy())

def select(i):
    selframe = CTkFrame(frame,width = 620,height = 540,corner_radius=25)
    selframe.place(relx = 0.5,rely = 0.567, anchor = CENTER)

    #-------------THUMBNAIL-----------------
    try:
        with urllib.request.urlopen(i[2]) as u:
            raw_data = u.read()
    except Exception as e:
        print(f"Error fetching image: {e}")
        return
    
    try:
        thumbimage = CTkImage(Image.open(io.BytesIO(raw_data)),size = (196,110))
    except Exception as e:
        print(f"Error opening image: {e}")

    thumb = CTkLabel(selframe,text = '', image = thumbimage)
    thumb.place(relx = 0.07,rely = 0.07)
    thumb._image = thumbimage

    CTkLabel(selframe,text=i[1],font=('comfortaa',17,'bold')).place(relx = 0.45,rely = 0.1)
    
    def v_download(link,res,frmt):
        yt_opts = {
            'verbose': True,
            'extract_audio': True,
            "video_ext": frmt,
            "resolution": res,
            'outtmpl': 'C:\\Users\\samyo\\Downloads\\%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(yt_opts) as video:
            video.download(link)

    vid_card = CTkFrame(selframe,height = 135,width = 540,corner_radius=25)
    vid_card.place(relx = 0.5,rely = 0.48, anchor = CENTER)

    CTkLabel(vid_card,text='Video',font=('Montserrat',15)).place(relx = 0.08,rely = 0.1, anchor = CENTER)

    CTkOptionMenu(vid_card,)
    v_optionmenu = CTkOptionMenu(vid_card, values=["4k", "1440p","1`080p","720p","480p"])
    v_optionmenu.place(relx = 0.27,rely = 0.5, anchor = CENTER)
    v_optionmenu.set("1080p")

    v_optionmenu_ = CTkOptionMenu(vid_card, values=["mp4",'webm'])
    v_optionmenu_.place(relx = 0.6,rely = 0.5, anchor = CENTER)
    v_optionmenu_.set("mp4")

    #radiobutton_1 = CTkRadioButton(vid_card, text="No Audio",value=1)
    #radiobutton_1.place(relx = 0.4,rely = 0.7, anchor = CENTER)

    img_dw = CTkImage(Image.open('asssets\\dw.png'),size = (55,55))
    img_dw0 = CTkImage(Image.open('asssets\\dw0.png'),size = (55,55))

    b_dw0 = CTkLabel(vid_card,text = '',fg_color='#333333',image=img_dw)
    b_dw0.place(relx = 0.88,rely = 0.5,anchor = CENTER)
    b_dw0.bind("<Button-1>",lambda x:v_download(i[0],a_optionmenu.get(),a_optionmenu_.get()))

    def onenter(a):a.configure(image=img_dw0)
    def onleave(a):a.configure(image=img_dw)

    b_dw0.bind('<Enter>',lambda x:onenter(b_dw0));b_dw0.bind('<Leave>',lambda x: onleave(b_dw0))

    def a_download(link,res,frmt):
        yt_opts = {
            'verbose': True,
            "resolution": "audio only",
            "format_note": res,
            'format': 'bestaudio',
            'outtmpl': f'C:\\Users\\samyo\\Downloads\\%(title)s.{frmt}'
        }
        with yt_dlp.YoutubeDL(yt_opts) as audio:
                audio.download(link)

    aud_card = CTkFrame(selframe,height = 135,width = 540,corner_radius=25)
    aud_card.place(relx = 0.5,rely = 0.789, anchor = CENTER)

    a_optionmenu = CTkOptionMenu(aud_card, values=["Default", "Medium","Low",])
    a_optionmenu.place(relx = 0.27,rely = 0.5, anchor = CENTER)
    a_optionmenu.set("Normal")

    a_optionmenu_ = CTkOptionMenu(aud_card, values=["mp3",'m4a'])
    a_optionmenu_.place(relx = 0.6,rely = 0.5, anchor = CENTER)
    a_optionmenu_.set("mp3")

    b_dw1 = CTkLabel(aud_card,text = '',fg_color='#333333',image=img_dw)
    b_dw1.place(relx = 0.88,rely = 0.5,anchor = CENTER)
    b_dw1.bind("<Button-1>",lambda x:a_download(i[0],a_optionmenu.get(),a_optionmenu_.get()))
    b_dw1.bind('<Enter>',lambda x:onenter(b_dw1));b_dw1.bind('<Leave>',lambda x: onleave(b_dw1))
    
def progres(event=None):
    url = entry.get()
    if len(url) < 10:
        void()
    else:
        try:
            ydl_opts = {'format': 'best',
                        'noplaylist': True,
                        'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                curinfo = ydl.extract_info(url, download=False)
            #with open('video_info.json') as f:
            #    curinfo = json.load(f)
            title = curinfo['title'] # type: ignore
            if len(title)>30:
                title = title[:30]+'...'
            thumbnail = curinfo['thumbnail'] # type: ignore
            duration = curinfo['duration'] # type: ignore
            select([url,title,thumbnail,duration,'https://i.ytimg.com/vi/kfsKda_lNWs/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAcv-25xm9D1FgjAVEyKbTBzvGP2g'])

        except:
            void()
            
            
entry = CTkEntry(frame,placeholder_text="Enter link",height=50,width=580,corner_radius=30)
entry.place(relx = .5,rely = .075,anchor='center')
entry.insert(0,'https://youtu.be/kfsKda_lNWs?si=AcDb5nxEf1ezK-Ii')#-------------------------------------------------AUTO-LINK--------


entry.bind('<Return>',progres)
#entry.bind('<Control-v>',progres)

null = CTkFrame(frame,width = 620,height = 540,corner_radius=25)
null.place(relx = 0.5,rely = 0.567,anchor = CENTER)

nullpic = CTkImage(Image.open('asssets\\null.png'),size = (512,512))

nullpic1 = CTkLabel(null,text = '', image = nullpic)
nullpic1.place(relx = 0.5,rely = 0.5,anchor = CENTER)
nullpic1._image = nullpic1



















def progress_hook(progress):
    tot=progress['total_bytes']
    if progress['status'] == 'downloading':
        progres.set(progress['percent'])
    elif progress['status'] == 'error':
        progres.set('Error')
    elif progress['status'] == 'finished':
        progres.set('Finished')

def progress(event=None):
    url = entry.get()
    if len(url) < 10:
        void()
    else:
        entry.configure(state='readonly')
        prog = CTkFrame(frame,width = 620,height = 540,corner_radius=25)
        prog.place(relx = 0.5,rely = 0.567,anchor = CENTER)
        progres = CTkProgressBar(prog,height=60,width=200,mode='indeterminate',corner_radius=35,orientation='horizontal')
        progres.place(relx = 0.5,rely = 0.5,anchor = CENTER)
        progres.start()
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            root.update_idletasks()
            curinfo = ydl.extract_info(url, download=False)
        with open('data.json','w') as f:
            json.dump(curinfo,f)
            print('done')
        root.after(3000,lambda:progres.stop())

root.after(50,lambda:entry.focus_set())

root.mainloop()