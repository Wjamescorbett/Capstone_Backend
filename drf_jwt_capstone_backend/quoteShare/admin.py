from django.contrib import admin
from .models import Car
from .models import PostedQuote
# Register your models here.

admin.site.register(Car)
admin.site.register(PostedQuote)