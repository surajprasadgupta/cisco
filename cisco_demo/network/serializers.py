from network.models import router_details
from rest_framework import serializers

class routerSerializer(serializers.ModelSerializer):
    class Meta:
        model = router_details
        fields = '__all__' 