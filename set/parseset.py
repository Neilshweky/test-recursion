from bs4 import BeautifulSoup
import requests

import re
# import classes from set.py
from set import SetCard, SetBoard


class SetParser:
  @classmethod
  def parseTodays(cls):
    print("Hello World!")
    url = "https://www.setgame.com/set/puzzle"

    r = requests.get(url)
    data = r.text

    soup = BeautifulSoup(data, "html.parser")
    # print(soup.prettify())

    cardDivs = soup("div", {"class": "set-card-td"})

    print(len(cardDivs))
    cards = []

    for cardDiv in cardDivs:
      # print(cardDiv.prettify())

      cardLink = cardDiv.find("a")
      cardImg = cardLink.find("img")

      link = cardImg['src']
      id = cardImg['class'][0][1:]

      p = re.compile("\/sites\/all\/modules\/setgame_set\/assets\/images\/new\/(\d+)\.png")
      result = p.search(link)
      linkId = result.group(1)
      # print(link + ": " + linkId + " " + id)

      cardObj = SetCard.cardForLink(id, int(linkId))

      print(cardObj)
      cards.append(cardObj)

    print(cards)
    board = SetBoard(cards)
    sets = board.getSets()
    for set in sets:
      print(str(set[0]) + " ... " + str(set[1]) + " ... " + str(set[2]))

    return sets