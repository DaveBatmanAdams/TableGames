#this is the version that introduces the betting system. Was a lot harder than expected

import random
import time

money = 100

faces = ["king.", "queen.", "jack."]
 
#this is for the end of any hand, a module used to restart or exit the game
def new_hand(money):
	
	print "\n"	
	
	if money == 0:
		print "Looks like you're all outta cash..."
		print "You blew 100 bucks in a night? Whew. That's pretty hefty."
		print "Listen, I don't wanna be a downer or anything..."
		print "But you might, just possibly, have a massive gambling addiction."
		print "I can't be sure, but it's just a suggestion."
		time.sleep(5)
		print"."
		time.sleep(2)
		print"."
		time.sleep(2)
		print"."
		time.sleep(2)
		print "I'm just going to leave this number here with you."
		print "1-800-522-4700"
		print "This may or may not be a hotline for people with addictions."
		print "Gambling addictions."
		print "Take it as you will."
		print "Oh yeah, you also lost the game."
		exit()
		
	if money > 1000:
		print "After starting with $100 and making $%s from blackjack in a single night,"
		print "an enraged casino owner brings over a group of hardy, broud-shouldered"
		print "gentlemen who \"escort\" you to the parking lot. This is technically a game"
		print "over, sure, but with this one you get to feel like a winner. Nice."
		exit() 

			
	print "Would you like to play again?"
	play_again = raw_input ("? ")
#I know it looks like the variable and the words INside of it should be flipped, but this is actually the correct formatting!
	if play_again in {"Yes", "yes", "y", "Y", "Sure", "sounds good", "absolutely", "let\'s do it", "affirmative"} :
		initial_draw(money)
	elif play_again in {"No", "no", "N", "n", "nope", "nein", "never", "fuck off", "you're a shithead", "I'd rather not", "mayber later", "not really"}:
		print "Alright then, thanks for playing!"
		exit()
	else: 
		print "Speak English, Dork-a-tron"
		new_hand(money)
 
#this module is the actual start of the game, start here to follow the code chronologically
def initial_draw(money) :
 
	first_card = random.randint(1,11)
 	
 	print "You have %s dollars." % money
 	
	print "\n"
	
	print "How much money would you like to gamble?"
	
	try:
		bet = int(raw_input("? "))
	except ValueError:
		print "You need to type a whole number."
		initial_draw(money)
		
	print "You decide to put down %s dollars worth of chips." % bet

	if bet > money:
		print "Until you realise you only have %s dollars!" % money
		print "For real this time,"
		initial_draw(money)	
 
 	print "\n"
 	
	if first_card == 1:
		print "Your first card is an ace."
		print "\n" 
 
	if first_card == 2:
		print "Your first card is a two."
		print "\n" 
	
	if first_card == 3:
		print "Your first card is a three."
		print "\n" 
	
	if first_card == 4:
		print "Your first card is a four."
		print "\n" 
	
	if first_card == 5:
		print "Your first card is a five."
		print "\n" 
	
	if first_card == 6:
		print "Your first card is a six."
		print "\n" 
	
	if first_card == 7:
		print "Your first card is a seven."
		print "\n" 
	
	if first_card == 8:
		print "Your first card is an eight."
		print "\n" 
	
	if first_card == 9:
		print "Your first card is a nine."
		print "\n" 
	
	if first_card == 10:
		print "Your first card is a ten."
		print "\n" 
	
	if first_card == 11:
		print "Your first card is a %s" % random.choice(faces)
		print "\n" 
 
	second_card = random.randint(1, 11)
 
	if second_card == 1:
		print "Your second card is an ace."
		print "\n" 
 
	if second_card == 2:
		print "Your second card is a two."
		print "\n" 
	
	if second_card == 3:
		print "Your second card is a three."
		print "\n" 
	
	if second_card == 4:
		print "Your second card is a four."
		print "\n" 
	
	if second_card == 5:
		print "Your second card is a five."
		print "\n" 
	
	if second_card == 6:
		print "Your second card is a six."
		print "\n" 
	
	if second_card == 7:
		print "Your second card is a seven."
		print "\n" 
	
	if second_card == 8:
		print "Your second card is an eight."
		print "\n" 
	
	if second_card == 9:
		print "Your second card is a nine."
		print "\n" 
	
	if second_card == 10:
		print "Your second card is a ten."
		print "\n" 
	
	if second_card == 11:
		print "Your second card is a %s" % random.choice(faces)
		print "\n" 
 
	total = first_card + second_card 
 
	if total > 21:
		print "Looks like you're over 21. You lose this round for sure..."
		money -= bet
		new_hand(money)
	
	if total == 21:
		print "Blackjack! Quick win for you!"
		money += bet
		new_hand(money)
 
	first_dealer = random.randint(1, 11)
 
	if first_dealer == 1:
		print "The dealer's first card is an ace."
		print "\n" 
 
	if first_dealer == 2:
		print "The dealer's first card is a two."
		print "\n" 
	
	if first_dealer == 3:
		print "The dealer's first card is a three."
		print "\n" 
	
	if first_dealer == 4:
		print "The dealer's first card is a four."
		print "\n" 
	
	if first_dealer == 5:
		print "The dealer's first card is a five."
		print "\n" 
	
	if first_dealer == 6:
		print "The dealer's first card is a six."
		print "\n" 
	
	if first_dealer == 7:
		print "The dealer's first card is a seven."
		print "\n" 
	
	if first_dealer == 8:
		print "The dealer's first card is an eight."
		print "\n" 
	
	if first_dealer == 9:
		print "The dealer's first card is a nine."
		print "\n" 
	
	if first_dealer == 10:
		print "The dealer's first card is a ten."
		print "\n" 
	
	if first_dealer == 11:
		print "The dealer's first card is a %s" % random.choice(faces)
		print "\n" 
 
	print "The dealer places another card face down on the table."
	
	choice(total, first_dealer, money, bet)
 
def dealer(total, first_dealer, money, bet):
	total_dealer = first_dealer	
	while total_dealer < 21: 
		print "The dealer flips his next card."
		second_dealer = random.randint(1, 11)
		if second_dealer == 1:
			print "The card is an ace."
			print "\n" 
		if second_dealer == 2:
			print "The card is a two."
			print "\n" 
		elif second_dealer == 3:
			print "The card is a three."
			print "\n" 
		elif second_dealer == 4:
			print "The card is a four."
			print "\n" 	
		elif second_dealer == 5:
			print "The card is a five."
			print "\n" 	
		elif second_dealer == 6:
			print "The card is a six."
			print "\n" 
		elif second_dealer == 7:
			print "The card is a seven."
			print "\n" 
		elif second_dealer == 8:
			print "The card is an eight."
			print "\n" 	
		elif second_dealer == 9:
			print "The card is a nine."
			print "\n" 	
		elif second_dealer == 10:
			print "The card is a ten."
			print "\n" 	
		elif second_dealer == 11:
			print "The card is a %s" % random.choice(faces)
			print "\n" 
		total_dealer += second_dealer
		print "Dealer is at %s" % total_dealer
		if total_dealer > 21:
			print "Looks like the dealer broke, you win!"
			money += bet
			new_hand(money)
		elif total_dealer == 21:
			print "Blackjack! Dealer couldn't have played it better. You lose this time."
			money -= bet
			new_hand(money)
		elif total_dealer > total:
			print "Looks like the dealer got higher than %s, tough luck. House wins." % total
			money -= bet
			new_hand(money)
 
 
	
	
def choice(total, first_dealer, money, bet):	
	while total < 21:
		print "Hit or stick?"
		choice1 = raw_input("? ")
		if "hit" in choice1: 
			extra_card = random.randint(1, 11)
			total += extra_card
			print "You're at %d" % total
		elif "stick" in choice1:
			print "You stick with %d" % total
			dealer(total, first_dealer, money, bet)
#the else statement below is temporary, please remove with final version and make sure 
#this loop doesn't get the program stuck later!
		else:
			choice(total, first_dealer, money,bet)
		
		if total == 21:
			print "Blackjack! You win this round."
			money += bet
			new_hand(money)
		if total > 21:
			print "Looks like you broke 21. That's a win for the house."
			money -= bet
			new_hand(money)
			
			
initial_draw(money)



