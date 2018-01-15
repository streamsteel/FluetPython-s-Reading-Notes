# -*- coding: UTF-8 -*-
import collections
from random import choice

#rank->点数  suit->花色
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck():
	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank,suit) for suit in self.suits
									  for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self,position):
		return self._cards[position]


#构建纸牌对象
beer_card = Card('7','diamonds')
print(beer_card)

#一叠牌数量
deck = FrenchDeck()
print (len(deck))

#抽取一张特定的牌
print (deck[0])
print (deck[-1])

#使用Python内置的 random.choice函数随机抽牌
print ('随机抽取：'),choice(deck)

#切片操作
print (deck[:3])
print (deck[12::13])

#排序操作
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	return rank_value * len(suit_value) + suit_value[card.suit]

#升序排序
for card in sorted(deck, key=spades_high):
	print(card)