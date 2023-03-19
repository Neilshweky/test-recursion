from enum import Enum

class Color(Enum):
  RED = 1
  GREEN = 2
  PURPLE = 3

class Fill(Enum):
  EMPTY = 1
  STRIPED = 2
  SOLID = 3

class Shape(Enum):
  DIAMOND = 1
  OVAL = 2
  SQUIGGLE = 3

class Quantity(Enum):
  ONE = 1
  TWO = 2
  THREE = 3


class SetCard:

    def __init__(self, id, color, quantity, shape, fill):
        self.id = id
        self.color = color
        self.quantity = quantity
        self.shape = shape
        self.fill = fill

    def __str__(self):
      return self.id + ": [" + self.color.name + ", " + self.shape.name + ", " + self.fill.name + ", " + self.quantity.name + "]"

    @classmethod
    def cardForLink(cls, id, linkId):
      color = None
      fill = None
      shape = None
      quantity = None

      linkId = linkId - 1
      if linkId < 28:
        fill = Fill.SOLID
      elif linkId > 54:
        fill = Fill.EMPTY
      else:
        fill = Fill.STRIPED

      linkId = linkId % 27
      if linkId < 9:
        shape = Shape.SQUIGGLE
      elif linkId > 18:
        shape = Shape.OVAL
      else:
        shape = Shape.DIAMOND

      linkId = linkId % 9

      if linkId < 3:
        color = Color.RED
      elif linkId > 5:
        color = Color.GREEN
      else:
        color = Color.PURPLE

      linkId = (linkId % 3) + 1
      if linkId == 1:
        quantity = Quantity.ONE
      elif linkId == 2:
        quantity = Quantity.TWO
      else:
        quantity = Quantity.THREE

      return SetCard(id, color, quantity, shape, fill)

    # a class method called verify
    @classmethod
    def verify(cls, card1, card2, card3):
        # check if the cards are a set
        # return True if they are a set
        # return False if they are not a set
        pass



# This is old
    @classmethod
    def addUpAttributes(cls, attr, card1, card2, card3):
        # add up the attributes of the cards
        # return the sum
        colorSum = card1.color.value + card2.color.value + card3.color.value
        quantitySum = card1.quantity.value + card2.quantity.value + card3.quantity.value
        shapeSum = card1.shape.value + card2.shape.value + card3.shape.value
        fillSum = card1.fill.value + card2.fill.value + card3.fill.value

    @classmethod
    def validCombo(cls, sum):
       return sum == 3 or sum == 6 or sum == 12 or sum == 7

# This class represents a set board with 12 SetCards
class SetBoard:

  def __init__(self, board = None) -> None:
    if board is not None:
      self.board = board
    else:
      self.board = self.setupBoard()

  def setupBoard(self):
    # generate 12 cards
    # return the cards
    return [
      SetCard("1", Color.RED, Quantity.TWO, Shape.OVAL, Fill.SOLID),
      SetCard("2", Color.GREEN, Quantity.ONE, Shape.DIAMOND, Fill.EMPTY),
      SetCard("3", Color.RED, Quantity.ONE, Shape.DIAMOND, Fill.SOLID),
      SetCard("4", Color.GREEN, Quantity.ONE, Shape.SQUIGGLE, Fill.SOLID),
      SetCard("5", Color.RED, Quantity.THREE, Shape.SQUIGGLE, Fill.EMPTY),
      SetCard("6", Color.PURPLE, Quantity.TWO, Shape.OVAL, Fill.EMPTY),
      SetCard("7", Color.RED, Quantity.TWO, Shape.SQUIGGLE, Fill.SOLID),
      SetCard("8", Color.GREEN, Quantity.TWO, Shape.OVAL, Fill.STRIPED),
      SetCard("9", Color.PURPLE, Quantity.ONE, Shape.SQUIGGLE, Fill.EMPTY),
      SetCard("10", Color.PURPLE, Quantity.TWO, Shape.SQUIGGLE, Fill.STRIPED),
      SetCard("11", Color.PURPLE, Quantity.THREE, Shape.SQUIGGLE, Fill.SOLID),
      SetCard("12", Color.RED, Quantity.THREE, Shape.SQUIGGLE, Fill.SOLID),
    ]

  # This method should generate a list of card pairs
  def generatePairsOfCards(self):
    pairs = []
    for i in range(len(self.board)):
      for j in range(i,len(self.board)):
        if j != i:
          pairs.append([self.board[i], self.board[j]])
    return pairs

  # self.partition = {
  #   color: {
  #     shape: {
  #       fill: {
  #         quantity: {}
  #       }
  #     }
  #   }
  # }
  # self.partition[card.color][card.attribute][card.fill][card.quantity]
  def partitionBoard(self):
    self.partition = {}
    for card in self.board:
      if card.color not in self.partition:
        self.partition[card.color] = {}

      if card.shape not in self.partition[card.color]:
        self.partition[card.color][card.shape] = {}

      if card.fill not in self.partition[card.color][card.shape]:
        self.partition[card.color][card.shape][card.fill] = {}

      self.partition[card.color][card.shape][card.fill][card.quantity] = card
    return self.partition

  def findThirdCardForPair(self, pair):
    card1 = pair[0]
    card2 = pair[1]

    # generate the right color
    color = None
    fill = None
    shape = None
    quantity = None
    if card1.color == card2.color:
      color = card1.color
    else:
      color = self.otherAttribute(Color, card1.color, card2.color)

    if card1.fill == card2.fill:
      fill = card1.fill
    else:
      fill = self.otherAttribute(Fill, card1.fill, card2.fill)

    if card1.shape == card2.shape:
      shape = card1.shape
    else:
      shape = self.otherAttribute(Shape, card1.shape, card2.shape)

    if card1.quantity == card2.quantity:
      quantity = card1.quantity
    else:
      quantity = self.otherAttribute(Quantity, card1.quantity, card2.quantity)

    return self.cardExistsForAttributes(color, shape, fill, quantity)

  def otherAttribute(self, cls, attr1, attr2):
    return cls(6 - attr1.value - attr2.value)


  def cardExistsForAttributes(self, color, shape, fill, quantity):
    if self.partition.get(color) and \
       self.partition.get(color).get(shape) and \
       self.partition.get(color).get(shape).get(fill):
      return self.partition.get(color).get(shape).get(fill).get(quantity)
    return None

  # returns a list of 6 sets [card1, card2, card3]
  def getSets(self):
    pairs = self.generatePairsOfCards()
    self.partitionBoard()

    sets = []
    found = {}
    for pair in pairs:
      card3 = self.findThirdCardForPair(pair)
      if card3:
        ids = [pair[0].id, pair[1].id, card3.id]
        ids.sort()
        if ids[0] not in found or not found[ids[0]].get(ids[1]):
          sets.append([pair[0], pair[1], card3])


          row = {}
          if ids[0] in found:
            row = found[ids[0]]
          else:
            row = {}
          row[ids[1]] = True
          found[ids[0]] = row


    return sets

def __main__():
  import pprint
  board = SetBoard()
  print("\n".join(map(lambda x: x[0].id + ", " + x[1].id, board.generatePairsOfCards())))
  print(len(board.generatePairsOfCards()))
  pprint.pprint(board.partitionBoard())
  print(len(board.getSets()))
  sets = board.getSets()
  for set in sets:
    print(str(set[0]) + " ... " + str(set[1]) + " ... " + str(set[2]))