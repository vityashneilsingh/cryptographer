import sys
from encoder.a1z26 import a1z26
from encoder.adfvx_cipher import adfgvx_cipher
from encoder.affine_cipher import affine_cipher
from encoder.alphabetical_cipher import alphabetical_cipher 
from encoder.ascii85 import ascii85
from encoder.bacon_code import bacon_cipher
from encoder.base32_or_base64 import base32_text, base64_text
from encoder.bifid_cipher import bifid_cipher
from encoder.caeser_cipher import keyword_caeser_cipher, normal_caesar_cipher
from encoder.morse_code import morse_code
from encoder.nihilist_cipher import nihilist_cipher

print('''
      ==========================================================
                            Cryptographer
      ==========================================================
      
      1. Encoder
      2. Exit
      ''')
user_input = int(input("What you want to do? "))
  
if user_input == 2:
  sys.exit()
if user_input == 1:
  
  print('''
         ==========================================================
                            Cryptographer
        ==========================================================
        
        The types of available ciphers/encoders:
        1. a1z26
        2. ADFVX Cipher
        3. Affine Cipher
        4. Alphabetical Cipher
        5. ASCII85
        6. Bacon Cipher
        7. Base32
        8. Base64
        9. Bifid Cipher
        10. Caeser Cipher
        11. Morse Code
        12. Nihilist Cipher
        13. Exit
        ''')
  user_input_encoder = int(input("What you want to do? "))
  
def error_msg():
    return sys.exit("Unknown command.")

encoding_type = {
      1 : a1z26,
      2 : adfgvx_cipher,
      3 : affine_cipher,
      4 : alphabetical_cipher,
      5 : ascii85,
      6 : bacon_cipher,
      7 : base32_text,
      8 : base64_text,
      9 : bifid_cipher,
      10 : normal_caesar_cipher,
      11 : keyword_caeser_cipher,
      12 : morse_code,
      13 : nihilist_cipher,
      14 : sys.exit("Unknown Command!")
    }
