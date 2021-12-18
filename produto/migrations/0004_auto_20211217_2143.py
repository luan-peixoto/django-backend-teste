# Generated by Django 3.2.9 on 2021-12-18 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20211205_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='produto',
            name='qtd_estoque',
            field=models.IntegerField(),
        ),
    ]
