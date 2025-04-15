from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('vote/', views.vote_view, name='vote'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='vote/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('results/', views.live_results, name='live_results'),  
    path('blockchain/', views.blockchain_viewer, name='blockchain_viewer'),
    path('api/live-data/', views.api_live_data, name='api_live_data'),
    path('vote/receipt/<int:candidate_id>/', views.vote_receipt, name='vote_receipt'),
    path('vote/receipt/pdf/<int:candidate_id>/', views.generate_pdf_receipt, name='generate_pdf_receipt'),
    
    path('my-receipts/', views.my_receipts, name='my_receipts'),




]
