from django.contrib import admin
from .models import mk_film, mk_event, News, mk_info

admin.site.register(mk_film)
admin.site.register(mk_event)
admin.site.register(News)
admin.site.register(mk_info)
