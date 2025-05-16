#main file for tarot python script
"""
MUST HAVE:
Terminal program with at least one interactive feature using input()
Use git version control
Use command line and file navigation
Write an online post on the project

"""

#please push commit
"""
IDEA:
Class defining tarot cards
    Init Name, number, major/minor arcana, cups/wands/knives/pentacles/Null alignment, upright/reversed???,
    upright meaning, reversed meaning, elemental alignment?
    Repr card info
    Reset - resets all cards to upright position??????
Class for Deck
    Init List of tarot card objects based on provided information
    Repr names of all cards in deck
    Shuffle - takes number of cards to randomly draw from deck based on Spread, assigns upright/reversed value,
    returns card values
Methods for Spread (a spread is a specific layout of cards chosen from the deck to intuit specific fortunes or questions)
    THIS SHOULD BE WITHIN THE DECK CLASS
    Would take random cards from a Deck object and array them into a specific spread based on what is requested by user
    Potential spreads: Past/Present/Future(3 cards), 4 card spread, card of the day (1 card)
Main code allows user to select what kind of spread they want and will produce text of that spread

BONUS:
I could input multiple types of decks for the user to choose from
Expanded spread options
raider waite deck has 78 cards total (22 major, 56 minor)
"""
import random
import time

#TAROT CARD CLASS - Creates a card with all their features and meanings
class tarot_card:
    def __init__(self, name, number, arcana, suit, position, upright_meaning, reversed_meaning):
        self.name = name
        self.number = number
        self.arcana = arcana
        self.suit = suit
        self.position = position
        self.upright_meaning = upright_meaning
        self.reversed_meaning = reversed_meaning

    def __repr__(self):
        return "Name: {name}, Number: {number}, Arcana: {arcana}, Suit: {suit}, Its Position: {position}, Upright Meaning: {upright_meaning}, Reversed Meaning: {reversed_meaning}".format(name = self.name, number = self.number, arcana = self.arcana, suit = self.suit, position = self.position, upright_meaning = self.upright_meaning, reversed_meaning = self.reversed_meaning)

    #Randomly sets position of card to either upright or reversed
    def uprightReverse(self):
        coinFlip = random.randint(0,1)

        if coinFlip == 0:
            self.position = "upright"
        else:
            self.position = "reversed"

#DECK CLASS - Takes a list of cards to form a deck, the deck style, and can shuffling and perform specific spreads with the cards
class deck:
    def __init__(self, cardList, deckStyle):
        self.cardList = cardList
        self.deckStyle = deckStyle

    def __repr__(self):
        return self.deckStyle

    #Picks a random card from the tarot deck to present as the card of the day and prints the card meaning
    def cardOfTheDay(self):
        tempDeck = self.cardList.copy()
        random.shuffle(tempDeck)
        tempCard = tempDeck[0]
        tempCard.uprightReverse() 
        if tempCard.position == "upright":
            print("  C A R D  O F  T H E  D A Y  \n"
                  "______________________________")
            print("The Card of the Day is the {name} in the UPRIGHT position.".format(name = tempCard.name))
            print("MEANING: " + tempCard.upright_meaning)
            print("______________________________")
        else:
            print("  C A R D  O F  T H E  D A Y  \n"
                  "______________________________")
            print("The card of the day is the {name} in the REVERSED position.".format(name = tempCard.name))
            print("MEANING: " + tempCard.reversed_meaning)
            print("______________________________")

    #Shuffles a copy of the deck and selects 2 cards to represent a querent's situation and potential advice for the situation
    def twoCardCross(self):
        counter = 0
        tempDeck = self.cardList.copy()
        tempHand = []

        random.shuffle(tempDeck)
        for card in tempDeck:
            card.uprightReverse()

        while counter<=1:
            tempHand.append(tempDeck[counter])
            counter += 1

        print("   T W O  C A R D  C R O S S   \n"
              "_______________________________")
        print("Take 10 seconds to think of a situation you are currently dealing with.\n"
              ".....")
        time.sleep(10)
        print("CARD 1: The card that represents your situation is the {position} {name}.".format(position = tempHand[0].position, name = tempHand[0].name))
        if tempHand[0].position == "upright":
            print("MEANING: " + tempHand[0].upright_meaning)
        else:
            print("MEANING: " + tempHand[0].reversed_meaning)
        print("CARD 2: Seek advice for this situation in the {position} {name}.".format(position = tempHand[1].position, name = tempHand[1].name))
        if tempHand[1].position == "upright":
            print("MEANING: " + tempHand[1].upright_meaning)
        else:
            print("MEANING: " + tempHand[1].reversed_meaning)
        print("_______________________________")

    #Shuffles a copy of the deck and selects 3 cards to represent the Past, Present, and Future and prints the spread
    def pastPresentFuture(self):
        counter = 0
        tempDeck = self.cardList.copy()
        tempHand = []

        random.shuffle(tempDeck)
        for card in tempDeck:
            card.uprightReverse()

        while counter <= 2:
            tempHand.append(tempDeck[counter])
            counter += 1

        print("  P A S T  P R E S E N T  F U T U R E  \n"
            "___________________________________________")
        print("CARD 1: The card that represents your PAST is the {position} {name}.".format(position = tempHand[0].position, name = tempHand[0].name))
        if tempHand[0].position == "upright":
            print("MEANING: " + tempHand[0].upright_meaning)
        else:
            print("MEANING: " + tempHand[0].reversed_meaning)
        print("CARD 2: The card that represents your PRESENT is the {position} {name}.".format(position = tempHand[1].position, name = tempHand[1].name))
        if tempHand[1].position == "upright":
            print("MEANING: " + tempHand[1].upright_meaning)
        else:
            print("MEANING: " + tempHand[1].reversed_meaning)
        print("CARD 3: The card that represents your FUTURE is the {position} {name}.".format(position = tempHand[2].position, name = tempHand[2].name))
        if tempHand[2].position == "upright":
            print("MEANING: " + tempHand[2].upright_meaning)
        else:
            print("MEANING: " + tempHand[2].reversed_meaning)
        print("___________________________________________")

    #Shuffles a copy of the deck and selects 4 cards to represent a current obstacle or goal the querent is facing
    def fourCardSpread(self):
        counter = 0
        tempDeck = self.cardList.copy()
        tempHand = []

        random.shuffle(tempDeck)
        for card in tempDeck:
            card.uprightReverse()

        while counter <= 3:
            tempHand.append(tempDeck[counter])
            counter += 1

        print("  F O U R  C A R D  S P R E A D  \n"
            "_____________________________________")
        print("Take 10 seconds to think of a goal you have.\n"
              ".....")
        time.sleep(10)
        print("CARD 1: The nature of your current GOAL can be found in the {position} {name}.".format(position = tempHand[0].position, name = tempHand[0].name))
        if tempHand[0].position == "upright":
            print("MEANING: " + tempHand[0].upright_meaning)
        else:
            print("MEANING: " + tempHand[0].reversed_meaning)
        print("CARD 2: You may encounter OBSTACLES that align with the {position} {name}.".format(position = tempHand[1].position, name = tempHand[1].name))
        if tempHand[1].position == "upright":
            print("MEANING: " + tempHand[1].upright_meaning)
        else:
            print("MEANING: " + tempHand[1].reversed_meaning)
        print("CARD 3: Gain INSIGHT on overcoming these obstacles with the {position} {name}.".format(position = tempHand[2].position, name = tempHand[2].name))
        if tempHand[2].position == "upright":
            print("MEANING: " + tempHand[2].upright_meaning)
        else:
            print("MEANING: " + tempHand[2].reversed_meaning)
        print("CARD 4: The expected OUTCOME given this advice is best represented by the {position} {name}.".format(position = tempHand[3].position, name = tempHand[3].name))
        if tempHand[3].position == "upright":
            print("MEANING: " + tempHand[3].upright_meaning)
        else:
            print("MEANING: " + tempHand[3].reversed_meaning)
        print("_____________________________________")

    #shuffles a copy of the deck and selects 5 cards to represent the nature of a relationship the querent is in
    def fiveCardLove(self):
        counter = 0
        tempDeck = self.cardList.copy()
        tempHand = []

        random.shuffle(tempDeck)
        for card in tempDeck:
            card.uprightReverse()

        while counter <= 4:
            tempHand.append(tempDeck[counter])
            counter += 1

        print("This 5 card spread gives insight into love and relationships in general.")
        print("Card 1: You")
        print("The card that repesents you in this relationship is the {position} {name}.".format(position = tempHand[0].position, name = tempHand[0].name))
        print("Card 2: The Other Person")
        print("The card that represents the other person in this relationship is the {position} {name}.".format(position = tempHand[1].position, name = tempHand[1].name))
        print("Card 3: The Relationship")
        print("The card that repesents the current state of the relationship is the {position} {name}.".format(position = tempHand[2].position, name = tempHand[2].name))
        print("Card 4: The Past")
        print("The card that represents past aspects of this relationship is the {position} {name}.".format(position = tempHand[3].position, name = tempHand[3].name))
        print("Card 5: The Future")
        print("The card that represents future aspects of this relationship is the {position} {name}.".format(position = tempHand[4].position, name = tempHand[4].name))
        for card in tempHand:
            if card.position == "upright":
                print("The {position} {name}: ".format(position=card.position, name=card.name) + card.upright_meaning)
            else:
                print("The {position} {name}: ".format(position=card.position, name=card.name) + card.reversed_meaning)


#BUILDING DECK FROM FILE
with open('card_data.txt') as card_doc:
    card_text = card_doc.read()
first_split = card_text.split('!')
second_split = []
tarot_deck = []
for card in first_split:
    second_split.append(card.split(';'))
for entry in second_split:
    tarot_deck.append(tarot_card(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]))

new_deck = deck(tarot_deck, "Raider Waite")

#START MAIN LOOP
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n"
      "|                                           |\n"
      "|         T A R O T  R E A D I N G S        |\n"
      "|                                           |\n"
      "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Welcome! Would you like a reading today? Y/N")
loop1 = True
while loop1 == True:
    reply1 = input()
    if reply1 == 'n' or reply1 == 'N':
        print("Okay, goodbye!")
        exit()
    elif reply1 == 'y' or reply1 == 'Y':
        loop1 = False
    else:
        print("Please enter either Y or N")
        loop1 = True

loop2 = True
while loop2 == True:
    print("Please select a number from the following options:")
    print("1. CARD OF THE DAY\n2. TWO CARD CROSS\n3. PAST PRESENT FUTURE\n4. FOUR CARD SPREAD\n5. FIVE CARD LOVE\n6. INFO ABOUT SPREADS")
    reply2 = input()

    if reply2 == '1':
        new_deck.cardOfTheDay()
    elif reply2 == '2':
        new_deck.twoCardCross()
    elif reply2 == '3':
        new_deck.pastPresentFuture()
    elif reply2 == '4':
        new_deck.fourCardSpread()
    elif reply2 == '5':
        new_deck.fiveCardLove()
    elif reply2 == '6':
        print("     S P R E A D  I N F O     \n"
              "______________________________")
        print("Each spread provides different insight on different topics or questions.")
        print("1. CARD OF THE DAY - Draws one random card from the deck. This can be used to understand the general tone of the day, or to answer a specific question on the querent's mind.\n"
              "2. TWO CARD CROSS - Draws two cards and provides insight on a specific situation. The first card represents the situation itself. The second card represents advice about the situation.\n"
              "3. PAST PRESENT FUTURE - Draws three cards from the deck. The first, second, and third card each represent aspects of the querent's past, present, and future respectively.\n"
              "4. FOUR CARD SPREAD - Draws four cards to give insight on goals and obstacles in the querent's life. The first card represents the goal. The second card represents potential obstacles.\nThe third card gives insight on overcoming the obstacles. The fourth card represents what outcome can be expected based on the other cards.\n"
              "5. FIVE CARD LOVE - Draws five cards to give insight into a relationship in the querent's life. The first card represents the querent themself.\nThe second card represents the other person or group. The third card represents the nature of the relationship currently. The fourth card represents past aspects of this relationship.\nThe fifth card represents how this relationship might change in the future.")
        print("______________________________")
        continue
    elif reply2 == '7':
        for card in new_deck.cardList:
            print(card)
    else:
        print("The value entered must a number 1 through 6")
        continue

    print("Would you like another reading? Y/N")
    loop3 = True
    while loop3 == True:
        reply3 = input()
        if reply3 == 'y' or reply3 == 'Y':
            loop3 = False
        elif reply3 == 'n' or reply3 == 'N':
            print("Goodbye!")
            exit()
        else:
            print("Please enter Y or N")
            loop3  = True


#TESTING
#the_Fool = tarot_card("Fool", 0, "Major", "Null", "upright", "Folly, mania, extravagance", "Negligence, absense, distribution")
#the_Magician = tarot_card("Magician", 1, "Major", "Null", "upright", "Skill, diplomacy, self-confidence", "Illness, disgrace, disquiet")
#the_High_Priestess = tarot_card("High Priestess", 2, "Major", "Null", "upright", "Secrets, mystery, the future as yet unrevealed", "Passion, conceit, surface knowledge")
#the_Empress = tarot_card("Empress", 3, "Major", "Null", "upright", "Fruitfulness, initiative, clandestine", "Light, truth, the unraveling of involved matters")
#the_Emperor = tarot_card("Emperor", 4, "Major", "Null", "upright", "Stability, power, protection", "Benevolence, compassion, immaturity")
#print(the_Fool)


#print(new_deck)
#new_deck.cardOfTheDay()
#new_deck.twoCardCross()
#new_deck.pastPresentFuture()
#new_deck.fourCardSpread()
#new_deck.fiveCardLove()
