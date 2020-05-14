from django.contrib import admin
from .models import mk_film, mk_event, News
# Register your models here.

class EventsAdmin(admin.ModelAdmin): #специальный класс для спецпроектов
    list_display = ('title',
                    'date_of_release',
                    'in_premiere')

admin.site.register(mk_event, EventsAdmin)

@admin.register(mk_film)
class FilmAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass



admin.site.register(mk_event)
#admin.site.register(News)
