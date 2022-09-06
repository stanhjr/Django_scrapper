from rest_framework import serializers
from home.models import OlxModel


class OlxSerializer(serializers.ModelSerializer):

    class Meta:
        model = OlxModel
        fields = '__all__'
