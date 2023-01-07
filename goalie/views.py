from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from goal.serializers import StudentsSerializer
from goal.models import Students

class TesView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Williams',
            'no_of_years': 12
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializers = StudentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
