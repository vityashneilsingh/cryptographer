def a1z26():
  plain_text = str(input("Enter the plain text(letters): "))
  words = plain_text.lower().split()
  
  
  encoding_characters = {
    'a' : '1',
    'b' : '2',
    'c' : '3', 
    'd' : '4',
    'e' : '5',
    'f' : '6',
    'g' : '7',
    'h' : '8',
    'i' : '9',
    'j' : '10',
    'k' : '11',
    'l' : '12',
    'm' : '13',
    'n' : '14',
    'o' : '15',
    'p' : '16',
    'q' : '17',
    'r' : '18',
    's' : '19',
    't' : '20',
    'u' : '21',
    'v' : '22',
    'w' : '23',
    'x' : '24',
    'y' : '25',
    'z' : '26'
  }
  
  encoded_words = []
  
  for word in words:
    numbers = [encoding_characters[char] for char in word if char in encoding_characters]

    encoded_word = "-".join(numbers)
    encoded_words.append(encoded_word)
        
  final_text = " / ".join(encoded_words)