vowels = ["a", "e", "i", "o", "u"]
strr = "hello world"

for x in strr:
    if x in vowels:
        strrUpdate = strr.replace(x, "")
print(strrUpdate)
