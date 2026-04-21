"""
Task Serializers – Week 7 Demo

Demonstrates (Lesson 6):
  1. Basic Serializer       – manual field declaration (shown first on Day 2)
  2. ModelSerializer        – automatic field generation (shown after)
  3. SerializerMethodField  – computed / read-only field (Day 3)
  4. Field-level validation – validate_<field>()        (Day 3)

Trainer Note:
  Start with TaskSerializerBasic to show the verbose way.
  Then switch to TaskSerializer (ModelSerializer) to show how DRF saves time.
"""

from rest_framework import serializers
from .models import Task


# ─────────────────────────────────────────────────────────────────────────────
# Day 2 – Show first: Serializer (manual, verbose)
# ─────────────────────────────────────────────────────────────────────────────

class TaskSerializerBasic(serializers.Serializer):
    """
    Lesson 6a – Plain Serializer.
    Every field is declared manually.
    Used to illustrate the concept before showing ModelSerializer.
    """
    id          = serializers.IntegerField(read_only=True)
    title       = serializers.CharField(max_length=200)
    description = serializers.CharField(required=False, default='')
    completed   = serializers.BooleanField(default=False)
    created_at  = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title       = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed   = validated_data.get('completed', instance.completed)
        instance.save()
        return instance


# ─────────────────────────────────────────────────────────────────────────────
# Day 2/3 – Use this in the project: ModelSerializer (concise, powerful)
# ─────────────────────────────────────────────────────────────────────────────

class TaskSerializer(serializers.ModelSerializer):
    """
    Lesson 6b – ModelSerializer.
    Fields are derived from the model automatically.
    Adds a computed 'priority_display' field (SerializerMethodField).
    """

    # Lesson 6c – SerializerMethodField: computed, read-only
    priority_display = serializers.SerializerMethodField()

    class Meta:
        model  = Task
        fields = [
            'id',
            'title',
            'description',
            'completed',
            'priority',
            'priority_display',   # extra computed field
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_priority_display(self, obj):
        """Return human-readable priority label."""
        return obj.get_priority_display()

    # Lesson 6d – Field-level validation
    def validate_title(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long."
            )
        return value.strip()
