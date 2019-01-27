import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from support import parts_of_speech



def generate_tags(mail):
    """Generate keywords for the string passed"""
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(mail)

    punctuation = [',', '.', '!', ';', '-', '(', ')']
    filtered_sentence = []

    # Removing stop words and punctuation
    for word in words:
        if word not in stop_words:
            if word not in punctuation:
                filtered_sentence.append(word)

    # Keeping only nouns verbs adjectives
    tagged = nltk.pos_tag(filtered_sentence) # list of tuples
    final_list = []
    for tag in tagged:
        if tag[1] in parts_of_speech:
            final_list.append(tag[0])
    return final_list