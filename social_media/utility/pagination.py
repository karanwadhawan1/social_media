from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        response = {}
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        response['result'] = data
        return response