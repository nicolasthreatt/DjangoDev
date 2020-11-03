""" REST API""" 

from rest_framework import serializers
from .models import Player
import datetime

class PlayerSerializers(serializers.ModelSerializer):

    # Read Only Value
    # read_only_variable = serializers.IntegerField(read_only=True)

    # Different Style for date field
    # date = serializers.DateTimeField(input_formats=['%m-%d-%Y %H:%M:%S'], 
    #                                  format=None,
    #                                  allow_null=False,
    #                                  style={'input_type': 'text'})

    # Add a photo
    # photo = serializers.ImageField(default=None)

    # Add a file (could be useful to wrtie a summary after every game)
    # stats_file = serializers.FileField(write_only=True, default=None)
    # def update(self, instance, validated_data):
    #     if validated_data.get('stats_file', None):
    #         instance.summary += '\n\nWarranty Information:\n'
    #         instance.summary += b'; '.join(
    #             validated_data['stats_file'].readlines()
    #         ).decode()
    #     return(instance)

    class Meta:
        model = Player
        fields = ('name', 'team', 'jersey_num', 'ppg', 'fg_p', 'tp_p', 'reb', 'ast', 'date') # , read_only_varaiabe, photo)


class PlayerStatsSerializer(serializers.Serializer):

    stats = serializers.DictField(
        child=serializers.ListField(
            child=serializers.IntegerField(),
        )
    )
