from django.urls import path, include
import banners.views as views
# router = routers.DefaultRouter()

# router.register('jobs', views.JobsView)

urlpatterns = [
    path("banners", views.banners, name='banners'),
]
