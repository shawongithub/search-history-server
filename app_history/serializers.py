from rest_framework import serializers
from . models import SearchHistory



class SearchHistorySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
            read_only=True,
            slug_field='username'
    )
    class Meta:
        model = SearchHistory
        fields = '__all__'
