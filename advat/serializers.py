from advat.models import Post
from rest_framework import serializers


class AdvatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('sale_title', 'sale_description','category', 'start_date','end_date','location', 'address','banner')
