import sys
import math

def affine_cipher():
  #E(x) = (ax + b)(mod m)
  m_str = str(input("Enter the alphabets(Mininmum alphabets should be 2): "))
  m = len(m_str)
  
  if m<2:
    sys.exit("Invalid Input of alphabets")
  
  a = int(input(f"Enter the slope(Less then {m} and co-prime with {m}): "))
  if a<0 or a>=m or math.gcd(a, m) != 1:
    sys.exit("Invalid Input of slope!")  
    
  b = int(input(f"Enter the shift/constant(can't be greater than or equal to {m} or 0): "))
  if b<=0 or b>= m:
    sys.exit("Invalid Input of shift!")

  plain_text = str(input("Enter the plain text: "))
  
  cipher_text_list = []
  
  for char in plain_text:
    
    lower_char = char.lower()  
      
    if lower_char in m_str:
      
      x = m_str.index(lower_char)
      
      cipher_index = (a * x + b) % m
      
      cipher_char = m_str[cipher_index]
      
      if char.isupper():
        cipher_text_list.append(cipher_char.upper())
        
      else:
        cipher_text_list.append(cipher_char)
        
    else:
      cipher_text_list.append(char)
      
  cipher_text = "".join(cipher_text_list)
  print("Ciphered text: ", cipher_text)