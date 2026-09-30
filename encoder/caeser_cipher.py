def keyword_caeser_cipher():
  plain_text = input("Enter the plain text: ").upper().replace(" ", "")
  keyword = input("Enter the keyword: ").upper()
  
  alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  refence_text = []
  for char in keyword:
    if char not in refence_text and char.isalpha():
      refence_text.append(char)
  for char in alphabets:
    if char not in refence_text:
          refence_text.append(char)
          
  cipher_text_list = []
  for char in plain_text:
    if char in alphabets:
      i = alphabets.index(char)
      cipher_text_list.append(refence_text[i])

  print(cipher_text_list)

def normal_caesar_cipher():
    plain_text = input("Enter the plain text: ").upper()
    shift = int(input("Enter shift value (e.g., 3): "))
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher_text_list = []
    
    for char in plain_text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + shift) % 26
            cipher_text_list.append(alphabet[new_index])
        else:
            cipher_text_list.append(char)
            
    print(cipher_text_list)
