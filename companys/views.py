from companys.models import Company
from companys.serializer import CompanySerializer
from rest_framework import status, serializers
from utils.api_response import success_response, error_response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from utils.response_serializer import BaseResponseSerializer, PaginationSerializer


class CompanyResponseSerializer(BaseResponseSerializer):
    data = CompanySerializer(many=True)
    pagination = PaginationSerializer()


class CompanySingleResponseSerializer(BaseResponseSerializer):
    data = CompanySerializer()


@extend_schema(
    tags=['Company'],
    methods=['POST'],
    request=CompanySerializer,
    responses={201: CompanySingleResponseSerializer}
)
@extend_schema(
    tags=['Company'],
    methods=['GET'],
    description=(
        "Retrieve a paginated list of all registered companies. "
        "Each response page contains up to 10 companies by default. "
        "You can control pagination using the `page` and `per_page` query parameters. "
        "The response includes metadata such as total items, total pages, and navigation flags."
    ),
    responses=OpenApiResponse(response=CompanyResponseSerializer),
    parameters=[
        OpenApiParameter(name='page', required=False, type=int,
                         location=OpenApiParameter.QUERY),
        OpenApiParameter(name='per_page', required=False,
                         type=int, location=OpenApiParameter.QUERY),
    ]
)
@api_view(['GET', 'POST'])
def companys(request):
    if request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response(data=serializer.data, message="Company berhasil dibuat", status_code=status.HTTP_201_CREATED)
        return error_response(errors=serializer.errors, message="Validasi gagal", status_code=status.HTTP_400_BAD_REQUEST)
    else:
        data = Company.objects.all()
        page_number = int(request.GET.get('page', 1))
        items_per_page = int(request.GET.get('per_page', 10))
        paginator = Paginator(data, items_per_page)
        try:
            paginated_companys = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_companys = paginator.page(1)
        except EmptyPage:
            return error_response(
                message="Halaman tidak ditemukan",
                errors={"page": "Page number melebihi jumlah total halaman"},
                status_code=404
            )

        serializer = CompanySerializer(paginated_companys, many=True)
        return success_response(
            data=serializer.data,
            is_have_pagination=True,
            paginated_page=paginated_companys,
            paginator=paginator
        )

# Detail Endpoint


@extend_schema(
    tags=['Company'],
    description="Retrieve detailed information of a single company based on the provided `company_id`. This endpoint returns detailed fields such as company name, email, website, location, logo, employee count, and benefit information. If the specified `company_id` does not exist, a 404 error response will be returned along with an appropriate error message.",
    responses=OpenApiResponse(response=CompanySingleResponseSerializer)
)
@api_view(['GET'])
def get_company(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
        serializer = CompanySerializer(company)
        return success_response(data=serializer.data)
    except Company.DoesNotExist:
        return error_response(
            message="Data tidak ditemukan",
            errors={"company_id": "Company dengan ID tersebut tidak ada"},
            status_code=status.HTTP_404_NOT_FOUND
        )
