from django.urls import path
from .views import (
    ProjectListView, SkillListView, ContactCreateView,
    HeroProfileView, AboutSectionView, BlogPostListView
)
from .views import ProjectDetailView

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('skills/', SkillListView.as_view()),
    path('contact/', ContactCreateView.as_view()),
    path('hero/', HeroProfileView.as_view()),
    path('about/', AboutSectionView.as_view()),
    path('blog/', BlogPostListView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
]