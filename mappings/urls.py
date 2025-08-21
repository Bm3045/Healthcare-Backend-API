from django.urls import path
from .views import MappingListCreateView, MappingRetrieveView, MappingDeleteView

urlpatterns = [
    path("", MappingListCreateView.as_view(), name="mappings-list-create"),
    path("<int:patient_id>/", MappingRetrieveView.as_view(), name="mappings-by-patient"),
    path("delete/<int:pk>/", MappingDeleteView.as_view(), name="mapping-delete"),
]
