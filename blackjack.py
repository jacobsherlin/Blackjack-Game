# Name: Jacob Sherlin
# Text-based blackjack game.
import random
#deck
class Deck:
	# deck methods
	def __init__(self):
		self.cards = [(suit, rank) for suit in ['♥', '♦', '♣', '♠']
					for rank in range(1, 14)]
	# get length of deck
	def __len__(self):
		return len(self.cards)
	# shuffle deck
	def shuffle(self):
		random.shuffle(self.cards)
	# move card to top of deck
	def top(self, card):
		if card in self.cards:
			self.cards.remove(card)
			self.cards.insert(0, card)
	# move card to bottom of deck
	def bottom(self, card):
		if card in self.cards:
			self.cards.remove(card)
			self.cards.insert(self.__len__(), card)
	# move card to any position of deck
	def move(self, card, position):
		if card in self.cards and position < self.__len__():
			self.cards.insert(position, card)
	# delete card from deck
	def deleteCard(self, card):
		self.cards.remove(card)
	# draw top from deck
	def draw(self):
		card = self.cards[0]
		self.cards.remove(card)
		return card

#hand class
class Hand:
	# hand methods
	def __init__(self):
		self.cards = [] * 5 # default size
	# get length of hand
	def __len__(self):
		return len(self.cards)
	# add card
	def addCard(self, card):
		self.cards.append(card)
	# delete card from hand
	def deleteCard(self, card):
		self.cards.remove(card)
	# get sum of hand
	def getSum(self):
		total = []
		# convert face cards and aces
		for i in range(self.__len__()):
			suit, rank = self.cards[i]
			if rank > 10:
				rank = 10
			total.append(rank)
		finalTotal = sum(total)
		# calculate aces
		for i in range(self.__len__()):
			suit, rank = self.cards[i]
			if rank == 1:
				if sum(total) + 10 <= 21:
					finalTotal+=10
				break
					
		return finalTotal

#card class
class Card:
	# card methods
	def __init__(self, card):
		self.card = card
	# print card
	def printCard(self):
		suit, rank = self.card
		rank = str(rank)
		if rank == '1':
			rank = 'A'
		if rank == '11':
			rank = 'J'
		if rank == '12':
			rank = 'Q'
		if rank == '13':
			rank = 'K'
		if rank != '10':
			print('---------')
			print(f'| {rank}     |')
			print('|       |')
			print(f'|   {suit}   |')
			print('|       |')
			print(f'|     {rank} |')
			print('---------')
		elif rank == '10':
			print('---------')
			print(f'|{rank}     |')
			print('|       |')
			print(f'|   {suit}   |')
			print('|       |')
			print(f'|    {rank} |')
			print('---------')
		else:
			print('No card is selected')
	# get value of card
	def getValue(self):
		suit, rank = self.card
		if rank > 10:
			return 10
		else:
			return rank
	# add two cards
	def __add__(self, other):
		suit, rank = self.card
		suit2, rank2 = other
		return (rank + rank2)
	# add two cards from right to left
	def __radd__(self, other):
		suit, rank = self.card
		suit2, rank2 = other
		return (rank2 + rank)

# game function			
def game():
	for i in range(30):
		print()
	deck = Deck()
	dealerHand = Hand()
	playerHand = Hand()
	playerSum = 0
	dealerSum = 0
	# shuffle deck
	deck.shuffle()
	# dealer draws
	card = Card(deck.draw())
	dealerHand.addCard(card.card)
	card = Card(deck.draw())
	dealerHand.addCard(card.card)
	dealerSum = dealerHand.getSum()
	# output dealer's cards
	print("Dealer's Hand:")
	# if dealer draws 21
	if dealerSum == 21:
		for i in range(2):
			card = Card(dealerHand.cards[i])
			card.printCard()
		print(f"Dealer's sum: {dealerSum}. Blackjack! You lose")
		return # end program
	card = Card(dealerHand.cards[0])
	card.printCard()
	#print face down card
	print('---------')
	print('| ?     |')
	print('|       |')
	print('|   ?   |')
	print('|       |')
	print('|     ? |')
	print('---------')
	# player draws
	card = Card(deck.draw())
	playerHand.addCard(card.card)
	card = Card(deck.draw())
	playerHand.addCard(card.card)
	# output player's hand
	print('\n\n')
	print("Player's Hand:")
	for i in range(playerHand.__len__()):
		card = Card(playerHand.cards[i])
		card.printCard()
	playerSum = playerHand.getSum()
	if playerSum == 21:
		print("Blackjack!")
	print(f"Player's Sum: {playerSum}\n")
	# gameplay 
	choice = input('Stand or Hit? ')
	print()
	while choice == 'hit' or choice == 'Hit': 
		# player draws
		card = Card(deck.draw())
		playerHand.addCard(card.card)
		# output player's hand
		print()
		print("Player's Hand: ")
		for i in range(playerHand.__len__()):
			card = Card(playerHand.cards[i])
			card.printCard()
		playerSum = playerHand.getSum()
		if playerSum == 21:
			print("Blackjack!")
		# if player exceeds 21
		if playerSum > 21:
			print(f"Player busts: {playerSum}. You Lose.")
			return # end program
		# else
		print(f"Player's Sum: {playerSum}\n")
		# ask for hit 
		choice = input('Stand or Hit? ')
	# if dealer total is greater than 17
	if dealerSum >= 17:
		print()
		print("Dealer's Hand: ")
		for i in range(dealerHand.__len__()):
			card = Card(dealerHand.cards[i])
			card.printCard()
		dealerSum = dealerHand.getSum()
		print(f"Dealer's Sum: {dealerSum}\n")
	#dealer loop
	while dealerSum < 17:
		#dealer draws
		card = Card(deck.draw())
		dealerHand.addCard(card.card)
		# output dealer's cards
		print()
		print("Dealer's Hand: ")
		for i in range(dealerHand.__len__()):
			card = Card(dealerHand.cards[i])
			card.printCard()
		dealerSum = dealerHand.getSum()
		# if dealer exceeds 21
		if dealerSum > 21:
			print(f"Dealer busts: {dealerSum}. You win!")
			return # end program
		if dealerSum == 21:
			print("Blackjack!")
		# else
		print(f"Dealer's Sum: {dealerSum}\n")
		#determine outcome

	if dealerSum == playerSum:
		print("It's a tie!")
	
	elif dealerSum == 21:
		print("You lose.")

	elif playerSum == 21:
		print("You win!")

	elif dealerSum > playerSum:
		print('You lose.')

		
	else:
		print('You win!')
		
	return
	#end of program

# main function
def main():
	choice = True
	while choice == True:
		game()
		choice = input("\nPlay again? (Y \ N)\n")
		if choice == 'Y' or choice == 'y':
			choice = True
		else:
			choice = False
	print("\nThanks for playing!")

if __name__ == "__main__":
    main()
