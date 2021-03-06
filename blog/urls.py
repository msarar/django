
from django.urls import path
from .views import  (ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDleteView)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/delete/', ArticleDleteView.as_view(), name='article-delete'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update')
]
