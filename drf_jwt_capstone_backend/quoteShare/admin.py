from django.contrib import admin
from .models import Car
from .models import PostedQuote
from .models import PostedComment
from .models import UserFavorite
from .models import ApiComment
# Register your models here.

admin.site.register(Car)
admin.site.register(PostedQuote)
admin.site.register(PostedComment)
admin.site.register(UserFavorite)
admin.site.register(ApiComment)