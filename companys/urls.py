from django.urls import path, include
import companys.views as views
# router = routers.DefaultRouter()

# router.register('jobs', views.JobsView)

urlpatterns = [
    path("companys", views.companys, name='companys'),
]
