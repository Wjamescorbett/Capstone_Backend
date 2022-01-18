from django.urls import path
from quoteShare import views

urlpatterns = [
    path('', views.CarList.as_view()),
    path('all/', views.get_all_cars),
    path('post/', views.user_cars),
    path('postedQuote/', views.postedQuotes),
    path('postedComment/', views.postedComment),
    path('allQuotes/', views.get_all_postedQuotes),
    path('allComments/', views.get_all_postedComments),
    path('apiComment/', views.apiComment),
    path('allApiComments/', views.get_all_apiComments),
    path('deleteQuote/<int:pk>/', views.deleteQuote),
    path('deleteComment/<int:pk>/', views.deleteComment),
    # path('allComments/<str:id>/', views.get_all_postedComments)
]
