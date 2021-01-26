from django.urls import path
from . import views

app_name = 'datasets'

urlpatterns = [
	path('v1/datasets', views.DatasetListView.as_view(), name='dataset_list'),
	path('v1/rows', views.RowListView.as_view(), name='row_list'),
]