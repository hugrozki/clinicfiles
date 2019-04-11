# Generated by Django 2.2 on 2019-04-11 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre de usuario')),
                ('no_expediente', models.IntegerField(verbose_name='Número de expediente')),
                ('fecha_ultima_consulta', models.DateField(verbose_name='Fecha de última consulta')),
                ('tipo_sangre', models.CharField(max_length=3, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('open_date', models.DateField(verbose_name='Fecha de alta')),
                ('medicine', models.CharField(max_length=50, verbose_name='Medicamento')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergies', to='accounts.Account')),
            ],
        ),
    ]
