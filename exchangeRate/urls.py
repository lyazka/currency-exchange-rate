from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.balance, name='currency'),
    url(r'^converter/', TemplateView.as_view(template_name="../templates/exchangeRate/converter.html"), name="converter"),
    url(r'^er_balance/', views.balance, name="balance"),
    url(r'^exchange/', views.exchange_rate, name="exchange"),
]