from rest_framework import serializers

from green_medic.apps.medicines.models import Medicine


class MedicineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'id',
            'manufacturer',
            'brand_name',
            'generic_name',
            'strength',
            'dosages',
            'price',
            'use_for',
            'dar',
        ]


class MedicineRetrieveSerializer(serializers.ModelSerializer):
    similar_medicines = serializers.SerializerMethodField()

    def get_similar_medicines(self, medicine):
        similar_medicines = Medicine.objects.filter(generic_name=medicine.generic_name)
        serializer = MedicineListSerializer(instance=similar_medicines, many=True)
        return serializer.data

    class Meta:
        model = Medicine
        fields = [
            'id',
            'manufacturer',
            'brand_name',
            'generic_name',
            'strength',
            'dosages',
            'price',
            'use_for',
            'dar',
            'similar_medicines',
        ]


