from rest_framework.views import APIView
from rest_framework.response import Response

from .items_matrix import *
from .opti import *

class getPanelData(APIView):
    def get(self, request):  
        data = {
        'items': itemsList
        }
        return Response(data, 200)
    
    def post(self, request):
        itemList=request.data["data"]
        itemListIndexed=[Items[item].value for item in itemList]
        
        optimalSequence = optimiseSKUs(itemListIndexed)
        return Response({"optimalSequence": optimalSequence}, 200)
