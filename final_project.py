import librosa
import IPython.display as ipd
import subprocess
from scipy.io.wavfile import write


print(format('.............This is a program used for beat detection................','^40'))

#reading of video and taking some temmporary variables

pathl = input("enter the path of the location of a file where the action is stored and executed\nLike   C:\\\\users\\\\rajesh\\\\file_name          \nIt should always be in the above format:")

path_video = input("enter the location of the video file which has to be processed \nNote that the file ends with .mp4\nEXAMPLE      C:\\\\users\\\\rajesh\\\\file_name\\\\video_name.mp4      :")
path_audio = pathl + '\\audio.wav'
path_videot = pathl + '\\muted_video.mov'

subprocess.call(['ffmpeg','-i',path_video,'-c:v','copy','-an',path_videot])
subprocess.call(['ffmpeg','-i',path_video,'-c:v','copy',path_audio])


path = path_audio

#reading the audio

array, sample_rate = librosa.load(path)

#finding the beat location

bpm , beat_locations = librosa.beat.beat_track(y = array , sr = sample_rate)
#print(bpm)
#print(beat_locations)

#applying clicks in the beat locations

clicks = librosa.clicks(frames = beat_locations, sr=sample_rate, length=len(array))

#producing the clicks_applyed audio (this works in jupyter notebook)

ipd.Audio(array+clicks,rate=sample_rate)

#if not jupyter notebook this will give output

write(path,sample_rate,array+clicks)
print()

#reading the input video path

path_v = path_videot
path_v1 = pathl + '\\tempo_video.mov'
subprocess.call(['ffmpeg','-i',path_v,'-c:v','copy','-an',path_v1])


pathf = pathl + '\\final_output1.mov'

subprocess.call(['ffmpeg', '-i' ,path_v1, '-i' , path , '-c:v', 'copy', '-c:a', 'copy', pathf])

print ('process done you will find the video in the location that you gave by the name final_output1.mov')




