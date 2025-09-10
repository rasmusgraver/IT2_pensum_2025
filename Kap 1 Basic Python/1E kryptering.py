krypter = {
    "a": "c", "b": "d", "c": "e", "d": "f", "e": "g", 
    "f": "h", "g": "i", "h": "j", "i": "k", "j": "l", 
    "k": "m", "l": "n", "m": "o", "n": "p", "o": "q", 
    "p": "r", "q": "s", "r": "t", "s": "u", "t": "v", 
    "u": "w", "v": "x", "w": "y", "x": "z", "y": "æ", 
    "z": "ø", "æ": "å", "ø": "a", "å": "b", " ": " "
}

tekst = "Ordbøker er både moro og spennende."
kryptert = ""

for b in tekst:
    # print(b, end=":")
    try:
        # print(krypter[b])
        # TODO: Bør håndtere store bokstaver bedre
        kryptert += krypter[b]
    except KeyError:
        # print("fant ikke")
        # Hvis ikke jeg finner bokstaven i dictionary
        # så legger jeg den til som den er:
        kryptert += b

print("Kryptert tekst:", kryptert)
