from rest_framework import serializers

from ....model.certificate_entity import Certificate


class InsertCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['title', 'description', 'earned_date', 'link']


class CertificateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('image',)


class GetCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['title', 'description', 'earned_date', 'link', 'image']
