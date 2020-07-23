from rest_framework import serializers

from .models import Music


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = ('name', 'audio')

    def create(self, validated_data):
        return Music.objects.create(**validated_data)
