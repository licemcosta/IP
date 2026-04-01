musica = input()
qtd_musicas = 0
nome = ""

if musica.lower() != "voa, voa brabuleta":
    qtd_musicas += 1
    nome = musica
    musica1 = input()
    while musica1.lower() != "voa, voa brabuleta":
        qtd_musicas += 1
        nome += " - " + musica1
        musica1 = input()

print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")
print(f"A quantidade de músicas selecionadas foi {qtd_musicas}")
print(f"Setlist de músicas: {nome}")