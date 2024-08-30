class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, words_list):
        return [word for word in words_list if self._is_it_anagram(word)]

    def _is_it_anagram(self, word):
        return ''.join(sorted(word)) == self.sorted_word
    pass