#Returns a string as a list with only words
def List_Words(Words):
  import nltk
  ###nltk.download('punkt')
  WordsListTransfer=nltk.word_tokenize(Words)
  WordsList=[]
  C=0
  LWordsListTransfer=len(WordsListTransfer)
  while (C<LWordsListTransfer):
    Listing=[]
    Append=WordsListTransfer[C]
    if (Append=="." or Append==","):
      C=C+1
      continue
    Listing.append(Append)
    WordsList.append(Listing)
    C=C+1
  return WordsList
List_Words("In trigonometry, trigonometric identities are equalities that involve trigonometric functions and are true for every value of the occurring variables for which both sides of the equality are defined. Geometrically, these are identities involving certain functions of one or more angles. They are distinct from triangle identities, which are identities potentially involving angles but also involving side lengths or other lengths of a triangle.")
