from nltk.tag import pos_tag
from nltk import word_tokenize, sent_tokenize
from nltk.text import Text
import string

class Analyser:
    def __init__(self, text):
        if not text:
            raise ValueError("The text cannot be empty.")

        self.text = text

    def pre_traitement(self):
        self.tokens = word_tokenize(self.text)
        self.num_tokens = len(self.tokens)
        self.sentences = sent_tokenize(self.text)
        self.text = Text(self.tokens)
        return self.tokens, self.sentences, self.num_tokens


    def number_of_words(self):
        """Separates tokens from words"""
        self.words, self.punctuation = [], []

        for token in self.text:
            if token in string.punctuation:
                self.punctuation.append(token)
            else:
                self.words.append(token)

        """Int of words"""
        self.num_words = len(self.words)


    def letters_per_words(self):
        """Sum number of letters per words"""
        self.letters = "".join(self.words)
        self.letters_words = (len(self.letters)/self.num_words)


    def number_of_sentences(self):
        """Counts len of sentences in each text."""
        self.num_sentences = len(self.sentences)


    def words_per_sentences(self):
        """Returns the moyenne of words per sentence."""
        self.words_sentences = self.num_words/self.num_sentences


    def lexical_diversity(self):
        """Lexical diversity for both texts."""
        # Method from Natural Language Processing with Python
        self.lex_div = len(self.words)/len((set(self.words)))


    def pos_tagging(self):
        """POS tag on both texts"""
        self.data = {
            "NOUN" : 0,
            "VERB" : 0,
            "ADJ" : 0,
            "ADV" : 0,
            "PRON" : 0,
            "DET" : 0,
            "ADP" : 0,
            "CONJ" : 0,
            "NUM" : 0,
            "PRT" : 0,
            }

        self.tag = pos_tag(self.words, tagset="universal")

        for _, category in self.tag:
            if category in self.data:
                self.data[category]+=1

    def analyse(self):
        """Starts the analysis"""
        self.pre_traitement()
        self.number_of_words()
        self.letters_per_words()
        self.number_of_sentences()
        self.words_per_sentences()
        self.lexical_diversity()
        self.pos_tagging()