from django.urls import path
from stage2 import views
urlpatterns = [
    path('',views.Person_list),
    path('<int:id>',views.Person_detail)
]
