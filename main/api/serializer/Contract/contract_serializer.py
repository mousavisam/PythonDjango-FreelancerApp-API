from rest_framework import serializers

from main.enum.contract_status import ContractStatus
from main.model.contract_entity import Contract


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['proposal', 'delivery_time_in_day', 'payment_amount', 'payment_type', 'start_time']


class GetContractSerializer(serializers.ModelSerializer):
    proposal = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['proposal', 'delivery_time_in_day', 'payment_amount', 'payment_type', 'start_time', 'end_time',
                  'status', 'creation_time']

    def get_proposal(self, obj):
        return obj.proposal.task.title


class UpdateContractSerializer(serializers.Serializer):
    contract_id = serializers.IntegerField(min_value=1)
    status = serializers.ChoiceField(choices=ContractStatus.choices)


class MakeContractDoneSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(min_value=1)
    client_message = serializers.CharField(max_length=500, required=False, allow_blank=True)

    class Meta:
        model = Contract
        fields = ['client_message', 'is_done', 'id']
