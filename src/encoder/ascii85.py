import base64

def ascii85():
  
  plain_text = input("Enter the plain text: ")
  
  hex_text = base64.a85encode(plain_text.encode('utf-8')).hex(' ')
  
  print(hex_text)
