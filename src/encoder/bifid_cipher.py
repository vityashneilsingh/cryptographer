def bifid_cipher():
  plain_text = str(input("Enter the plain text: ")).upper().replace("J", "I")
  
  alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  
  keyword = input("Enter the keyword: ").upper().replace("J", "I")
  
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

  ciphered_numbers_rows = []
  ciphered_numbers_column = []

  for char in plain_text:
    for r in range(5):
      for c in range(5):
        if polybius_square[r][c] == char:
          ciphered_numbers_rows.append(str(r))
          ciphered_numbers_column.append(str(c))
  
  ciphered_numbers = ciphered_numbers_rows + ciphered_numbers_column
  ciphered_numbers_str = "".join(ciphered_numbers)
        
  cipher_text_list = []
  for i in range(0, len(ciphered_numbers_str), 2):
    r = int(ciphered_numbers_str[i])
    c = int(ciphered_numbers_str[i + 1])
    letter = polybius_square[r][c] 
    cipher_text_list.append(letter)

  cipher_text = "".join(cipher_text_list) 
  print(cipher_text)      
