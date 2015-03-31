# -*- coding: utf-8 -*-
import pprint
from collections import defaultdict
from string import punctuation

# Get a word count for each word in a pair of wordlists that appear in a block of text.
# Exclude the appearance of a word from the count if any of the 3 words before or after the word
# in question are a member of the negator set (no, not, never).

def main():
	wordlist1 = ['mickey', 'pluto', 'goofy', 'minnie', 'donald']
	wordlist2 = ['bugs', 'daffy', 'elmer', 'foghorn', 'porky']

	# Whether to ensure the words in the wordlists are lowercase depends on your use-case
	wordlist1 = [element.lower() for element in wordlist1]
	wordlist2 = [element.lower() for element in wordlist2]
	mergedwordset = set(wordlist1 + wordlist2)
	negatorset = set(['no', 'not', 'never'])

	# Using collections.defaultdict here so that we can add a key with the value of 1 
	# if it doesn't already exist and increment the value of the key if it does exist.
	countincludingneg = defaultdict(int)
	countexcludingneg = defaultdict(int)

	# Using a multi-line string here just to simplify this example.
	# This will be parsed for the word count.
	# Adapt it to your own uses.
	# Text excerpts from wikipedia:
	# http://en.wikipedia.org/wiki/Pluto_(Disney)
	textblock = '''
Pluto, also called Pluto the Pup, is a cartoon character created in 1930 by Walt Disney Productions. He is a red-colored, medium-sized, short-haired dog with black ears. Unlike most Disney characters, Pluto is not anthropomorphic beyond some characteristics such as facial expression, though he did speak for a short portion of his history. He is Mickey Mouse's pet. Officially a mixed-breed dog, he made his debut as a bloodhound in the Mickey Mouse cartoon The Chain Gang. Together with Mickey Mouse, Minnie Mouse, Donald Duck, Daisy Duck, and Goofy, Pluto is one of the "Sensational Six"—the biggest stars in the Disney universe. Though all six are non-human animals, Pluto alone is not dressed as a human.
Pluto debuted in animated cartoons and appeared in 24 Mickey Mouse films before receiving his own series in 1937. All together Pluto appeared in 89 short films between 1930 and 1953. Several of these were nominated for an Academy Award, including The Pointer (1939), Squatter's Rights (1946), Pluto's Blue Note (1947), and Mickey and the Seal (1948). One of his films, Lend a Paw (1941), won the award in 1942. Because Pluto does not speak, his films generally rely on physical humor. This made Pluto a pioneering figure in character animation, which is expressing personality through animation rather than dialogue.
Like all of Pluto's co-stars, the dog has appeared extensively in comics over the years, first making an appearance in 1931. He returned to theatrical animation in 1990 with The Prince and the Pauper and has also appeared in several direct-to-video films. Pluto also appears in the television series Mickey Mouse Works (1999–2000), House of Mouse (2001–2003), and Mickey Mouse Clubhouse (2006–2013).
In 1998, Disney's copyright on Pluto, set to expire in several years, was extended by the passage of the Sonny Bono Copyright Term Extension Act. Disney, along with other studios, lobbied for passage of the act to preserve their copyrights on characters such as Pluto for 20 additional years.
Pluto first and most often appears in the Mickey Mouse series of cartoons. On rare occasions he is paired with Donald Duck ("Donald and Pluto", "Beach Picnic", "Window Cleaners", "The Eyes Have It", "Donald's Dog Laundry", & "Put Put Troubles").
The first cartoons to feature Pluto as a solo star were two Silly Symphonies, Just Dogs (1932) and Mother Pluto (1936). In 1937, Pluto appeared in Pluto's Quin-Puplets which was the first instalment of his own film series, then headlined Pluto the Pup. However, they were not produced on a regular basis until 1940, by which time the name of the series was shortened to Pluto.
His first comics appearance was in the Mickey Mouse daily strips in 1931 two months after the release of The Moose Hunt. Pluto Saves the Ship, a comic book published in 1942, was one of the first Disney comics prepared for publication outside newspaper strips. However, not counting a few cereal give-away mini-comics in 1947 and 1951, he did not have his own comics title until 1952.
In 1936 Pluto got an early title feature in a picture book under title "Mickey Mouse and Pluto the Pup" by Whitman Publishing.
Pluto runs his own neighborhood in Disney's Toontown Online. It's called the Brrrgh and it's always snowing there except during Halloween. During April Toons Week, a weekly event that is very silly, Pluto switches playgrounds with Minnie (all other characters do this as well). Pluto actually talks in Minnie's Melodyland.
Pluto has also appeared in the television series Mickey Mouse Works (1999–2000), Disney's House of Mouse (2001–2003) and Mickey Mouse Clubhouse (2006–present). Curiously enough, however, Pluto was the only standard Disney character not included when the whole gang was reunited for the 1983 featurette Mickey's Christmas Carol, although he did return in The Prince and the Pauper (1990) and Runaway Brain (1995). He also had a cameo in Who Framed Roger Rabbit (1988). In 1996, he made a cameo in the Quack Pack episode "The Really Mighty Ducks".
'''
	# Removing leading and trailing whitespace.
	# Removing new-lines so we can extend the look-aheads / look-behinds across lines.
	# Removing punctuation.
	# Setting all text to lowercase
	# Adjust to your use-cases
	textblock = textblock.strip().replace('\n', ' ').translate(None, punctuation).lower()
	textblockwords = textblock.split()

	# Construct a list of 6-gram (or less) word windows.
	# The window will center on each individual word of the textblock
	# and include the 3 words before and after its appearance.
	windows = n_gram_word_windows(textblockwords, 3)

	# Un-comment the following line if you'd like to see a representation of the n-gram word windows
	#pprint.pprint(windows)


	for windowdict in windows:
		for key, ngramlist in windowdict.iteritems():
			# Is the word a member of the wordlists?
			if key in mergedwordset:
				countincludingneg[key] += 1
				# Do the words preceeding or following appear in the set of negators?
				if len(negatorset.intersection(set(ngramlist))) == 0:
					countexcludingneg[key] += 1
	print "Count including negators"
	pprint.pprint(countincludingneg)
	print "Count excluding negators"
	pprint.pprint(countexcludingneg)



# The idea here is to examine each word in the textblock and
# create a list containing the 3 words before the word, the word itself, and the 3 words following the word.
# This method will return a list of dictionaries.
# The dictionary will be comprised of the examined word as the key, and its n-gram word window as the value.
def n_gram_word_windows(textlist, lookaheadbehind=3):
	wordwindows = []
	for index, item in enumerate(textlist):
		intermediatelist = []
		if index < lookaheadbehind:
			for preceedingword in textlist[:index]:
				intermediatelist.append(preceedingword)
		else:
			for preceedingword in textlist[index-lookaheadbehind:index]:
				intermediatelist.append(preceedingword)
		if index < len(textlist):
			for lookaheadword in textlist[index:index+lookaheadbehind+1]:
				intermediatelist.append(lookaheadword)
		wordwindows.append({item: intermediatelist})
	return wordwindows


if __name__ == '__main__':
	main()