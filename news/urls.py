from django.urls import path
from news.views import HomeView,ArticleView,CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:id>/', ArticleView.as_view(), name='article'),
    path('category/<int:id>/', CategoryView.as_view(), name='category'),
]