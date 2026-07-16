#python filename.py
# apple --> ppl
# twitter --> twttr
# hello --> hll
vowls = ["a","e","i","o","u","A","E","I","O","U"]
text = input("text: ")
for i in text:
    if i in vowls:
        text = text.replace(i,"")

print(text)

