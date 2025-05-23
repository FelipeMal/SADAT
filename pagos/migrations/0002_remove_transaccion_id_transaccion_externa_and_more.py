# Generated by Django 4.2.7 on 2025-04-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaccion',
            name='id_transaccion_externa',
        ),
        migrations.AddField(
            model_name='transaccion',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='stripe_payment_intent_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='transaccion',
            name='stripe_payment_method_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='metodo_pago',
            field=models.CharField(choices=[('card', 'Tarjeta de Crédito/Débito'), ('transfer', 'Transferencia Bancaria')], max_length=50, null=True),
        ),
    ]
