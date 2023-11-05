from PyPDF2 import PdfReader
from gtts import gTTS
import os

# Input PDF file
pdf_file = "index.pdf"  # Replace with the path to your PDF file

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to convert text to audio
def text_to_audio(text, output_file="output.mp3"):
    tts = gTTS(text)
    tts.save(output_file)
    return output_file

if __name__ == "__main__":
    # Extract text from the PDF
    pdf_text = extract_text_from_pdf(pdf_file)

    # Convert text to audio
    audio_file = text_to_audio(pdf_text)

    print(f"Text from PDF extracted and saved as {audio_file}")

    # Play the audio (you may need to install a suitable audio player)
    os.system(f"start {audio_file}")
