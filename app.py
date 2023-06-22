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
            audio_input1 = gr.Audio(label="Audio File", type="filepath")
            text_output1 = gr.Textbox(label="Transcribed text", show_label=True)
        file_button = gr.Button("Transcribe")
    with gr.Tab("Record"):
        with gr.Row().style(equal_height=True):
            audio_input2 = gr.Audio(label="Input Audio", source="microphone", type="filepath")
            text_output2 = gr.Textbox(label="Transcribed text", show_label=True)
        rec_button = gr.Button("Run")
    gr.HTML('''
        <div class="footer">
            <p>Model by <a href="https://github.com/openai/whisper" style="text-decoration: underline;" target="_blank">OpenAI</a></p>
        </div>
        ''')

    file_button.click(speech, inputs=audio_input1, outputs=text_output1)
    rec_button.click(speech, inputs=audio_input2, outputs=text_output2)

demo.launch()