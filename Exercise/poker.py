# 扑克牌案例

import random


class Poker:
    def __init__(self):
        self.cards = []
        self.suits = ['♠', '♣', '♦', '♥']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in self.suits:
            for value in self.values:
                self.cards.append(suit + value)

    def shuffle(self):
        random.shuffle(self.cards)

    def __getitem__(self, index):
        return self.cards[index]


poker = Poker()
print(poker.cards)
# 输出第一张牌
print(poker[0])
# 输出第2到第5张牌
print(poker[1:5])
# 洗牌
poker.shuffle()
print(poker.cards)
