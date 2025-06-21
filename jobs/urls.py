from django.urls import path
from jobs.views import job_views

# router = routers.DefaultRouter()

# router.register('jobs', views.JobsView)

urlpatterns = [
    path("", job_views.jobs, name='jobs'),
    path("<uuid:company_id>/companys",
         job_views.get_other_jobs_same_company, name='get_jobs_company'),
    path("<uuid:job_id>/", job_views.get_job, name='get_jobs'),
    path("<str:job_id>/update", job_views.update_job, name='update_job'),
    path("<str:job_id>/delete", job_views.delete_job, name='delete_job'),

]
