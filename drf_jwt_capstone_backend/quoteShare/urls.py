from django.urls import path
from quoteShare import views

urlpatterns = [
    path('', views.CarList.as_view()),
    path('all/', views.get_all_cars),
    path('post/', views.user_cars)
]
