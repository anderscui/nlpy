import nltk
from nltk.corpus import words


def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)


if __name__ == '__main__':
    t = '''
        I'm a programmer using Python (sometimes).
        Hello, Wold.
        Read mmore about my program, OK?
        '''

    print(unusual_words(nltk.word_tokenize(t)))