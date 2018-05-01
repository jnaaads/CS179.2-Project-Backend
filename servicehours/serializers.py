from rest_framework import serializers
from .models import Student, Task, Office

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'

	class StudentSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		id_number = serializers.IntegerField(max_digits=6)
		first_name = serializers.CharField(max_length=100)
		last_name = serializers.CharField(max_length=100)
		year = serializers.IntegerField(max_digits=1)
		course = serializers.CharField(max_length=20)
		service_hours_todo = serializers.DecimalField(max_digits=5, decimal_places=2)
		service_hours_done = serializers.DecimalField(max_digits=5, decimal_places=2)

		def cretae(self, validated_data):
			return Student.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.id_number = validated_data.get('id_number', instance.id_number)
			instance.first_name = validated_data.get('name', instance.name)
			instance.last_name = validated_data.get('last_name', instance.last_name)
			instance.year = validated_data.get('year', instance.year)
			instance.course = validated_data.get('course', instance.course)
			instance.service_hours_todo = validated_data.get('service_hours_todo', instance.service_hours_todo)
			instance.service_hours_done = validated_data.get('service_hours_done', instance.service_hours_done)
			instance.save()
			return instance

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'

	class TaskSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		name = serializers.CharField(max_length=200)
		description = serializers.CharField(max_length=400)
		duration_in_hours = serializers.DecimalField(max_digits=5, decimal_places=2)
		isDone = serializers.BooleanField()

		def create(self, validated_data):
			return Task.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.name = validated_data.get('name', instance.name)
			instance.description = validated_data.get('description', instance.description)
			instance.duration_in_hours = validated_data.get('duration_in_hours', instance.duration_in_hours)
			instance.isDone = validated_data.get('isDone', instance.isDone)
			instance.save()
			return instance

class OfficeSerializer(serializers.ModelSerializer):
	tasks = TaskSerializer(many=True)

	class Meta:
		model = Office
		fields = '__all__'

	class OfficeSerializer(serializers.Serializer):
		id = serializers.IntegerField(read_only=True)
		name = serializers.CharField(max_length=200)
		location = serializers.CharField(max_length=200)

		def create(self, validated_data):
			tasks_data = validated_data.pop('tasks')
			office = Office.objects.create(**validated_data)
			for task_data in tasks_data:
				Task.object.create(office=office, **task_data)
			return office

		def update(self, instance, validated_data):
			instance.name = validated_data.get('name', instance.name)
			instance.location = validated_data.get('location', instance.location)
			tasks_data = validated_data.pop('tasks')
			instance.tasks_data = tasks_data.id
			instance.save()
			return instanc