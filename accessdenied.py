longueur = 0
temps = 5
pasfini = True
while temps == 5 and pasfini:
    longueur += 1
    print(longueur * '0')
    reponse = input()
    if reponse == 'ACCESS GRANTED':
        pasfini = False
    else:
        temps = int(reponse[15:-4])
caracteres = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
mot = longueur * '0'
i = 0
t = temps
while i < longueur and pasfini:
    b = True
    j = 0
    while b and j < len(caracteres):
        mot = mot[:i] + caracteres[j] + mot[i + 1:]
        print(mot)
        reponse = input()
        if reponse == 'ACCESS GRANTED':
            b = False
            pasfini = False
        else:
            temps = int(reponse[15:-4])
            if temps > t:
                b = False
                t = temps
            elif temps < t:
                b = False
                mot = mot[:i] + '0' + mot[i + 1:]
        j += 1
    i += 1