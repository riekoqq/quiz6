from base.models import Drug
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DrugSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/drugs',
        '/api/drugs/create',
        '/api/drugs/update/<id>',
        '/api/drugs/delete/<id>',
        '/api/drugs/<id>/reviews',
        '/api/drugs/top/',
        '/api/drugs/<id>/',
        '/api/drugs/<id>/reviews',
    ]

    return Response(routes)

@api_view(['GET'])
def getDrugs(request):
    drugs = Drug.objects.all()
    serializer = DrugSerializer(drugs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDrug(request, pk):
    try:
        drug = Drug.objects.get(_id=pk)
        serializer = DrugSerializer(drug)
        return Response(serializer.data)
    except Drug.DoesNotExist:
        return Response({'detail': 'Drug not found'})