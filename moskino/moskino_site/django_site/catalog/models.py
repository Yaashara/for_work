from datetime import datetime
from django.db import models


# Тестовая модель объекта ФИЛЬМ


class Genre(models.Model):
    """
    Данная модель определяет возможные жанры фильмов, должен быть выбор нескольких вариантов
    """

    genre_name = models.CharField(
        max_length = 50,
        help_text = "Введите название жанра фильма (боевик, вестерн, драма и т.д.)",
        unique = True
    )

    def __str__(self):
        return self.genre_name


class mk_film(models.Model):
    """
    Структура данных для фильмов в прокате
    """
    # Поля для администраторов

    #Функция валидации значения при определении приоритета
    #Пока в проекте
    #def validate(self):

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
        auto_now = True
    )

    on_screen_till = models.DateField(
        "Дата снятия с проката",
        auto_now = True,
        blank = True,
        null = True,
    )

    PRIORTIES = (
        ("О", "Обычный"),
        ("В", "Высокий"),
        ("Н", "Наивысший"),
    )

    priority_mark = models.CharField(
        "Метка приоритета",
        max_length = 1,
        choices = PRIORTIES,
        blank = True,
        default = "О",
    )

    # Поля, на основе которых настраиваются фильтры и т.д.

    # Поля, которые вияют на то, что видят пользователи

    name = models.CharField(
        "Название фильма",
        max_length = 50,
        blank = True,
        help_text = "Введите название фильма"

    )

    title = models.CharField(
        "Название фильма на главной странице сайта",
        max_length=100,
        help_text="Введите название фильма",
        blank = True,
        null = True
    )

    short_description = models.TextField(
        "Краткое описание фильма",
        max_length = 500,
        blank = True,
        null = True,
        help_text = "Введите краткое описание фильма"
    )

    """ 
    Заблокированы, пока нет чёткой структуры хранения
        photo = models.ImageField("Прикреплённые к новости фотографии",
                                  blank=True,
                                  null=True,
                                  upload_to='/photo',  # Где будет храниться на сервере изображнение
                                  height_field=100,
                                  width_field=100
                                  )

        banner = models.ImageField("Баннер новости",
                                   blank=True,
                                   null=True,
                                   upload_to='/banner',  # Где будет храниться на сервере изображнение
                                   height_field=100,
                                   width_field=100
                                   )
    """

    class Meta:
        ordering = ["film_id"]


    def __str__(self):
        return "{0}".format(self.name)


class mk_event(models.Model):
    """
    Модель описывает мероприятие
    """
    #Переменные для полей с выбором
    f_var = "Да"
    s_var = "Нет"
    in_premiere_vars = [
        (f_var, "Отобразить в блоке"),
        (s_var, "Не отображать в блоке"),
    ]

    #Поля

    event_id = models.AutoField(
        "Идентификатор фильма",
        primary_key = True
    )

    name = models.CharField("Название мероприятия",
                            max_length = 10,
                            help_text = "Название мероприятия"
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
        ordering = ["event_id"]

    #Методы

    def __str__(self):
        return "{0}, {1}".format(self.name, self.short_description)


class News(models.Model):
    """
    Модель создания новости
    """
    #Поля
    # Админ
    ID = models.AutoField("ID",
                          primary_key = True,
                          editable = False
                          )



    date_create = models.DateField("Дата создания",
                                   editable = False,
                                   auto_now = True
                                   )

    creater_name = models.CharField("Имя разместившего",
                                    max_length = 100
                                    )

    date_change = models.DateField("Дата последнего изменения",
                                   editable = True,
                                   auto_now_add = True
                                   )

    changer_name = models.CharField("Имя последнего редактора",
                                    max_length = 100
                                    )

    date_close = models.DateField("Дата закрытия премьеры",
                                   editable = True,
                                   null = True,
                                   blank = True
                                   )

    #Инфо
    title = models.CharField("Заголовок новости",
                             max_length = 100,
                             help_text = "Введите заголовок новости"
                             )

    lead = models.CharField("Лид новости",
                            max_length = 100,
                            help_text="Введите лид новости"
                            )

    description = models.TextField("Новость",
                                   help_text = "Введите текст новости",
                                   null = True,
                                   blank = True,
                                   max_length = 600
                                   )
    """ Временно отключено
    photo = models.ImageField("Прикреплённые к новости фотографии",
                              blank = True,
                              null = True,
                              upload_to='/photo', #Где будет храниться на сервере изображнение
                              height_field = 100,
                              width_field = 100
                              )

    banner = models.ImageField("Баннер новости",
                               blank = True,
                               null = True,
                               upload_to='/banner', #Где будет храниться на сервере изображнение
                               height_field=100,
                               width_field=100
                               )
    """
    source = models.CharField("Источник",
                              blank = True,
                              null = True,
                              max_length = 300
                               )
    #Полезн
    news_type = models.CharField("Тип новости",
                                 blank = True,
                                 null = True,
                                 max_length = 100
                                 )


class mk_info(models.Model):
    """
    Модель для создания страницы 'О нас'
    """
    #Инорм.часть
    description = models.TextField("О нас",
                                   null = True,
                                   blank = True,
                                   max_length = 3000
                                   )

    manual = models.TextField("Руководство",
                              help_text = "Введите имена руководителей через запятую с пробелом",
                              null = True,
                              blank = True,
                              max_length = 600
                              )

    about_union = models.TextField("О профсоюзе",
                                   help_text = "Введите информацию профсоюз",
                                   null = True,
                                   blank = True,
                                   max_length = 3000
                                   )

    documentation = models.CharField("Ссылки на документацию",
                                     max_length = 500,
                                     help_text = "Введите ссылки на документы через запятую с пробелами",
                                     null = True,
                                     blank = True
                                     )

    #Адм.часть
    last_change_date = models.DateTimeField("Дата и время последнего изменения данных",
                                            auto_now = True
                                            )

    changer_name = models.CharField("Имя последнего редактора",
                                    max_length = 100
                                    )

