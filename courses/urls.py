from django.urls import path 
from . import views

urlpatterns=[

    path('',views.course_list),
    path('<int:course_id>',views.course_details)
]
