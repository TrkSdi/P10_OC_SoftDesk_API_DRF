from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from auth.models import User



class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id',
                  'first_name',
                  'last_name',
                  'username',
                  'email',]
        

class RegisterSerializer(ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'})
    
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'username',
                  'password',
                  'password2']
        
    def save(self):
        user = User(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username']
        )   
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        user.set_password(password)
        user.save()
        
        return user
    
    


