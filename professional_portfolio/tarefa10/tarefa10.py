# Write a Python script that takes a PDF file and converts it into speech.

import PyPDF2
from gtts import gTTS
import os

def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
    return text

def convert_text_to_speech(text, output_file='output.mp3', language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    return output_file

def main():
    pdf_path = 'professional_portfolio/tarefa10/exemplo.pdf'
    output_file = 'professional_portfolio/tarefa10/output.mp3'

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Convert text to speech
    convert_text_to_speech(text, output_file)

    # Play the generated speech
    os.system(f'start {output_file}')

if __name__ == "__main__":
    main()
