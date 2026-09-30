def adfgvx_cipher():
  plain_text = str(input("Enter the plain text: ")).upper().replace(" ", "")
  key = str(input("Enter a key: ")).upper()
  
  headers = ['A', 'D', 'F', 'G', 'V', 'X']
  encoding_array = [
    ['P', 'H', '0', 'Q', 'G', '6'],
    ['4', 'M', 'E', 'A', '1', 'Y'],
    ['L', '2', 'N', 'O', 'F', 'D'],
    ['X', 'K', 'R', '3', 'C', 'V'],
    ['S', '5', 'Z', 'W', '7', 'B'],
    ['J', '9', 'U', 'T', '8', 'I']
  ]
  encoded_text = ""
  
  for char in plain_text:
    for i in range(6):
            for j in range(6):
                if encoding_array[i][j] == char:
                  encoded_text += headers[i] + headers[j]
  
  grid = {i: [] for i in range(len(key))}
  
  
  for idx, char in enumerate(encoded_text):
    col_index = idx % len(key)
    grid[col_index].append(char)
    
  sorted_indices = sorted(range(len(key)), key=lambda k: key[k])
  
  final_encoded_text = ""
  for col_index in sorted_indices:
      final_encoded_text += "".join(grid[col_index])

  print("Final Cipher Text:", final_encoded_text)