from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('problem/', views.problem, name='problem'),
    path('solution/', views.solution, name='solution'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('beta/', views.beta, name='beta'),
    path('posts/', views.posts, name='posts'),
    path('api/beta-signup/', views.beta_signup, name='beta_signup'),
]

