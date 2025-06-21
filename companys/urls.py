from django.urls import path, include
import companys.views as views
# router = routers.DefaultRouter()

# router.register('jobs', views.JobsView)

urlpatterns = [
    path("", views.companys, name='companys'),
    path("<str:company_id>", views.get_company, name='get_company'),
]
