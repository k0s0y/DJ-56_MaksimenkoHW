# Generated by Django 4.1.2 on 2022-12-03 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('articles', models.ManyToManyField(related_name='tags', to='articles.article')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Тематика статьи',
                'verbose_name_plural': 'Тематика статьи',
            },
        ),
    ]
