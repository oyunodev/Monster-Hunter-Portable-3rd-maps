from PIL import Image

print("Selecione um número equivalente ao mapa que você deseja: ")
print("[1] - Mountain Stream")
print("[2] - Flooded Forest")
print("[3] - Sandy Plains")
print("[4] - Deserted Island")
print("[5] - Thundra")
print("[6] - Volcano")



mapa = int(input())

if mapa == 1:
    image = Image.open("source/mountainstream.webp")
    image.show()
elif mapa == 2:
    image = Image.open("source/FloodedForestA-1.webp")
    image.show()
elif mapa == 3:
    image = Image.open("source/SandyPlainsA.webp")
    image.show()
elif mapa == 4:
    image = Image.open("source/DesertedIslandA.webp")
    image.show()
elif mapa == 5:
    image = Image.open("source/TundraA.webp")
    image.show()
elif mapa == 6:
    image = Image.open("source/VC.webp")
    image.show()
else:
    print("Você não digitou uma entrada válida")


