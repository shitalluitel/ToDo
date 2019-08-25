from django.utils.functional import cached_property
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.commons.mixins.serializer_fields import JSONTextField as\
    JSONSerializerField
from apps.commons.fields import JSONTextField

class CustomModelSerializer(ModelSerializer):
    """
    Custom Model Serializer that contains field mapping of custom fields
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.serializer_field_mapping.update({
            JSONTextField: JSONSerializerField})


class DynamicFieldsModelSerializer(CustomModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` and 'exclude_fields'
    argument that controls which fields should be displayed and not to be
    displayed.
    """

    def __init__(self, instance=None, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        exclude_fields = kwargs.pop('exclude_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(
            instance, *args, **kwargs
        )

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
        # exclude fields
        if exclude_fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            exclude_fields = set(exclude_fields)
            for field_name in exclude_fields:
                self.fields.pop(field_name)

    def get_extra_kwargs(self):
        extra_kwargs = super().get_extra_kwargs()
        create_only_fields = getattr(self.Meta, 'create_only_fields', None)

        if self.instance and create_only_fields:
            for field_name in create_only_fields:
                kwargs = extra_kwargs.get(field_name, {})
                kwargs['read_only'] = True
                extra_kwargs[field_name] = kwargs

        return extra_kwargs

    @cached_property
    def request(self):
        return self.context.get("request")