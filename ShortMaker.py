from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip
import TextFormater
def make_short(input_path, output_path,text1,text2,audio_path1,audio_path2,audio_path3,Chname):
    text1 = TextFormater.format_text(text1,25) #second value is max char in line
    text2 = TextFormater.format_text(text2,29)
    video_clip = VideoFileClip(input_path)
    
    audio_clip1 = AudioFileClip(audio_path1)
    audio_clip2 = AudioFileClip(audio_path2)
    audio_clip3 = AudioFileClip(audio_path3)

    audio_clip1 = audio_clip1.volumex(2.0)  
    audio_clip2 = audio_clip2.volumex(2.0)  
    audio_clip3 = audio_clip3.volumex(0.3)  

    #
    text_clip1 = TextClip(text1, fontsize=60, color='rgb(255,192,203)', bg_color='none', size=(video_clip.w, 120), stroke_color='rgb(255,20,147)', stroke_width=3)
    text_clip1 = text_clip1.set_position('center')  
    text_clip2 = TextClip("_", fontsize=1, color='black', bg_color='white', size=(video_clip.w, 200), stroke_color='rgb(255,20,147)', stroke_width=3)
    text_clip2 = text_clip2.set_position('center').set_opacity(.7)
    #
    text_clip3 = TextClip(Chname, fontsize=40, color='rgb(255,192,203)', bg_color='none', size=(video_clip.w, 50), stroke_color='rgb(255,20,147)', stroke_width=2)
    text_clip3 = text_clip3.set_position(('center', video_clip.h // 2 + 200))  
    
    text_clip4 = TextClip("_", fontsize=1, color='black', bg_color='white', size=(video_clip.w, 55), stroke_color='rgb(255,20,147)', stroke_width=2)
    text_clip4 = text_clip4.set_position(('center', video_clip.h // 2 + 200)).set_opacity(.7)
    #
    text_clip5 = TextClip(text2, fontsize=48, color='rgb(255,20,147)', bg_color='none', size=(video_clip.w, video_clip.h), stroke_color='rgb(255,20,147)')
    text_clip5 = text_clip5.set_position('center')  
    text_clip6 = TextClip("_", fontsize=1, color='black', bg_color='white', size=(video_clip.w, video_clip.h), stroke_color='rgb(255,20,147)', stroke_width=3)
    text_clip6 = text_clip6.set_position('center').set_opacity(.7)

    #clips_start
    start_time1 = 0
    start_time2 = audio_clip1.duration
    audio_clip2 = audio_clip2.set_start(start_time2)

    #clips_time
    duration1 = audio_clip1.duration
    duration2 = audio_clip2.duration
    audio_clip3 = audio_clip3.set_duration(duration1+duration2)

    text_clip1 = text_clip1.set_duration(duration1)
    text_clip2 = text_clip2.set_duration(duration1)

    text_clip3 = text_clip3.set_duration(duration1*2/3)
    text_clip4 = text_clip4.set_duration(duration1*2/3)

    text_clip5 = text_clip5.set_duration(duration2)
    text_clip6 = text_clip6.set_duration(duration2)

    
    #short time
    video_clip = video_clip.subclip(0,duration1+duration2)
    composite_audio = CompositeAudioClip([audio_clip1,audio_clip2,audio_clip3])
    video_with_text = CompositeVideoClip([video_clip, 

                                            text_clip2.set_start(start_time1),
                                            text_clip1.set_start(start_time1),

                                            text_clip4.set_start(duration1/3),
                                            text_clip3.set_start(duration1/3),
                                                                                        
                                            text_clip6.set_start(start_time2),
                                            text_clip5.set_start(start_time2),
                                            ])

    video_with_text = video_with_text.set_audio(composite_audio)
    video_with_text.write_videofile(output_path, codec='libx264', audio_codec='aac')
#if __name__ == "__main__":
#    text1 = "Harmonia Hormonalna"
#    text2 = "Zmiany hormonalne u kobiet mają znaczący wpływ nie tylko na cykl menstruacyjny, lecz także na ogólny stan emocjonalny. Hormony, takie jak estrogen i progesteron, pełnią kluczową rolę w regulacji nastroju, energii i zachowań, co sprawia, że harmonia hormonalna staje się fascynującym obszarem badań związanych z psychobiologią kobiecego organizmu."
#    audio_path1 = "C:\\Users\\Piotr\\Downloads\\Harmonia Hormonalna.mp3"
#    audio_path2 = "C:\\Users\\Piotr\\Downloads\\Zmiany hormonalne u .mp3"    
#    Chname = "@BezKontrowersji"
#    make_short('Sample1.mp4','ShortMakerVid.mp4',text1,text2,audio_path1,audio_path2,"@BezKontrowersji")