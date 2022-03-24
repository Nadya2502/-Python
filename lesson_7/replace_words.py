class Solution(object):
    def replaceWords(self, dictionary, sentence):

        sentence_word = sentence.split(" ")
        for word in sentence_word:
            for dic in dictionary:
                if word.find(dic) == 0:
                    sentence = sentence.replace(word, dic, 1)
                    word = dic

        return sentence