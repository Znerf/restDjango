from rest_framework import serializers
from . models import user

class userSerializer2(serializers.ModelSerializer):
    firstname=serializers.CharField(max_length=10)
    lastname=serializers.CharField(max_length=10)
    userid=serializers.IntegerField()

    
    class Meta:
        model=user
        fields=['firstname','lastname','userid']
        # fields='__all__'

    def create(self,validated_data):
        return user.objects.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.firstname=validated_data.get('firstname',instance.firstname)
        instance.lastname=validated_data.get('firstname',instance.lastname)
        instance.userid=validated_data.get('firstname',instance.userid)
        instance.save()
        return instance

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        # field=['id','firstname','lastname','userid']
        fields='__all__'