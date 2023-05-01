# 18 – Faça um programa que receba uma frase e junte as palavras (retirando todos os
# espaços em branco)

phrase = input("Type a phrase: ")

if ' ' in phrase:
    new_phrase = [letter for letter in phrase
                  if letter.strip()
                  ]
    new_phrase = ''.join(new_phrase)
    print(new_phrase)
else:
    print("This isn't a phrase.")



