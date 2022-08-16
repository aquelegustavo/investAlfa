# Generated by Django 4.1 on 2022-08-16 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0004_company_max_quote_company_min_quote_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.PositiveSmallIntegerField()),
                ('tunnel_min', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tunnel_max', models.DecimalField(decimal_places=2, max_digits=6)),
                ('last_notification', models.DateTimeField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
