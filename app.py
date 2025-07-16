import os
from dotenv import load_dotenv
import gradio as gr

load_dotenv()

MODEL     = os.getenv("MODEL")
API_TOKEN = os.getenv("API_TOKEN")
ENDPOINT  = os.getenv("ENDPOINT", "https://llm.nrp-nautilus.io/")

if not MODEL or not API_TOKEN:
    raise RuntimeError("Please set MODEL and API_TOKEN in your .env file.")

def main():
    interface = gr.load_chat(
        ENDPOINT,
        model=MODEL,
        token=API_TOKEN,
    )

    interface.launch(
        server_name="0.0.0.0",   # bind to all interfaces
        server_port=7860,        # or read from env
        inbrowser=True,          # auto-open your default browser
        share=False              # set to True if you want a public URL
    )

if __name__ == "__main__":
    main()
