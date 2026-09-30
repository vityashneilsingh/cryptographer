def alphabetical_cipher():
  
  normal_alphabet = str(input("Enter the alphabets: "))
  
  substituting_alphabet = str(input("Enter the substituting alphabets: "))
  
  plain_text = input("Enter the plain text: ")
  
  substituted_text_list = []
  
  for char in plain_text:
    lower_char = char.lower()
        
    if lower_char in normal_alphabet:
      index = normal_alphabet.index(lower_char)
            
      sub_char = substituting_alphabet[index]
            
      if char.isupper():
        substituted_text_list.append(sub_char.upper())
      else:
        substituted_text_list.append(sub_char)
    else:
      substituted_text_list.append(char)

  cipher_text = "".join(substituted_text_list)
  print(cipher_text)