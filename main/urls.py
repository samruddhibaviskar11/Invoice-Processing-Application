from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("login", Login.as_view(), name="login"),
    path("extract", Extract.as_view(), name="extract"),
    #path("download", Download.as_view(), name="download"),
    path("upload", Upload.as_view(), name="upload"),
    path("logout", Logout.as_view(), name="logout"),
]
