def Simplified_Parts_Of_Speech(Word):
  import nltk
  from nltk import pos_tag, word_tokenize
  #nltk.download('punkt')
  #nltk.download('universal_tagset')
  #nltk.download('averaged_perceptron_tagger')
  Tokenized_Word=pos_tag(word_tokenize(Word), tagset='universal')
  Part_Of_Speech=Tokenized_Word[0][1]
  return Part_Of_Speech


def Complicated_Parts_Of_Speech(Word):
  import nltk
  from nltk import pos_tag, word_tokenize
  #nltk.download('punkt')
  Tokenized_Word=pos_tag(word_tokenize(Word))
  Part_Of_Speech=Tokenized_Word[0][1]
  return Part_Of_Speech
