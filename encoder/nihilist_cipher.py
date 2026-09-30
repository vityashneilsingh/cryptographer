def nihilist_cipher():
  plain_text = input("Enter the plain text: ").upper().replace("J", "I")
  keyword = input("Enter the keyword: ").upper().replace("J", "I")
  numerical_keyowrd = input("Enter the second keyword: ").replace("J", "I")
  alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  
  polybius_square_list = []
    
  for char in keyword:
    if char not in polybius_square_list and char.isalpha():
      polybius_square_list.append(char)
  for char in alphabets:
    if char not in polybius_square_list:
      polybius_square_list.append(char)
        
  polybius_square = []
  
  for i in range(0, 25, 5): 
    row = polybius_square_list[i : i + 5]
    polybius_square.append(row)
    
  cipher_numberlist_keywords = []
  cipher_numberlist_alphabets = []
        
  for char in plain_text:
    if char.isalpha():
      for r in range(5):
        for c in range(5):
          if polybius_square[r][c] == char:
            lst = f"{r + 1}{c + 1}"
            cipher_numberlist_alphabets.append(lst)
  
  for char in numerical_keyowrd:
    if char.isalpha():
      for r in range(5):
        for c in range(5):
          if polybius_square[r][c] == char:
            lst = f"{r + 1}{c + 1}"
            cipher_numberlist_keywords.append(lst)

  cipher_text = []
  number_key_coords = len(cipher_numberlist_keywords)  
  
  for i in range(len(cipher_numberlist_alphabets)):
        plain_num = int(cipher_numberlist_alphabets[i])
        key_num = int(cipher_numberlist_keywords[i % number_key_coords])
        summed_value = plain_num + key_num
        cipher_text.append(summed_value)
        
  print(cipher_text)
