from django.urls import path
from .views import getPanelData
# from .views import ItemListCreate, ItemRetrieveUpdateDelete

urlpatterns = [
    path('getPanel/', getPanelData.as_view(), name='get-panel-data'),
]