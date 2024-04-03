from django.shortcuts import render
from django.http import HttpResponse
from .models import gereradorGrafico
import matplotlib.pyplot as plt
import io
import urllib, base64

# Create your views here.
def home(request):
    # gg = gereradorGrafico.objects.all()
    # #print(gg)
    # print(gg.get_queryset(DependenciaAdministrativa='Municipal'))
    # plt.bar(gg['Creche'], gg.filter(UnidadeGeografica='Nordeste', localizacao='Rural', DependenciaAdministrativa='Municipal'), label='self.colunasFiltro[i]')
    # fig = plt.gcf()
    # buf = io.BytesIO()
    # fig.savefig(buf, format='png')
    # buf.seek(0)
    # string = base64.b64encode(buf.read())
    # uri = urllib.parse.quote(string)
    return render(request, 'index.html')
    # fig, ax = plt.subplots()
    # ax.bar(gg.values_list('Creche', flat=True), gg.values_list('DependenciaAdministrativa', flat=True))
    # ax.set_title('Title of the Graph')
    # ax.set_xlabel('X-axis Label')
    # ax.set_ylabel('Y-axis Label')
    # fig.savefig('static/mygraph.png')
    # return render(request, 'index.html', {'graph_image': 'mygraph.png'})
    #return HttpResponse("Hello Uord!")