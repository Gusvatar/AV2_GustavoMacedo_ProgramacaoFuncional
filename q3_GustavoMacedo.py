from PIL import Image


ajustaPixel = lambda pixel, fator: tuple(min(int(component * fator), 255) for component in pixel)
ajustaDados = lambda imagem, fator: [ajustaPixel(pixel, fator) for pixel in imagem.getdata()]


imagemPath = 'C:/Users/gusta/Desktop/baiacu1.jpg'  # Coloque o path da imagem.jpg
imagem = Image.open(imagemPath)


fatorBrilho = float(input("Informe o fator de brilho (ex. 1.5 para aumentar o brilho, 0.5 para diminuir o brilho): "))


imagemClareada = Image.new('RGB', imagem.size)
imagemClareada.putdata(ajustaDados(imagem, fatorBrilho))

imagemClareada.show() #mostra a imagem