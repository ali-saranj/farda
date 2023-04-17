from rest_framework import serializers
from .models import Restaurant
from .models import Usera
from .models import Result
from .models import Comment
from .models import Food


class RestaurantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class UseraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usera
        fields = "__all__"


class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"