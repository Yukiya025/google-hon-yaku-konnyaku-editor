import eel
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

eel.init("web")

@eel.expose
def add_popup(input_words):
    sentences = sent_tokenize(input_words)

    output_words = ""
    for ru in sentences:
        url = "https://script.google.com/macros/s/AKfycbyMd"\
              "s6HiWhtHjnK0FiAYlhcKSa4sns6UIt-iZH1jS9-rCbyK"\
              "p07/exec?text=" + ru + "&source=ru&target=ja"

        ja = requests.get(url).text
        output_words += f'<span title="{ja}">{ru}</span> '

    output_words = output_words.rstrip()

    eel.show(output_words)

web_app_options = {
    "mode": "chrome-app",
    "chromeFlags": [
        "--window-size=500,600"
    ]
}

eel.start("main.html", options=web_app_options)