from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(DailyGoal)