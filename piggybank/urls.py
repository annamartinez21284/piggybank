from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("customer_info", views.customer_info, name="customer_info"),
    path("create_goal", views.create_goal, name="create_goal"),
    path("customer_info/<customer_id>", views.customer_info, name="customer_info_id"),
    path("delete/<savingsGoalUid>", views.delete, name="delete")
]
