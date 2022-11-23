#Returns one of the 12 parts of speech
"""
VERB: Verbs (all tenses and modes)
NOUN: Nouns (common and proper)
PRON: Pronouns 
ADJ: Adjectives
ADV: Adverbs
ADP: Adpositions (prepositions and postpositions)
CONJ: Conjunctions
DET: Determiners
NUM: Cardinal numbers
PRT: Particles or other function words
X: Other: foreign words, typos, abbreviations
.: Punctuation
"""
def Simplified_Parts_of_Speech(Word):
  import nltk
  from nltk import pos_tag, word_tokenize
  #nltk.download('punkt')
  #nltk.download('universal_tagset')
  #nltk.download('averaged_perceptron_tagger')
  Tokenized_Word=pos_tag(word_tokenize(Word), tagset='universal')
  Part_Of_Speech=Tokenized_Word[0][1]
  return Part_Of_Speech
Simplified_Parts_of_Speech("and")



#Returns one of the 34 complicated parts of speech
def Complicated_Parts_of_Speech(Word):
  import nltk
  from nltk import pos_tag, word_tokenize
  #nltk.download('punkt')
  Tokenized_Word=pos_tag(word_tokenize(Word))
  Part_Of_Speech=Tokenized_Word[0][1]
  return Part_Of_Speech
Complicated_Parts_of_Speech("and")
