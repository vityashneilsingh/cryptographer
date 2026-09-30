import base64

def base32_text():
  plain_text = input("Enter the plain text: ")
  
  byte_text = plain_text.encode('utf-8')
  
  base32_text = base64.b32encode(byte_text).decode('utf-8')
  
  print(base32_text)
  
def base64_text():
  plain_text = input("Enter the plain text: ")
    
  byte_text = plain_text.encode('utf-8')
    
  base64_text = base64.b64encode(byte_text).decode('utf-8')
  
  print(base64_text)
