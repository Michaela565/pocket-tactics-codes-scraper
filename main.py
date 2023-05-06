from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier

toast = ToastNotifier()
url = "https://www.pockettactics.com/genshin-impact/codes"
textBeforeCodes = "Here are all the new Genshin Impact codes:"
# Text that is right before the list of codes, "Here are all the new Genshin Impact codes:" or
# "Here are all the active Honkai Star Rail codes:"
game = "Genshin Impact" # Name of the game

def getResponse(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

def getCodes(html, beforeCodes):
    for classs in html.find_all('div', attrs={'class': 'entry-content'}):
        allParagraphs = classs.find_all('p')
        for text in allParagraphs:
            textNoLineEnds = text.text.replace("\n", "")
            if textNoLineEnds == beforeCodes:
                print(text.next_sibling.text)
                return text.next_sibling.text

def main():
    doc = getResponse(url)
    barStr = str(getCodes(doc, textBeforeCodes))
    barHeader = "Current {} codes!".format(game)
    toast.show_toast(barHeader, barStr, icon_path= "favicon.ico", duration=10)

if __name__ == '__main__':
    main()



