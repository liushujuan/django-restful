from rest_framework import serializers
from update_api.models import *

class AutherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name','email','qq','addr')
    def create(self, validated_data):
        return serializers.ModelSerializer.create(self, validated_data)
    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)
    
    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('author','title','context','created_time','last_modified_time','status','views','likes','category')
    def create(self, validated_data):
        return serializers.ModelSerializer.create(self, validated_data)
    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)
    
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','created_time','created_time')
    def create(self, validated_data):
        return serializers.ModelSerializer.create(self, validated_data)
    def update(self, instance, validated_data):
        return serializers.ModelSerializer.update(self, instance, validated_data)