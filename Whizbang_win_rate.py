#CONDITIONS needed to run this program:
#All Whizbang decks in HS deck tracker app must have their deck name start with 'Whizbang'
#'DeckStats.xml' file (can be found at %AppData%\HearthstoneDeckTracker) must be copied into your python/IDE directory

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

#Calculates winrate and prepares output
whizbang_winrate = (wins/len(gameresults) * 100)
print('Total Whizbang win rate: {}%'.format((round(whizbang_winrate, 2))),'({}/{})'.format(wins,len(gameresults)))
