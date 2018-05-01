from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Task, Office
from .serializers import StudentSerializer, TaskSerializer, OfficeSerializer
from django.http import Http404

# Create your views here.

class StudentList(APIView):
	def get(self, request):
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
	def get_object(self, pk):
		try:
			return Student.objects.get(pk=pk)
		except Student.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		student = self.get_object(pk)
		serializer = StudentSerializer(user)
		return Response(serializer.data)

	def patch(self, request, pk):
		student = self.get_object(pk)
		serializer = StudentSerializer(student, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		student = self.get_object(pk)
		student.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class TaskList(APIView):
	def get(self, request):
		tasks = Task.objects.all()
		serializer = TaskSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = TaskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
	def get_object(self, pk):
		try:
			return Task.objects.get(pk=pk)
		except Task.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		task = self.get_object(pk)
		serializer = TasksSerializer(product)
		return Response(serializer.data)

	def patch(self, request, pk):
		task = self.get_object(pk)
		serializer = TaskSerializer(product, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		task = self.get_object(pk)
		task.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class OfficeList(APIView):
	def get(self, request):
		offices = Office.objects.all()
		serializer = OfficeSerializer(carts, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = OfficeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OfficeDetail(APIView):
	def get_object(self, pk):
		try:
			return Office.objects.get(pk=pk)
		except Office.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		office = self.get_object(pk)
		serializer = OfficeSerializer(cart)
		return Response(serializer.data)

	def patch(self, request, pk):
		office = self.get_object(pk)
		serializer = OfficeSerializer(cart, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		office = self.get_object(pk)
		office.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)