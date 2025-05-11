# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def is_anagram(self, other_word):
        other = other_word.lower()
        return sorted(self.word) == sorted(other) and self.word != other

    def match(self, words):
        return [word for word in words if self.is_anagram(word)]
