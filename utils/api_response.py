from rest_framework.response import Response
from rest_framework import status


def success_response(
    data=None,
    message="Berhasil mendapatkan data",
    status_code=status.HTTP_200_OK,
    is_have_pagination=False,
    paginator=None,
    paginated_page=None
):
    response_data = {
        "message": message,
        "errors": None,
        "data": data if data is not None else [],
    }

    if is_have_pagination and paginator and paginated_page:
        response_data["pagination"] = {
            "total_items": paginator.count,
            "total_pages": paginator.num_pages,
            "item_per_page": paginator.per_page,
            "current_page": paginated_page.number,
            "has_next": paginated_page.has_next(),
            "has_previous": paginated_page.has_previous(),
        }

    return Response(response_data, status=status_code)


def error_response(
    errors=None,
    message="Terjadi kesalahan",
    status_code=status.HTTP_400_BAD_REQUEST
):
    return Response({
        "message": message,
        "errors": errors,
        "data": []
    }, status=status_code)
