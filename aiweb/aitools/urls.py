from django.urls import path

from . import views

app_name = 'aitools'

urlpatterns = [
    path("", views.index, name="index"),
    path("docscanner", views.view_document, name="documentscanner")
]