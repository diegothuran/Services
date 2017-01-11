# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf_cnpj', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Oredem_de_Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('observacao', models.TextField()),
                ('contato', models.CharField(blank=True, max_length=200)),
                ('fone', models.CharField(blank=True, max_length=20)),
                ('agencia', models.CharField(blank=True, max_length=200)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceOrdering.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='oredem_de_servico',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceOrdering.Servico'),
        ),
        migrations.AddField(
            model_name='oredem_de_servico',
            name='tecnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiceOrdering.Tecnico'),
        ),
    ]
