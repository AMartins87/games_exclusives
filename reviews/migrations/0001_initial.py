# Generated by Django 3.2 on 2022-09-29 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        ('profiles', '0002_auto_20220928_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('reviews', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]