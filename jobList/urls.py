from django.contrib import admin
from django.urls import path, include
from job import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.JobListView.as_view()),
    path('<int:pk>/', views.JobDetailView.as_view()),
    path('new/', views.JobCreateView.as_view()),
    path('<int:pk>/update/', views.JobUpdateView.as_view()),
    path('<int:pk>/delete/', views.JobDeleteView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(next_page="/")),
    path('register/', views.RegisterView.as_view()),
    
]
