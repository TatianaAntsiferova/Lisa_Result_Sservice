# Generated by Django 4.2.9 on 2024-01-14 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id_author', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id_test', models.IntegerField(primary_key=True, serialize=False)),
                ('right_answer_1', models.IntegerField()),
                ('right_answer_2', models.IntegerField()),
                ('right_answer_3', models.IntegerField()),
                ('max_point', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.author')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_student', models.IntegerField(primary_key=True, serialize=False)),
                ('id_group', models.IntegerField()),
                ('answer_1', models.IntegerField()),
                ('answer_2', models.IntegerField()),
                ('answer_3', models.IntegerField()),
                ('test', models.ManyToManyField(to='main.test')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id_results', models.IntegerField(primary_key=True, serialize=False)),
                ('point_student', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.author')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.student')),
            ],
        ),
    ]
