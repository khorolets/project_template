from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class DemoView(APIView):
    def get(self, *args, **kwargs):
        data = [
            {
                'id': 1,
                'title': 'test1',
            },
            {
                'id': 2,
                'title': 'test2',
            },
        ]
        return Response(data)
