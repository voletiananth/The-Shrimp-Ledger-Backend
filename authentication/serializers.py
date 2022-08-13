
from rest_framework.serializers import ModelSerializer

from authentication.models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['phone_number'],
                                            password=validated_data['password'],
                                            first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name'])
            return user

    # User serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
