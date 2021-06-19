# Generated by Django 3.1.1 on 2020-10-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='food',
            field=models.FloatField(default=0, verbose_name='FOOD'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='healthcare',
            field=models.FloatField(default=0, verbose_name='HEALTHCARE'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='housing',
            field=models.FloatField(default=0, verbose_name='HOUSING'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='income',
            field=models.FloatField(default=0, verbose_name='INCOME'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='miscellaneous',
            field=models.FloatField(default=0, verbose_name='MISCELLANEOUS'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='recreation',
            field=models.FloatField(default=0, verbose_name='RECREATION'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='savings',
            field=models.FloatField(default=0, verbose_name='SAVINGS'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='totalExpenditure',
            field=models.FloatField(default=0, verbose_name='TOTAL EXPENDITURE'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='totalTransactions',
            field=models.IntegerField(default=0, verbose_name='TOTAL TRANSACTIONS'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='transportation',
            field=models.FloatField(default=0, verbose_name='TRANSPORTATION'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0, verbose_name='AMOUNT'),
        ),
    ]