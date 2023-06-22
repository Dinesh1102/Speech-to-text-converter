from IPython.display import Audio, display
import whisper
display(Audio('audio.mp3', autoplay=True))
model = whisper.load_model('large')
pred = model.transcribe('audio.mp3')
print(pred['text'])