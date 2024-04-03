import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    #cria buffer e salva a imagem em png
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    #salva os dados da imagem do buffer
    image_png = buffer.getvalue()

    #encoda e decoda a imagem
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    #remove buffer
    buffer.close()

    #retorna imagem
    return graph

def get_plot(x,y):
    pass