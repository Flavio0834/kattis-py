tonalities = {
    "C": "UNIQUE",
    "C#": "Db",
    "Db": "C#",
    "D": "UNIQUE",
    "D#": "Eb",
    "Eb": "D#",
    "E": "UNIQUE",
    "F": "UNIQUE",
    "F#": "Gb",
    "Gb": "F#",
    "G": "UNIQUE",
    "G#": "Ab",
    "Ab": "G#",
    "A": "UNIQUE",
    "A#": "Bb",
    "Bb": "A#",
    "B": "UNIQUE",
}

i = 1
while True:
    try:
        tonality, major_minor = input().split()
        if tonalities[tonality] == "UNIQUE":
            print(f"Case {i}: UNIQUE")
        else:
            print(f"Case {i}: {tonalities[tonality]} {major_minor}")
        i += 1
    except:
        break
