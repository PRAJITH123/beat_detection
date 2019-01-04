import librosa
import IPython.display as ipd
import subprocess
from scipy.io.wavfile import write
from pydub import AudioSegment

print(format('.............This is a program used for beat detection................','^40'))

x = int(input(print('enter 1 if u are giving us a mp3 file,enter 2 if giving us a wav form of audio')))
'''if x == 1
    path = input(print('enter the file location'))
    input = AudioSegment.from_mp3(path)
    input.export()'''

#elif x==2
path = input(print('enter the audio file location'))

#reading the audio

array, sample_rate = librosa.load(path)

#finding the beat location

bpm , beat_locations = librosa.beat.beat_track(y = array , sr = sample_rate)
#print(bpm)
#print(beat_locations)

#applying clicks in the beat locations
clicks = librosa.clicks(frames = beat_locations, sr=sample_rate, length=len(array))

#producing the clicks_applyed audio
ipd.Audio(array+clicks,rate=sample_rate)
#help(write)
path2 = 'C:\\x\\man3.wav'
write(path2,sample_rate,array+clicks)
print()
#reading the input video path
path_v = input('Enter the path where the video is present')

subprocess.call(['ffmpeg','-i',path_v,'-c:v','copy','-an','C:\\x\\output1.mov'])

#merging the beat applied audio with the muted audio

subprocess.call(['ffmpeg', '-i' ,'C:\\x\\output1.mov', '-i' , path2 , '-c:v', 'copy', '-c:a', 'copy', 'C:\\x\\output_final2.mov' ])
print ('done')




