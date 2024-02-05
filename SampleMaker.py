from moviepy.editor import VideoFileClip

def przyciecie_centralne(video_clip, docelowe_proporcje=(9, 16), max_czas=35):

    szerokosc, wysokosc = video_clip.size
    

    nowa_szerokosc = int(wysokosc * docelowe_proporcje[0] / docelowe_proporcje[1])
    nowe_wymiary = (nowa_szerokosc, wysokosc)
    
    x1 = (szerokosc - nowa_szerokosc) // 2
    y1 = 0

    x2 = x1 + nowa_szerokosc
    y2 = wysokosc

    video_przyciete = video_clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
    

    video_przyciete = video_przyciete.subclip(2, min(video_przyciete.duration, max_czas+2))
    
    return video_przyciete


video_clip = VideoFileClip("video4.mp4") #<-------input


video_przyciete = przyciecie_centralne(video_clip, docelowe_proporcje=(9, 16), max_czas=40)#<-- tu wpisywac


video_przyciete.write_videofile("Sample1.mp4", codec="libx264", audio_codec="aac", fps=60)
                                #output^

