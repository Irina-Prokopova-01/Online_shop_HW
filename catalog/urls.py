from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail


app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", product_detail, name='product'),
]
