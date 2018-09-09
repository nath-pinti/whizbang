#CONDITIONS needed to run this program:
#All Whizbang decks in HS deck tracker app must have their deck name start with 'Whizbang'
#'DeckStats.xml' file (can be found at %AppData%\HearthstoneDeckTracker) must be copied into your python/IDE directory

#Set up element tree to parse XML data
import xml.etree.ElementTree as ET
tree = ET.parse('DeckStats.xml')
root = tree.getroot()

#Finding games where the deck name starts with 'Whizbang' and appends win or loss result into list (gameresults)
gameresults = list()
for deckname in root.iter('Game'):
    name = deckname.find('DeckName').text
    if name.startswith('Whizbang'):
        result = deckname.find('Result').text
        gameresults.append(result)

#Sums the number of wins
wins = 0
for outcome in gameresults:
    if outcome == 'Win':
        wins += 1

#Calculates winrate and prepares output
whizbang_winrate = (wins/len(gameresults) * 100)
print('Total Whizbang win rate: {}%'.format((round(whizbang_winrate, 2))),'({}/{})'.format(wins, len(gameresults)))

#Additional statistics (number of wins by class, sorted by #wins descending)
classwins = dict()
for deckname in root.iter('Game'):
    name = deckname.find('DeckName').text
    if name.startswith('Whizbang'):
        result = deckname.find('Result').text
        if result == 'Win':
            playerclass = deckname.find('PlayerHero').text
            if playerclass not in classwins:
                classwins[playerclass] = 1
            else:
                classwins[playerclass] += 1

classwins_sorted = list()                   #Converts dict to list of tupules for sorting
for key, value in classwins.items():
    classwins_sorted.append((value, key))
classwins_sorted.sort(reverse = True)
print('\nClass', "."*3, 'Wins')
for key, value in classwins_sorted:
    print(value, "."*(10-len(value)), key)
