frase = "Está é a frase que vamos checar as ocorrências da palavra frase"

print(frase.count("frase"))

if frase.count("frase") == 2:
    print("A contagem está correta!")

print(frase.find("checar"))

if frase.find("frase") >= 0:
    print("Encontrei!!!!!!!!!!!")