from rest_framework import serializers
from .models import *

# Serializados de Documentos
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class DocumentActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("status","last_updated",)

# Serializados de Procesos
class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class ProcessActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ("status","last_updated",)

class ProcessCalculateSerializer(serializers.Serializer):
    id_phase = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    total_task = serializers.CharField(max_length=10)
    completed_task = serializers.CharField(max_length=10)
    percentage = serializers.CharField(max_length=10)

class ProcessAllSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    id_user = serializers.CharField(max_length=10)
    name_user = serializers.CharField(max_length=50)
    user_list = serializers.CharField(max_length=10)
    documents_list = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=100)
    status_process = serializers.CharField(max_length=10)
    status = serializers.CharField(max_length=1)
    created = serializers.CharField(max_length=10)
    last_updated = serializers.CharField(max_length=10)

# Serializados de Fases
class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = '__all__'

class PhaseActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = ("status","last_updated",)

# Serializador de Criterios
class CriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'

class CriteriaActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criteria
        fields = ("status","last_updated",)

# Serializador Indicador 
class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'

class IndicatorActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = ("status","last_updated",)

# Serializados de Tareas
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("status","last_updated",)
class TaskAllSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
    id_indicator = serializers.CharField(max_length=10)
    name_indicator = serializers.CharField(max_length=50)
    id_criteria = serializers.CharField(max_length=10)
    name_criteria = serializers.CharField(max_length=50)
    id_phase = serializers.CharField(max_length=10)
    name_phase = serializers.CharField(max_length=50)
    description =serializers.CharField(max_length=500)
    user_list = serializers.CharField(max_length=100)
    start_date = serializers.CharField(max_length=25)
    end_date = serializers.CharField(max_length=25)
    user_list = serializers.CharField(max_length=100)
    close_date = serializers.CharField(max_length=25)
    documents_list = serializers.CharField(max_length=100)
    status_task = serializers.CharField(max_length=10)
    status =serializers.CharField(max_length=1)
    created = serializers.CharField(max_length=50)
    last_updated = serializers.CharField(max_length=50)

# Serializados de Criterios
class CriteriaDataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    percentage = serializers.CharField(max_length=10)

# Serializados de Combo Box
class SSelectSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=50)
# documents
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"