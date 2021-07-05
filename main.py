import hashlib
def main():
  text ="cyber scurity"
  textUtf8 = text.encode("utf-8")

  hash = hashlib.md5(textUtf8)
  hexa = hash.hexdigest()

  print (hexa)

  return
main()

import hashlib
text = "cyber security"
x = hashlib.md5(text.encode("utf-8")).hexdigest()
print(x)

import hashlib
text = "cyber security"
x = hashlib.sha256(text.encode("utf-8")).hexdigest()
print(x)

import hashlib
text = "cyber security"
x = hashlib.sha512(text.encode("utf-8")).hexdigest()
print(x)
