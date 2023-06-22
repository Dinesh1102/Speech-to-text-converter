import whisper
import gradio as gr

model = whisper.load_model('large')

def speech(x):
    text = model.transcribe(x)
    return text['text']

style = """
        .gradio-container {
            font-family: 'IBM Plex Sans', sans-serif;
        }
        .gr-button {
            color: white;
            border-color: black;
            background: black;
        }
        input[type='range'] {
            accent-color: black;
        }
        .dark input[type='range'] {
            accent-color: #dfdfdf;
        }
        .container {
            max-width: 730px;
            margin: auto;
            padding-top: 1.5rem;
        }
     
        .details:hover {
            text-decoration: underline;
        }
        .gr-button {
            white-space: nowrap;
        }
        .gr-button:focus {
            border-color: rgb(147 197 253 / var(--tw-border-opacity));
            outline: none;
            box-shadow: var(--tw-ring-offset-shadow), var(--tw-ring-shadow), var(--tw-shadow, 0 0 #0000);
            --tw-border-opacity: 1;
            --tw-ring-offset-shadow: var(--tw-ring-inset) 0 0 0 var(--tw-ring-offset-width) var(--tw-ring-offset-color);
            --tw-ring-shadow: var(--tw-ring-inset) 0 0 0 calc(3px var(--tw-ring-offset-width)) var(--tw-ring-color);
            --tw-ring-color: rgb(191 219 254 / var(--tw-ring-opacity));
            --tw-ring-opacity: .5;
        }
        .footer {
            margin-bottom: 45px;
            margin-top: 35px;
            text-align: center;
            border-bottom: 1px solid #e5e5e5;
        }
        .footer>p {
            font-size: .8rem;
            display: inline-block;
            padding: 0 10px;
            transform: translateY(10px);
            background: white;
        }
        .dark .footer {
            border-color: #303030;
        }
        .dark .footer>p {
            background: #0b0f19;
        }
        .prompt h4{
            margin: 1.25em 0 .25em 0;
            font-weight: bold;
            font-size: 115%;
        }
        .animate-spin {
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }
        #share-btn-container {
            display: flex; margin-top: 1.5rem !important; padding-left: 0.5rem !important; padding-right: 0.5rem !important; background-color: #000000; justify-content: center; align-items: center; border-radius: 9999px !important; width: 13rem;
        }
        #share-btn {
            all: initial; color: #ffffff;font-weight: 600; cursor:pointer; font-family: 'IBM Plex Sans', sans-serif; margin-left: 0.5rem !important; padding-top: 0.25rem !important; padding-bottom: 0.25rem !important;
        }
        #share-btn * {
            all: unset;
        }
"""

with gr.Blocks(css = style) as demo:
    with gr.Tab("Audio File"):
        with gr.Row().style(equal_height=True):
            audio_input1 = gr.Audio(label="Audio File", type="filepath")
            text_output1 = gr.Textbox(label="Transcription", show_label=False)
        file_button = gr.Button("Transcribe")
    with gr.Tab("Record"):
        with gr.Row().style(equal_height=True):
            audio_input2 = gr.Audio(label="Input Audio", source="microphone", type="filepath")
            text_output2 = gr.Textbox(label="Transcription", show_label=False)
        rec_button = gr.Button("Transcribe")
    gr.HTML('''
        <div class="footer">
            <p>Model by <a href="https://github.com/openai/whisper" style="text-decoration: underline;" target="_blank">OpenAI</a></p>
        </div>
        ''')

    file_button.click(speech, inputs=audio_input1, outputs=text_output1)
    rec_button.click(speech, inputs=audio_input2, outputs=text_output2)

demo.launch()