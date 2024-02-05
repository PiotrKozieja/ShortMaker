import DataSelector
import VoiceGenerator
import time
import ShortMaker
import TitleFormat
Data = DataSelector.select_data('Fakty.csv')
Data1 = Data[0]
Data2 = Data[1]
print("Data selected---->"+Data[0]+"--------------")
VoiceGenerator.get_voice(Data1)
time.sleep(3)  
VoiceGenerator.get_voice(Data2)
print("Voice generated ------------------------")
audio_path1 = TitleFormat.get_file_title(Data1)
audio_path2 = TitleFormat.get_file_title(Data2)


###########make_short(input_path, output_path,text1,text2,audio_path1,audio_path2,audio_path3,Channel name):
ShortMaker.make_short('Sample1.mp4','SM_6.mp4',Data1,Data2,audio_path1,audio_path2,'better-day.mp3',"@BezKontrowersji")