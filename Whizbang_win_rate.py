#INFO: In the game 'Hearth Stone' by Blizzard Entertainment, there is a card called 'Whizbang the Wonderful.'
#When you queue up for a match with this card in a deck, the game will assign you a random, premade, deck out of a
#pool of 18 total decks.

#PURPOSE: This program uses HS Deck Tracker data to calculate the total win rate of all your WHIZBANG decks combined!
#(to my knowledge, this is not yet a feature available on the HS Deck Tracker app)

#CONDITIONS needed to run this program:
#Enter all Whizbang decks into deck tracker and start the name of each of them with 'Whizbang'
#'DeckStats.xml' file (can be found at %AppData%\HearthstoneDeckTracker) must be copied into your python IDE directory

#Set up element tree to parse XML data
import xml.etree.ElementTree as ET
tree = ET.parse('DeckStats.xml')
root = tree.getroot()
gameresults = list()

#Finding games where the deck name starts with 'Whizbang' and appends win or loss result into list (winrate)
for deckname in root.iter('Game'):
    name = deckname.find('DeckName')
    if name.text.startswith('Whizbang'):
        result = deckname.find('Result').text
        gameresults.append(result)

#Sums the number of wins
wins = 0
for outcome in gameresults:
    if outcome == 'Win':
        wins = wins + 1

#Calculates winrate
whizbang_winrate = (wins/len(gameresults) * 100)
print('Total Whizbang win rate: {}%'.format((round(whizbang_winrate, 2))),'({}/{})'.format(wins,len(gameresults)))