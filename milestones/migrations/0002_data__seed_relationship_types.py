# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import migrations, models

from milestones.data import fetch_milestone_relationship_types


def seed_relationship_types(apps, schema_editor):
    """Seed the relationship types."""
    MilestoneRelationshipType = apps.get_model("milestones", "MilestoneRelationshipType")
    for name in fetch_milestone_relationship_types().values():
        MilestoneRelationshipType.objects.get_or_create(
            name=name,
            description='Autogenerated milestone relationship type "{}"'.format(name),
        )


def delete_relationship_types(apps, schema_editor):
    """Clean up any relationships we made."""
    MilestoneRelationshipType = apps.get_model("milestones", "MilestoneRelationshipType")
    for name in fetch_milestone_relationship_types().values():
        MilestoneRelationshipType.objects.filter(name=name).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('milestones', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_relationship_types, delete_relationship_types),
    ]
