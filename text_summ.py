from transformers import T5Tokenizer, T5ForConditionalGeneration,pipeline
import PyPDF2


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text


pdf_path = "C:/farewell/rabbit.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)


def generate_summary_and_sentiment(input_text):
    # Sentiment analysis pipeline
    sentiment_analyzer = pipeline('sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')
    

    # Analyze sentiment of the input text
    sentiment_result = sentiment_analyzer(input_text)[0]
    sentiment_label = sentiment_result['label']
    sentiment_score = sentiment_result['score']

    # Choose a Text Summarization Model
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Tokenize the input text
    tokenized_input = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate Summarization
    summary_ids = model.generate(tokenized_input, max_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary, sentiment_label, sentiment_score




pdf_path = "C:/farewell/rabbit.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
summary, sentiment_label, sentiment_score = generate_summary_and_sentiment(pdf_text)
#print(f"Summary: {summary}\nSentiment: {sentiment_label} (Score: {sentiment_score:.2f})")




from gtts import gTTS
import os
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=summary, lang=language, slow=False)

# Saving the converted audio in a file
tts.save("output.mp3")

# Playing the converted file
os.system("start output.mp3")