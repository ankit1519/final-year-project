# Text Summarization Project

This project allows users to upload PDF files, extract text, generate summaries, perform sentiment analysis, and convert summaries to audio.

## Table of Contents

- [Project Structure]
- [Introduction]
- [Features]
- [Installation]
- [Usage]
- [Dependencies]

## Project Structure


```plaintext
TextSummarizationSystem/
|-- app.py
|-- text_summ.py
|-- templates/
|   |-- index.html
|-- static/
|-- uploads/
|-- venv/
```


## Introduction

This project is designed to perform text summarization on uploaded PDF files. Users can extract text, generate summaries, analyze sentiment, and listen to audio summaries.

## Features

- PDF text extraction
- Text summarization
- Sentiment analysis
- Audio summary generation

## Installation

Clone the repository and set up the virtual environment.

```bash
git clone https://github.com/ankit1519/final-year-project
cd final-year-project
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate  # On Windows

```
## Usage
Run the Flask application to launch the web interface.
-python app.py
Visit http://127.0.0.1:5000/ in your web browser and follow the instructions for uploading PDF files and processing them.

## Dependencies

- [Flask](https://flask.palletsprojects.com/): A web framework for building web applications with Python.
- [Transformers](https://huggingface.co/transformers/): A library for natural language processing with pre-trained models.
- [gtts](https://pypi.org/project/gTTS/): Google Text-to-Speech API wrapper for converting text to speech.

Make sure to have Python and pip installed on your system before following the installation steps. The virtual environment ensures that your project's dependencies are isolated from the system-wide Python installation.
