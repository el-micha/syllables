# Syllables
Excerpt from a language project. Create a set of syllable patterns and derived syllables as a basis to an aesthetically consistent language.

There are about 16'000 English syllables (http://web.archive.org/web/20160822211027/http://semarch.linguistics.fas.nyu.edu/barker/Syllables/index.txt). English speakers can recognize them as English, and they can recognize fake syllables as possible-English or clearly non-English (_jabberwock_ vs _vzkvet_). This is due to the structural rules which syllables obey - in every language, albeit with different concrete rules. 

English syllables have the general form (C)^3 V (C)^5. However, not all consonants are eligible for every position, so much more structure needs to be obeyed to produce an english-sounding/looking syllable. The tables at https://en.wikipedia.org/wiki/English_phonology#Phonotactics, e.g., show possible onsets and codas. The choices are very limited, because the possible combinations from the different sonority classes are quite restrictive.

This program attempts to create a number of such subpatterns to limit the number of possible syllables. The fewer patterns, the more recognizable (as a member of its language) a random word will look. 

# Example
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

All the randomly generated onset patterns consist of a single class (plosives, fricatives etc, see code for all classes), because the only possible onset in CVCC is a single C. However, if a class is chosen (like the nasals, class 'E'), not all members may be elected: 
```
[('E', ['ng'])]
```

The codas can be empty, C or CC, but not all CC combinations are possible. A randomly chosen example:
```
[('E', ['m', 'n', 'ng']), ('D', ['w'])]
[('E', ['m']), ('C', ['f', 'h', 'th', 'sh', 'z'])]
```
This means we can have ["amw", "anw", "angw"] (any nasal followed by "w", class 'D'), but if we follow a nasal with a voiceless fricative (class 'C'), then the only allowed nasal is "m", so we get ["mf", "mh", "mth", "msh", "mz"]. 

Such coda/onset patterns are then combined with each other and a vowel, which gives, using the examples above:
```
E_V_ED
E_V_EC
```
The letters correspond to a (possibly reduced) sonority class (see code). 

When populating these concrete syllable patterns with letters from an alphabet, we get, e.g.:
```
----- C_V_EC -----
hamth, samh, themz, samth, shomh, fimf, fumf, hamh, thimz, shumz
----- C_V_GC -----
zulf, salf, hilsh, zajs, hujth, shelsh, sholz, fulch, solth, zilh
----- C_V_BA -----
shubp, shogp, sigp, zobt, hugk, zedp, shubk, zidp, fagk, zagt
----- E_V_ED -----
ngongw, ngingw, ngamw, nginw, ngomw, ngungw, ngenw, ngemw, ngengw, ngangw
----- E_V_EC -----
ngomh, ngamf, ngemz, ngumsh, ngumz, ngomsh, ngamz, ngimz, ngemth, ngimh
```

Randomly combining such syllables to words of 1-3 syllables gives:

_alhojidk, sage, jish, wugwoh, mohnimwno, getmotweh, lizriw, fihozno, zeznu, nipelt, effaf, fubanim, natot, iwig, gobej, elruz, ohzeb, monloiw, mejrno, thajz, rilzfuf, filuguj, suj, azthe, sho, fegthalz, malfhizash, emsopna, golfan, ulthet, ubnuz, sobpmiw, femijhimz, gojfmazek, lungazge, ughuwfi, new, wupnowam_


Rerunning the program with the same inputs gives a list of words with distinct aesthetics from the first - ymmv. 

_tesripit, bigbuk, defbeh, gifb, bab, gowskeb, wersihaz, awdulbet, dos, ad, gursab, upbuth, uhodtok, rateh, owwagahg, kurku, ulwdatat, ig, udihor, idokgi, ep, wuz, dehgergo, uhrejri, atkuar, dutierh, orskatoh, pefd, dowrilwefg, uzri, pikadiw, azwottaz, befror, etuf, belgafrab, ri, dap, ijbewgufb, utajelb, alwufdde, piw, wu, rurbadad, kuw, bagik, wo, ezdubug, gusrugu, uzgap, beshwej, aj, rubbahbpit, rabiwisd, ot, webod, kog, teposar, algwa, usddah_