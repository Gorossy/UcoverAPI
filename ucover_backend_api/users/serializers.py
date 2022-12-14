from rest_framework import serializers
from users.models.users import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id','Email_verified_at','Payment_method','created_at','updated_at','is_active','is_staff')