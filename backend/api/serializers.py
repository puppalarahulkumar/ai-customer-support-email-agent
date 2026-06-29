from rest_framework import serializers

class EmailRequestSerializer(serializers.Serializer):
    email=serializers.CharField()
    sender_email=serializers.EmailField()
    email_id=serializers.CharField()