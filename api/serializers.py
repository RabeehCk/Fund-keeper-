from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Expense,Income


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["id","username","email","password"]

        read_only_fields = ["id"]

    def create(self,validated_data):

        return User.objects.create_user(**validated_data)
    

class ExpenseSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Expense

        fields = "__all__"

        read_only_fields = ["id","owner","created_date","updated_date","is_active"]


class IncomeSerializer(serializers.ModelSerializer):

    owner = serializers.StringRelatedField(read_only=True)

    class Meta:

        model = Income

        fields = "__all__"

        read_only_fields = ["id","owner","created_date","updated_date"]