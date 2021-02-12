from .models import Info
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
@api_view(['GET', 'POST'])
def job_list_api(request):
    if request.method == 'GET':
        all_jobs_ = Info.objects.all()
        data = JobSerializer(all_jobs_, many=True).data
        return Response({'data': data})
    else:
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
