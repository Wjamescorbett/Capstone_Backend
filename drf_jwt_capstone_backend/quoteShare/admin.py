from django.contrib import admin
from .models import Car
from .models import PostedQuote
from .models import PostedComment
from .models import UserFavorite
# Register your models here.

admin.site.register(Car)
admin.site.register(PostedQuote)
admin.site.register(PostedComment)
admin.site.register(UserFavorite)