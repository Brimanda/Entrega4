from rest_framework import serializers
from .models import Flor, Categoria

class FlorSerializer(serializers.ModelSerializer):

    class Meta: 

        model = Flor
        fields = '__all__'
        