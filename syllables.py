import random
import math

#random.seed(0)

# english: (C)^3 V (C)^5
# german : (C)^2 V (C)^2 or same as english


# Sonoritätswert	Sonoritätsklasse
# 1	Plosive
# 2	Frikative
# 3	Nasale
# 4	Liquide
# 5	Approximanten
# 6	geschlossene Vokale
# 7	offene Vokale


class Alphabet:
    def __init__(self):
        self.voiceless_plosive = ["p", "t", "k"]                                    # A
        self.voiced_plosive = ["b", "d", "g"]                                       # B
        self.plosives = self.voiceless_plosive + self.voiced_plosive  # stops
        self.voiceless_fricatives = ["f", "s", "h", "th", "sh", "ch", "z"]    # C
        self.voiced_fricatives = ["w"]                                              # D
        self.fricatives = self.voiceless_fricatives + self.voiced_fricatives
        self.nasals = ["m", "n", "ng"]                                              # E
        self.liquids = ["r"]                                                        # F
        self.approximants = ["l", "j"]                                              # G
        self.vowels = ["u", "i", "o", "e", "a"]                                     # V

        self.sonority_hierarchy_list = [self.voiceless_plosive, self.voiced_plosive, self.voiceless_fricatives, self.voiced_fricatives, self.nasals, self.liquids, self.approximants]
        self.sonority_hierarchy_categories = ["A", "B", "C", "D", "E", "F", "G"]
        self.sonority_hierarchy = {k:v for (k,v) in zip(self.sonority_hierarchy_categories, self.sonority_hierarchy_list)}
        self.consonants = self.plosives + self.fricatives + self.nasals + self.liquids + self.approximants
        self.phonemes = self.vowels + self.consonants

    def get_vowels(self):
        return self.vowels

    def get_consonants(self):
        return self.consonants

    def sonority(self, phoneme):
        """Return small numbers for consonants and large numbers for vocals."""
        if phoneme in self.voiceless_plosive:
            return 1 + self.voiceless_plosive.index(phoneme) / len(self.voiceless_plosive)
        if phoneme in self.voiced_plosive:
            return 2 + self.voiced_plosive.index(phoneme) / len(self.voiced_plosive)
        if phoneme in self.voiceless_fricatives:
            return 3 + self.voiceless_fricatives.index(phoneme) / len(self.voiceless_fricatives)
        if phoneme in self.voiced_fricatives:
            return 4 + self.voiced_fricatives.index(phoneme) / len(self.voiced_fricatives)
        if phoneme in self.nasals:
            return 5 + self.nasals.index(phoneme) / len(self.nasals)
        if phoneme in self.liquids:
            return 6 + self.liquids.index(phoneme) / len(self.liquids)
        if phoneme in self.approximants:
            return 7 + self.approximants.index(phoneme) / len(self.approximants)
        if phoneme in self.vowels:
            return 8 + self.vowels.index(phoneme) / len(self.vowels)


class SyllableSet:
    """Consists of a number of SyllablePatterns like CV, V, CVC, etc.
    Parameters are the maximum number of onsets auslaut=coda
    Even if on = 0, CV will be allowed."""
    def __init__(self, alphabet, max_onset, max_coda):
        self.alphabet = alphabet
        self.max_onset = max_onset
        self.max_coda = max_coda
        self.pattern_strings = []
        for i in range(self.max_onset + 1):
            for j in range(self.max_coda + 1):
                pattern = "C"*i + "V" + "C"*j
                self.pattern_strings.append(pattern)
        if not "CV" in self.pattern_strings:
            self.pattern_strings.append("CV")

        print("pattern strings")
        print(self.pattern_strings)
        # extract all onsets
        self.onset_pattern_strings = []
        for pattern_string in self.pattern_strings:
            self.onset_pattern_strings.append(pattern_string[0:pattern_string.index("V")])
        self.onset_pattern_strings = list(set(self.onset_pattern_strings))
        # extract all codas
        self.coda_pattern_strings = []
        for pattern_string in self.pattern_strings:
            self.coda_pattern_strings.append(pattern_string[pattern_string.index("V")+1:])
        self.coda_pattern_strings = list(set(self.coda_pattern_strings))

        print("onset pattern strings")
        print(self.onset_pattern_strings)
        print("coda pattern strings")
        print(self.coda_pattern_strings)

        #self.patterns = [SyllablePattern(p) for p in self.pattern_strings]
        #print(self.pattern_strings)
        # perhaps: go through patterns and make them more concrete, that is: for every C and V, replace it
        # by a concreter form like sonarant, obstruent, frikative etc... or a member of a random subset of sets, like
        # a frikative or plosive but not a nasal.
        # C can also be replaced by the empty letter and so delete a possibility
        # perhaps generate every possibility

        # onsets: for CCCV, determine three distinct sets in the right order
        # for each set: 50% chance to only use a subset. the subset size is uniform random, but at least 1
        # the result is one concrete pattern for CCCV. create 10 each and at the end choose only a few, where longer
        # patterns are less likely

        self.onset_patterns = self.create_reduced_patterns(self.onset_pattern_strings, rev=False)
        self.coda_patterns = self.create_reduced_patterns(self.coda_pattern_strings, rev=True)
        print("============================================================================================")
        print("onsets")
        print(self.onset_patterns)
        for x in self.onset_patterns:
            print(x)
        print("codas")
        print(self.coda_patterns)
        for x in self.coda_patterns:
            print(x)

        #combine every onset with every coda to create final syllable patterns like CCCVCC
        self.syllable_patterns = {}
        for onset in self.onset_patterns:
            for coda in self.coda_patterns:
                if len(onset) == 0 and len(coda) == 0:
                    continue
                # lengths of these two lists are the onset length and the coda length. so we can generate the general CVC structure
                combined_pattern = "C"*len(onset) + "V" + "C"*len(coda)
                concrete_pattern = SyllablePattern(onset, coda)
                if not combined_pattern in self.syllable_patterns.keys():
                    self.syllable_patterns[combined_pattern] = []
                self.syllable_patterns[combined_pattern].append(concrete_pattern)

        print("Number of syllable patterns: " + str(sum([len(b) for a,b in self.syllable_patterns.items()])))
        self.syllables = []
        for pattern, concrete_pattern_list in self.syllable_patterns.items():
            print("=========== Abstract Pattern: " + pattern + " ==========")
            for concrete_pattern in concrete_pattern_list:
                print("----- " +concrete_pattern.pattern + " -----")
                syllables = list(set([concrete_pattern.create_syllable(self.alphabet) for i in range(1000)]))
                self.syllables.extend(syllables)
                for s in syllables[:10]:
                   print(s)
        self.syllables = list(set(self.syllables))
        print("number of syllables so far: " + str(len(self.syllables)))

    def create_reduced_patterns(self, pattern_strings, rev):
        """ Pattern strings are onset or coda abstract patterns like "", "C", "CC" etc
        Return list of concrete, reduced patterns: [(A, ["p","t"]), (C, ["f","s"])], such that AC can be built from the provided lists"""
        pattern_list = []
        for pattern_string in pattern_strings:
            for i in range(12 - min(2*len(pattern_string), 11)):
                # 10 leads to about 43000, 63000, 66000, 62000, 42000 syllables
                # 20 leads to about 163456, 185228, 160446, 191942, 208444
                length = len(pattern_string)
                #if length == 0:
                #    continue
                phoneme_sets = random.sample(self.alphabet.sonority_hierarchy.items(), length)
                # reduce some sets
                reduced_phoneme_sets = []
                for cat, pset in phoneme_sets:
                    if random.random() > 0.5:
                        rset = list(sorted(random.sample(pset, random.randint(1, len(pset))), key=lambda x: self.alphabet.sonority(x)))
                    else:
                        rset = pset  # not reduced
                    reduced_phoneme_sets.append((cat, rset))
                reduced_phoneme_sets = sorted(reduced_phoneme_sets, key=lambda d: d[0], reverse=rev)
                # this is a list of tuples of (category, reduced_phoneme_set), ordered by category
                # like: [("A", ["p", "t"]), "D", ["f", "s"])]   (or a,d order reversed)
                if reduced_phoneme_sets not in pattern_list:
                    pattern_list.append(reduced_phoneme_sets)
        return pattern_list

class SyllablePattern:
    """Is a vowel-consonant pattern like CV, V, VC, CVC etc and can generate
    concrete syllables given an alphabet. New: C are replaced by A-F, which stand
    for specific classes of consonants.
    """
    def __init__(self, onset, coda):
        self.onset_arg = onset
        self.coda_arg = coda

        self.onset = "".join([a for a,b in onset])
        self.coda = "".join([a for a, b in coda])
        self.pattern = self.onset + "_V_" + self.coda
        print("SyllablePattern: " + self.pattern)


    def length(self):
        return len(self.pattern)

    def create_syllable(self, alphabet):
        s = ""
        for e, l in self.onset_arg:
            s += random.choice(l)
        s += random.choice(alphabet.vowels)
        for e, l in self.coda_arg:
            s += random.choice(l)
        return s

    def __str__(self):
        return self.pattern

alph = Alphabet()

a = SyllableSet(alph, 0, 2)

total = set()
total.update(a.syllables)
# for i in range(1000):
#     for pattern, concrete_pattern_list in a.syllable_patterns.items():
#         for concrete_pattern in concrete_pattern_list:
#             syllables = [concrete_pattern.create_syllable(a.alphabet) for i in range(10)]
#             total.update(syllables)
#     if i%100==0:
#         print(str(i) + "-------------------------------------")
#         print(len(total))
#         print(sorted(total, key=lambda x:len(x)))
#
sy = list(total)
sy_weights = [math.exp(-len(x)*2) for x in sy]
#sy_weights = [1 for x in sy]
for i in range(100):
    print("".join(random.choices(sy, weights=sy_weights, k=random.randint(1,3))))



