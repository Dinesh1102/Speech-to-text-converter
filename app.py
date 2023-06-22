import whisper
import gradio as gr

model = whisper.load_model('large')

def speech(x):
    text = model.transcribe(x)
    return text['text']


with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Speech to Text Converter!
    """)
    with gr.Tab("Audio File"):
        with gr.Row().style(equal_height=True):
            audio1 = gr.Audio(label="Audio File", type="filepath")
            text1 = gr.Textbox(label="Transcribed text", show_label=True)
        file_button = gr.Button("Run")
    with gr.Tab("Record"):
        with gr.Row().style(equal_height=True):
            audio2 = gr.Audio(label="Input Audio", source="microphone", type="filepath")
            text2 = gr.Textbox(label="Transcribed text", show_label=True)
        rec_button = gr.Button("Run")
    
    file_button.click(speech, inputs=audio1, outputs=text1)
    rec_button.click(speech, inputs=audio2, outputs=text2)

demo.launch()