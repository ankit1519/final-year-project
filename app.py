# app.py
from flask import Flask, render_template, request, jsonify
from text_summ import extract_text_from_pdf, generate_summary_and_sentiment
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    pdf_file = request.files['pdf']
    if pdf_file and pdf_file.filename.endswith('.pdf'):
        # Extract text from PDF
        pdf_path = 'uploads/' + pdf_file.filename
        pdf_file.save(pdf_path)
        pdf_text = extract_text_from_pdf(pdf_path)

        # Generate summary and sentiment analysis
        summary, sentiment_label, sentiment_score = generate_summary_and_sentiment(pdf_text)

        # Convert summary to audio
        audio_path = 'static/summary_audio.mp3'
        tts = gTTS(text=summary, lang='en', slow=False)
        tts.save(audio_path)

        # Provide results to the frontend
        result = {
            'pdfText': pdf_text,
            'summary': summary,
            'sentimentLabel': sentiment_label,
            'sentimentScore': sentiment_score,
            'audioPath': audio_path
        }
        return jsonify(result)
    else:
        return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.run(debug=True)
