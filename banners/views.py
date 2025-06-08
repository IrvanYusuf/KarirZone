from banners.models import Banner
from rest_framework import status
from banners.serializer import BannerSerializer
from utils.api_response import success_response, error_response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiResponse
from utils.response_serializer import BaseResponseSerializer, PaginationSerializer
# Create your views here.


@extend_schema(
    tags=['Banners']
)
@api_view(['GET'])
def banners(request):
    banners = Banner.objects.all()[:3]
    banners_serializer = BannerSerializer(banners, many=True)
    return success_response(data=banners_serializer.data)
