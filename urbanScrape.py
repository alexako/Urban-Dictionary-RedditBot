
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

BASE_URL = "http://www.urbandictionary.com"


def get_definition_link(key_word):
    word_url = BASE_URL + "/define.php?term="+key_word
    response = requests.get(word_url)
    html = urlopen(response.url).read()
    soup = BeautifulSoup(html, "lxml")
    return response.url

def read_definition(word_url):
    html = urlopen(word_url)
    soup = BeautifulSoup(html,"lxml")
    try:
        definition = soup.find("div","meaning").text
        word = soup.find("a","word").string
        example = soup.find("div","example").text
    except:
        definition = " isn't defined :-("
        word = "NULL"
        example = "NULL"
    return [word,definition,example]






