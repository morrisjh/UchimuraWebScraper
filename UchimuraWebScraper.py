import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.aozora.gr.jp/cards/000034/files/233_43563.html')#Kanzō Uchimura's "Denmarukukoku no Hanashi" - this can be replaced with other html files from Aozora Bunko.
response.encoding = 'shift_jis' #Encodes the text to shift_jis to match Aozora Bunko's encoding.

soup = BeautifulSoup(response.text, 'html.parser') #Parser.

contents = soup.find_all('body') #Searches the body part of the text.

for content in contents:
    title = content.find(class_='title').get_text().replace('\n', '') #Finds the title.
    subtitle = content.find(class_='subtitle').get_text().replace('\n', '') #Finds the subtitle. Some texts do not have a subtitle, so this may return an error if run on a text without a subtitle.
    author = content.find(class_='author').get_text().replace('\n', '') #Finds the author.
    text = content.find(class_='main_text').get_text().replace('\n', '') #Finds the text.

f = open('aozoratext.txt', 'a+') #Creates a .txt file called "aozoratext.txt" or adds to this file if it already exists.
f.write(('Title: ') + title + ("\n")) #Prints the title in the .txt file.
f.write(('Subtitle: ') + subtitle + ("\n")) #Prints the subtitle in the .txt file.
f.write(('Author: ') + author + ("\n")) #Prints the author's name in the .txt file.
f.write(('Text: ') + text + ("\n")) #Prints the text in the .txt file. 