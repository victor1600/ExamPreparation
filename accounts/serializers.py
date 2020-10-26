from rest_framework import serializers
from accounts.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    # this field is not part of the model
    # The style that we apply will hide the field
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']

        extra_kwargs = {
            # For security, we hide the password
            'password': {'write_only': True}
        }

        # Override the method, so we get sure both password match
    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        # We have to call this method when overriding to actually save
        account.save()
        return account
