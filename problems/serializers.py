from rest_framework import serializers

class ProblemSerializer(serializers.Serializer):
    input_data = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'required': 'El campo es requerido',
            'blank': 'El campo no puede estar en blanco'
        }
    )
    
    def validate_input_data(self, value):
        pass
        return value