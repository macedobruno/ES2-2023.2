from typing import Any
import pandas as pd
from django.core.management.base import BaseCommand
from gereradorGrafico.models import gereradorGrafico

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        
        # carrega tabela ao DataFrame do Pandas
        tabela_file = "ATU_BRASIL_REGIOES_UFS_2023_ALTERADO4.ods"
        df = pd.read_excel(tabela_file,engine="odf")
        df.columns = df.columns.str.strip()
        
        # converte as colunas que são float
        for i in df.columns[4:]:
            df[i] = df[i].astype(float)
        
        # remove linhas contendo "Total" em 'Localização' e 'Dependência Administrativa'
        df = df[df['Localizacao'].map(lambda x: str(x)!="Total")]
        df = df[df['Dependencia Administrativa'].map(lambda x: str(x)!="Total")]
        
        # remove colunas com "Total 1", "Total"
        #df.drop(["Total 1", "Total"], axis=1, inplace=True)#, "Ano", "Unidade Geográfica", "Localização", "Dependência Administrativa", "Creche", "Pré-Escola", "Anos Iniciais", "Anos Finais"], axis=1, inplace=True)

        gereradorGrafico.objects.bulk_create([
            gereradorGrafico(Ano=row['Ano'], UnidadeGeografica=row['Unidade Geografica'], localizacao=row['Localizacao'], DependenciaAdministrativa=row['Dependencia Administrativa'], Creche=row['Creche'], PreEscola=row['PreEscola'], AnosIniciais=row['Anos Iniciais'], AnosFinais=row['Anos Finais'], _1Ano=row['1o ano'], _2Ano=row['2o ano'], _3Ano=row['3o ano'], _4Ano=row['4o ano'], _5Ano=row['5o ano'], _6Ano=row['6o ano'], _7Ano=row['7o ano'], _8Ano=row['8o ano'], _9Ano=row['9o ano'], TurmasMultietapa=row['Turmas Multietapa Multi ou Correcao de Fluxo 2'], _1Serie=row['1a serie'], _2Serie=row['2a serie'], _3Serie=row['3a serie'], _4Serie=row['4a serie'], NaoSeriado=row['NaoSeriado']) for _, row in df.iterrows()
        ])