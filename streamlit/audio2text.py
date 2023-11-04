import assemblyai as aai
import sounddevice as sd
from scipy.io.wavfile import write


def extract_audio():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file
    # Replace with your API token
    aai.settings.api_key = f"#"

    # URL of the file to transcribe
    FILE_URL = "output.wav"

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)

    return transcript.text
