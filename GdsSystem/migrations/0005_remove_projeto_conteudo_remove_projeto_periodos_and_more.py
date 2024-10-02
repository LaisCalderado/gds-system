# Generated by Django 5.0.2 on 2024-04-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GdsSystem', '0004_projeto_acontecimento_projeto_local_projeto_tipo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='conteudo',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='periodos',
        ),
        migrations.AddField(
            model_name='projeto',
            name='perigo',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
