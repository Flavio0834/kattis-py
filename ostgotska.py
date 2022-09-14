ostgotska = "dae ae ju traeligt va"
rikssvenska = "haer talar vi rikssvenska"

sentence = input()
counter = 0
for word in sentence.split():
    if "ae" in word:
        counter += 1

if counter / len(sentence.split()) >= 0.4:
    print(ostgotska)
else:
    print(rikssvenska)
