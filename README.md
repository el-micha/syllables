# syllables
Excerpt from a language project. Create a set of syllable patterns and derived syllables as a basis to an aesthetically consistent language.

There are about 16'000 English syllables (http://web.archive.org/web/20160822211027/http://semarch.linguistics.fas.nyu.edu/barker/Syllables/index.txt). English speakers can recognize them as English, and they can recognize fake syllables as possible-English or clearly non-English (jabberwock vs vzkvet). This is due to the structural rules which syllables obey - in every language, albeit with different concrete rules. 

English syllables have the general form (C)^3 V (C)^5. However, not all consonants are eligible for every position, so much more structure needs to be obeyed to produce an english-sounding/looking syllable. The tables at https://en.wikipedia.org/wiki/English_phonology#Phonotactics, e.g., show possible onsets and codas. The choices are very limited, because the possible combinations from the different sonority classes are quite restrictive.

This program attempts to create a number of such subpatterns to limit the number of possible syllables. The fewer patterns, the more recognizable (as a member of its language) a random word will look. 

Here is a small excerpt from a generated syllable set:
Creating patterns of the form V(C)^2
```
a = SyllableSet(alph, 0, 2)
```
gives onsets and codas and their combinations:
```
onset pattern strings
['', 'C']
coda pattern strings
['', 'C', 'CC']
pattern strings
['V', 'VC', 'VCC', 'CV']
```
The pattern CV is contained because this pattern is contained in _every_ human language, and is therefore included by default. 

