import librosa
import IPython.display as ipd
import subprocess
from scipy.io.wavfile import write

print(format('.............This is a program used for beat detection................','^40'))

x = int(input('enter 1 if u are giving us a mp3 file,enter 2 if giving us a wav form of audio'))
if x == 1:
    path= input('enter the file location')
    #path=input("give a storage path for our audio ending the file name with wav")
    subprocess.call(['ffmpeg','-i',path,'-c: a','copy',path])

if x==2:
    path = input('enter the audio file location')

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

#help(write)
path3 = input(print('enter a temporary file location for audio ending in .wav'))
write(path3,sample_rate,array+clicks)
print()

#reading the input video path

path_v = input('Enter the path where the video is present')
path_v1 = input('enter a path as a temporary path for a video ending with .mov')

subprocess.call(['ffmpeg','-i',path_v,'-c:v','copy','-an',path_v1])

#merging the beat applied audio with the muted audio
pathf = input('enter a path where u want ur beat added video to be added in ur pc in .mov')
subprocess.call(['ffmpeg', '-i' ,path_v1, '-i' , path3 , '-c:v', 'copy', '-c:a', 'copy', pathf ])
print ('done')




