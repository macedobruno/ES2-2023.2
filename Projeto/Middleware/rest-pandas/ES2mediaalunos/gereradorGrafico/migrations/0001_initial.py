# Generated by Django 5.0.3 on 2024-03-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gereradorGrafico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ano', models.CharField(max_length=4)),
                ('UnidadeGeografica', models.CharField(choices=[('BR', 'Brasil'), ('NE', 'Nordeste')], max_length=8)),
                ('localizacao', models.CharField(choices=[('UR', 'Urbana'), ('RU', 'Rural')], max_length=6)),
                ('DependenciaAdministrativa', models.CharField(choices=[('PU', 'Pública'), ('PR', 'Privada'), ('MU', 'Municipal'), ('ES', 'Estadual'), ('FE', 'Federal')], max_length=7)),
                ('Creche', models.DecimalField(decimal_places=1, max_digits=3)),
                ('PreEscola', models.DecimalField(decimal_places=1, max_digits=3)),
                ('AnosIniciais', models.DecimalField(decimal_places=1, max_digits=3)),
                ('AnosFinais', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_1Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_2Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_3Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_4Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_5Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_6Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_7Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_8Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_9Ano', models.DecimalField(decimal_places=1, max_digits=3)),
                ('TurmasMultietapa', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_1Serie', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_2Serie', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_3Serie', models.DecimalField(decimal_places=1, max_digits=3)),
                ('_4Serie', models.DecimalField(decimal_places=1, max_digits=3)),
                ('NaoSeriado', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]