
# from django.urls import path, include
# from . import views
# from rest_framework import routers
# from rest_framework.urlpatterns import format_suffix_patterns

# # router = routers.DefaultRouter()
# # router.register('store', views.StoreView)

# urlpatterns = [
#     path('', views.StoreView.as_view()),
#    #  path(r'(?P<drink_name>\D+)/', views.StoreView.as_view())
# ]


# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.StoreView.as_view()),
]
