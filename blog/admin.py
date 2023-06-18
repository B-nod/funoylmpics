from django.contrib import admin

from blog.models import Category
from .models import *

# Register your models here.
admin.site.register(Category)
# admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Country)
admin.site.register(ScoreBoard)





