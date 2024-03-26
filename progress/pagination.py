from rest_framework import pagination


class DefaultPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    limit_query_param = "limit"
    offset_query_param = "offset"
