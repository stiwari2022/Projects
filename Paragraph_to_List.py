def Paragraph_to_List(Paragraph):
  # Define the characters to be removed
  chars_to_remove = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", ";", ":", ",", "."]
  # Remove the specified characters from the string
  Paragraph = ''.join(char for char in Paragraph if char not in chars_to_remove)
  #Remove characters that arn't letters and split a string into words
  return [each_word for each_word in Paragraph.split() if each_word.isalpha()]
