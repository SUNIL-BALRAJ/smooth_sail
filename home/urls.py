from django.urls import path
from admin_datta import views
from django.contrib.auth import views as auth_views

from .views import tables
from . import views





urlpatterns = [
  #path('generate_pdf_report/<int:uploaded_image_id>/', views.generate_pdf_report, name='generate_pdf_report'),
  path('youtube/', views.youtube, name='youtube'),
  path('telegram/', views.telegram, name='telegram'),  
  path('profile/', views.profile, name='profile'),
  path('misleading_telegram/', views.misleading_telegram, name='misleading_telegram'),
  path(''       , views.index, name='index'),
  path('tables/', tables     , name='tables'),

  # Components
  path('components/button/', views.bc_button, name='bc_button'),
  path('components/badges/', views.bc_badges, name='bc_badges'),
  path('components/breadcrumb-pagination/', views.bc_breadcrumb_pagination, name='bc_breadcrumb_pagination'),
  path('components/collapse/', views.bc_collapse, name='bc_collapse'),
  path('components/tabs/', views.bc_tabs, name='bc_tabs'),
  path('components/typography/', views.bc_typography, name='bc_typography'),
  path('components/feather-icon/', views.icon_feather, name='icon_feather'),

  # Forms and Tables
  path('forms/form-elements/', views.form_elements, name='form_elements'),
  path('tables/basic-tables/', views.basic_tables, name='basic_tables'),

  # Chart and Maps
  path('charts/morris-chart/', views.morris_chart, name='morris_chart'),
  path('maps/google-maps/', views.google_maps, name='google_maps'),

  # Authentication
  path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
  path('accounts/login/', views.UserLoginView.as_view(), name='login'),
  path('accounts/logout/', views.logout_view, name='logout'),

  path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
  path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
      template_name='accounts/auth-password-change-done.html'
  ), name="password_change_done"),

  path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
  path('accounts/password-reset-confirm/<uidb64>/<token>/',
    views.UserPasswrodResetConfirmView.as_view(), name="password_reset_confirm"
  ),
  path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
    template_name='accounts/auth-password-reset-done.html'
  ), name='password_reset_done'),
  path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name='accounts/auth-password-reset-complete.html'
  ), name='password_reset_complete'),

  #
  path('profile/', views.profile, name='profile'),
  #path('sample-page/', views.sample_page, name='sample_page'),
  path('horizontal/', views.horizontal, name='horizontal'),
  path('segement_page1/', views.sample_page1, name='segment_page1'),
  path('segment_page2/', views.sample_page2, name='segment_page2'),

  path('failure/', views.failure, name='failure'),

]
