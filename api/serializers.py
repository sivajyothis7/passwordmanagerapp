from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Entry


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=[
            "username",
            "email",
            "password",
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class EntrySerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)


    class Meta:
        model=Entry
        fields=[
            "user",
            "site_name",
            "site_url",
            "site_password",
            "notes"
        ]

    def create(self, validated_data):
        user=self.context.get("user")
        return Entry.objects.create(user=user,**validated_data)