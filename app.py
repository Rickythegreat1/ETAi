from flask import Flask, request, jsonify, render_template
from pdfminer.high_level import extract_text
import pandas as pd
import docx
from pptx import Presentation
from openpyxl import load_workbook
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from io import StringIO

app = Flask(__name__)

def parse_pdf(file_path):
    print("Parsing PDF:", file_path)
    text = ''
    resource_manager = PDFResourceManager()
    fake_file_handle = StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(file_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # Cleanup
    converter.close()
    fake_file_handle.close()

    print("Parsed text:", text)
    return text

def get_response(user_input):
    print("User Input:", user_input)
    if "parse pdf" in user_input:
        file_path = user_input.split("parse pdf")[1].strip()
        print("PDF file path:", file_path)
        parsed_text = parse_pdf(file_path)
        print("Parsed text:", parsed_text)
        return parsed_text
    else:
        # Implement the rest of your chatbot logic
        pass

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form.get('user_input', '')
    response = get_response(user_input)
    print("Response:", response)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
