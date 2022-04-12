
import wave
import speech_recognition as sr
import io
from pydub import AudioSegment



class AudioToText:
    """speech recognition"""
    def __init__(self, filepath):
        self.filepath = filepath

    def WavToIo(self):
        """converting Wav to binary"""
        self.wavfile = open(self.filepath, 'rb').read()
        self.iofile = io.BytesIO(self.wavfile)
        print("Conversion to Binary complete\n")
        return self.iofile

    def IoToWav(self, filename):
        """name and save binary file into wav format"""
        # place ffmpeg.exe fie in same directory e.g \AppData\Local\Programs\Python\Python39-32\Scripts

        self.filename = filename
        self.filename = self.filename + ".wav"
        # pydub.AudioSegment.ffmpeg = "C:/ffmpeg/bin/"
        self.audio = AudioSegment.from_raw(self.iofile, sample_width=2, frame_rate=44100, channels=2).export(
            self.filename, format='wav')
        self.iofile = io.BytesIO(self.wavfile) # return iofile to binary
        print(f"\n{self.filename} file have been saved...")

    def IoToText(self):
        """converting binary file like object to text"""
        try:
            filename = sr.AudioFile(self.iofile)
            with filename as source:
                print("Processing Binary please wait ...\n")
                r = sr.Recognizer()
                audio = r.record(source)
                text = r.recognize_google(audio)
            self.iofile = io.BytesIO(self.wavfile)  # return iofile to binary
            print(text)
        except ValueError:
            print("Warning: Binary file type not supportive !!!\n")
            pass



    def WavToText(self):
        """convert wav to text without binary file like object"""
        try:
            filename = sr.AudioFile(self.filepath)
            with filename as source:
                print("Processing Wav please wait ...\n")
                r = sr.Recognizer()
                audio = r.record(source)
                text = r.recognize_google(audio)
            print(text)
        except ValueError:
            print("Warning: Wav Audio file type not supportive !!!\n")
            pass






myaudio = 'python_reference-apps_python-voice-recognition_harvard.wav'
#myaudio = "Harvard.wav"
audio = AudioToText(myaudio)
audio.WavToIo()
audio.IoToText()
audio.WavToText()
#audio.IoToWav("music03")


