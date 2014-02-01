from blob.models import Blob, SomeAdditionalInfo
from rest_framework import serializers

class SomeAdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model= SomeAdditionalInfo
        fields=('sometext',)

class BlobSerializer(serializers.ModelSerializer):
    other = SomeAdditionalInfoSerializer(many=True)

    class Meta:
        model = Blob
        fields = ('id', 'datext', 'someotherfield', 'other')
