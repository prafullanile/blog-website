from django.urls import path
from. import views

urlpatterns = [
        path('<int:category_id>/',views.posts_by_category, name='posts_by_category'),

    ]

# urlpatterns = [
#     # path('', views.category_list, name='category_list'),
#     path('<int:category_id>/', views.posts_by_category, name='posts_by_category'),
# ]
