import uuid
from datetime import datetime
from django.db import models

# Тестовая модель объекта ФИЛЬМ


class Genre(models.Model):
    """
    Данная модель определяет возможные жанры фильмов
    """

    genre_name = models.CharField(
        max_length = 200,
        help_text = "Введите название жанра фильма (боевик, вестерн, драма и т.д.)",
        unique = True
    )

    def __str__(self):
        return  self.genre_name

class mk_film(models.Model):
    """
    Структура данных для фильмов в прокате
    """
    #Функция автоматического определения
    
    #Функция валидации значения при определении приоритета
    #def validate(self):


    #Поля для администраторов

    film_id = models.AutoField(
        "Идентификатор фильма",
        primary_key = True
    )

    creation_date = models.DateTimeField(
        "Дата создания записи",
        auto_now = True,
        editable = False
    )

    last_change_date = models.DateTimeField(
        "Дата и время последнего изменения записи",
        auto_now = True,
    )

    on_screen_till = models.DateField(
        "Дата снятия с проката",
        default = "13.05.2020"

    )

    PRIORTIES = (
        (0, "Обычный"),
        (1, "Высокий"),
        (2, "Наивысший"),
    )

    priority_mark = models.CharField(
        max_length = 1,
        choices = PRIORTIES,
        balnk = True,
        default = 0,

    )


    """
    временно отключенное поле, в котором будет хранится информация о создавшем пользователе
    last_change_user = models.OneToOneField(
        "Кто вноосил последние изменения"
    )

    film_name = models.CharField(
        "Название фильма",
        max_length = 200,
        help_text = "Введите название фильма",

    )
    """
    #Поля, на основе которых настраиваются фильтры и т.д.


    #Поля, которые вияют на то, что видят пользователи


    #Метаданные

    class Meta:
        ordering = ["name"]

    #Методы

    def __str__(self):
        return "{0}, {1}".format(self.name, self.short_description)



class mk_event(models.Model):

    #Переменные для полей с выбором
    f_var = "Да"
    s_var = "Нет"
    in_premiere_vars = [
        (f_var, "Отобразить в блоке"),
        (s_var, "Не отображать в блоке"),
    ]

    #Поля

    name = models.CharField("Название в БД",  #id под которым элемент хранится в БД
                            primary_key = True,
                            max_length = 10,
                            help_text = "Название нового объекта в базе данных.Писать необходимо английскими буквами и с понятной аналогией на название фильма."
                            )

    title = models.CharField("Название на сайте",
                             max_length = 100,
                             help_text = "Введите название мероприятия"
                             )


    event_date = models.DateField("Дата проведения мероприятия",
                                  help_text = "Введите запланированную дату проведения мероприятия",
                                  null = True,
                                  blank = True
                                  )

    event_place = models.CharField("Место проведения меропритиятия",
                                   max_length = 100,
                                   help_text = "Введите месот, где будет проведено мероприятие",
                                   null = True,
                                   blank = True
                                   )

    date = models.DateField("Дата проведения мероаприятия",
                            help_text = "Введите дату проведения мероприятия",
                            null = True,
                            blank = True
                            )

    start_time = models.TimeField("Время начала мероаприятия",
                                  help_text="Введите время начала мероприятия",
                                  null=True,
                                  blank=True
                                  )

    description = models.TextField("Описание мероприятия",
                                   help_text = "Введите описание мероприятия",
                                   null = True,
                                   blank = True,
                                   max_length = 600
                                   )

    short_description = models.TextField("Краткое описание мероприятия",
                                         help_text = "Введите краткое описание, которое будет отображаться в блоке Премьера и Постере мероприятия",
                                         null = True,
                                         blank = True,
                                         max_length = 100
                                         )

    in_premiere = models.CharField('Отображать ли фильм в блоке "Премьеры"',
                                   max_length = 3,
                                   choices = in_premiere_vars,
                                   default = s_var)


    class Meta:
        ordering = ["name"]

    #Методы

    def __str__(self):
        return "{0}, {1}".format(self.name, self.short_description)


class News(models.Model):

    #Поля

    ID = models.AutoField(primary_key = True,
                          editable = False)

    title = models.CharField("Заголовок новости",
                             max_length = 100,
                             help_text = "Введите заголовок новости"
                             )

    lead = models.CharField("Лид новости",
                            max_length = 100,
                            help_text="Введите лид новости"
                            )

    date = models.DateField(editable = False,
                            auto_now_add = True
                            )

    description = models.TextField("Новость",
                                   help_text = "Введите текст новости",
                                   null = True,
                                   blank = True,
                                   max_length = 600
                                   )






































