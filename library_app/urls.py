from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('books/', views.books_collection, name='library-books'),
    path('books/<int:id>', views.show, name='library-show'),
]

handler404 = 'library_app.views.not_found_404'
handler500 = 'library_app.views.server_error_500'
