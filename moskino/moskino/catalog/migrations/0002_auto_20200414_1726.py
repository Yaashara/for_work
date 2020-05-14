# Generated by Django 3.0.5 on 2020-04-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mk_event',
            fields=[
                ('name', models.CharField(help_text='Название нового объекта в базе данных.Писать необходимо английскими буквами и с понятной аналогией на название фильма.', max_length=10, primary_key=True, serialize=False, verbose_name='Название в БД')),
                ('title', models.CharField(help_text='Введите название мероприятия', max_length=100, verbose_name='Название на сайте')),
                ('event_date', models.DateField(blank=True, help_text='Введите запланированную дату проведения мероприятия', null=True, verbose_name='Дата проведения мероприятия')),
                ('event_place', models.CharField(blank=True, help_text='Введите месот, где будет проведено мероприятие', max_length=100, null=True, verbose_name='Место проведения меропритиятия')),
                ('date', models.DateField(blank=True, help_text='Введите дату проведения мероприятия', null=True, verbose_name='Дата проведения мероаприятия')),
                ('start_time', models.TimeField(blank=True, help_text='Введите время начала мероприятия', null=True, verbose_name='Время начала мероаприятия')),
                ('description', models.TextField(blank=True, help_text='Введите описание мероприятия', max_length=600, null=True, verbose_name='Описание мероприятия')),
                ('short_description', models.TextField(blank=True, help_text='Введите краткое описание, которое будет отображаться в блоке Премьера и Постере мероприятия', max_length=100, null=True, verbose_name='Краткое описание мероприятия')),
                ('in_premiere', models.CharField(choices=[('Да', 'Отобразить в блоке'), ('Нет', 'Не отображать в блоке')], default='Нет', max_length=3, verbose_name='Отображать ли фильм в блоке "Премьеры"')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='mk_film',
            fields=[
                ('name', models.CharField(help_text='Название нового объекта в базе данных.Писать необходимо английскими буквами и с понятной аналогией на название фильма.', max_length=10, primary_key=True, serialize=False, verbose_name='Название в БД')),
                ('title', models.CharField(help_text='Введите название фильма', max_length=100, verbose_name='Название на сайте')),
                ('film_producer', models.CharField(blank=True, help_text='Введите имя режиссёра', max_length=100, null=True, verbose_name='Режиссёр')),
                ('date_of_release', models.DateField(blank=True, help_text='Введите год релиза фильма', null=True, verbose_name='Год релиза')),
                ('film_country', models.CharField(blank=True, help_text='Введите страну производства фильма', max_length=100, verbose_name='Страна производства фильма')),
                ('film_duration', models.DurationField(help_text='введите длительность фильма', verbose_name='Длительность фильма')),
                ('description', models.TextField(blank=True, help_text='Введите описание фильма', max_length=1000, null=True, verbose_name='Описание фильма')),
                ('short_description', models.TextField(blank=True, help_text='Введите краткое описание фильма, которое будет отображаться в блоке премьеры и постера', max_length=100, null=True, verbose_name='Краткое описание фильма')),
                ('in_premiere', models.CharField(choices=[('Да', 'Отобразить в блоке'), ('Нет', 'Не отображать в блоке')], default='Нет', max_length=3, verbose_name='Отображать ли фильм в блоке "Премьеры"')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Введите заголовок новости', max_length=100, verbose_name='Заголовок новости')),
                ('lead', models.CharField(help_text='Введите лид новости', max_length=100, verbose_name='Лид новости')),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, help_text='Введите текст новости', max_length=600, null=True, verbose_name='Новость')),
            ],
        ),
        migrations.DeleteModel(
            name='Film',
        ),
    ]