from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Dataset, Row
from .serializers import DatasetSerializer, RowSerializer

import csv

class DatasetListView(APIView):
	"""Vista de la lista de todos los datasets
	presentes en la DB."""
	def get(self, request, format=None):
		datasets = Dataset.objects.all()
		serializer = DatasetSerializer(datasets, many=True)
		return Response(serializer.data)

	def post(self, request):
		csv = request.FILES
		dataset = request.data
		dataset.save()
		serializer = DatasetSerializer(dataset)
		with open(csv, newline='') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				try:
					Row.objects.create(
						dataset_id=dataset,
						point=row[0],
						client_id=int(row[1]),
						client_name=row[2]
					)
				except:
					return Response(status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RowListView(generics.ListAPIView):
	"""Vista de la lista de todos los rows
	presentes en la DB"""
	serializer_class = RowSerializer

	def get_queryset(self):
		"""
		Filtra el contenido de la respuesta por query params,
		si existen. Así mismo, genera error si el param dataset_id 
		no está presente. 
		"""
		queryset = Row.objects.all()
		dataset_id = self.request.query_params.get('dataset_id')
		name = self.request.query_params.get('name', None)
		if not dataset_id:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		dataset = Dataset.objects.get(id=dataset_id)
		queryset.filter(dataset_id=dataset)
		if name is not None:
			queryset.filter(dataset__name=name)
		return queryset
