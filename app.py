from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.form['text']
    target_language = request.form['language']

    translated_text = translate_text(text_to_translate, target_language)

    return render_template('index.html', original_text=text_to_translate, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
