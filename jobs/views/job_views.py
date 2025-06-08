from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework import status
from utils.api_response import success_response, error_response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from drf_spectacular.utils import extend_schema
# Create your views here.


def create_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return success_response(data=serializer.data, message="Job berhasil dibuat", status_code=status.HTTP_201_CREATED)
    return error_response(errors=serializer.errors, message="Validasi gagal", status_code=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Jobs']
)
@api_view(['GET', 'POST'])
def jobs(request):
    if request.method == 'POST':
        return create_job(request)
    else:
        jobs = Job.objects.all()
        # pagination
        page_number = int(request.GET.get('page', 1))
        items_per_page = int(request.GET.get('per_page', 10))
        paginator = Paginator(jobs, items_per_page)
        try:
            paginated_jobs = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_jobs = paginator.page(1)
        except EmptyPage:
            paginated_jobs = paginator.page(paginator.num_pages)

        serializer = JobSerializer(paginated_jobs, many=True)

        return success_response(
            data=serializer.data,
            is_have_pagination=True,
            paginated_page=paginated_jobs,
            paginator=paginator
        )


@extend_schema(
    tags=['Jobs']
)
@api_view(['GET'])
def get_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        serializer = JobSerializer(job)
        return success_response(data=serializer.data)
    except Job.DoesNotExist:
        return error_response(
            message="Data tidak ditemukan",
            errors={"job_id": "Job dengan ID tersebut tidak ada"},
            status_code=status.HTTP_404_NOT_FOUND
        )


@extend_schema(
    tags=['Jobs']
)
@api_view(['PUT', 'PATCH'])
def update_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return error_response(
            message="Data tidak ditemukan",
            errors={"job_id": "Job dengan ID tersebut tidak ada"},
            status_code=status.HTTP_404_NOT_FOUND
        )

    partial = (request.method == 'PATCH')
    serializer = JobSerializer(job, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return success_response(data=serializer.data, message="Job berhasil diupdate")
    return error_response(errors=serializer.errors, message="Validasi gagal", status_code=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Jobs']
)
@api_view(['DELETE'])
def delete_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        job.delete()
        return success_response(data=None, message="Berhasil hapus data")
    except Job.DoesNotExist:
        return error_response(
            message="Data tidak ditemukan",
            errors={"job_id": "Job dengan ID tersebut tidak ada"},
            status_code=status.HTTP_404_NOT_FOUND
        )
