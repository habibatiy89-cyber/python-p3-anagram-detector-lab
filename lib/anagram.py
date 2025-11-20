# your code here
def find_anagrams(word, candidates):
    sorted_word = sorted(word.lower())
    return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted_word and candidate.lower() != word.lower()]
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        return find_anagrams(self.word, candidates)
