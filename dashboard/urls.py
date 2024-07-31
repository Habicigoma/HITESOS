from django.urls import path
from . import views


urlpatterns=[
    path('', views.dashboard, name='dashboard'),
    path('hightech_service/', views.hightech_service, name='hightech_service'),
    path('latest_info/', views.latest_info, name='latest_info'),
    path('market_service/', views.market_service, name='market_service'),
    path('security_camera/', views.security_camera, name='security_camera'),
    path('software_application_development/', views.software_application_development, name='software_application_development'),
    path('website_development/', views.website_development, name='website_development'),
    path('supply_hightech_equipment/', views.supply_hightech_equipment, name='supply_hightech_equipment'),
    path('contact_us/', views.contact_us, name='contact_us')
]