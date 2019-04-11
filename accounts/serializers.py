from rest_framework import serializers
from .models import Account, Allergy

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = (
          'nombre',
          'fecha_alta',
          'medicamento',
        )



class RecordSerializer(serializers.ModelSerializer):
    alergias = AllergySerializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = (
          'no_expediente',
          'fecha_ultima_consulta',
          'tipo_sangre',
          'alergias',
        )
