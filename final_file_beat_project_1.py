import librosa
import IPython.display as ipd
import subprocess
from scipy.io.wavfile import write

print(format('.............This is a program used for beat detection................','^40'))

#reading of video and taking some temmporary variables

path_video = input('enter the path of video file')

path_audio = input('give a path for storing audio \\ mind it that u give everything in double slash \nand the audio location for storage is in .wav form:')

path_videot = input('give the path for video \\ mind it that u give everything in double slash \nnote that u give the location of the video file in .mov:')


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

#asking for a temporary variable

path_v1 = input('enter a path as a temporary path for a video ending with .mov \\ \n note to add double slash')

subprocess.call(['ffmpeg','-i',path_v,'-c:v','copy','-an',path_v1])

#taking a final location for output

pathf = input('enter a path where u want ur beat added video to be added in ur pc in .mov \\ \nnote to add double slash')

#merging of beat added audio with video

subprocess.call(['ffmpeg', '-i' ,path_v1, '-i' , path , '-c:v', 'copy', '-c:a', 'copy', pathf])

print ('process done you will find the location of the modified video file in ur entered location')




