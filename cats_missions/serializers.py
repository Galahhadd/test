from rest_framework import serializers


from .models import SpyCat, Mission, Target
from .validators import not_valid_breed

class CatSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpyCat
        fields = ['id', 'name', 'years_of_experience', 'breed', 'salary']
      

    def validate_breed(self, value):
        if not_valid_breed(value):
            raise serializers.ValidationError("Validation breed error!")
        print('OK')
        return value
        
    def update(self, instance, validated_data):
        # Only update salary if I correctly got the task
        instance.salary = validated_data.get('salary', instance.salary)
        instance.save()
        return instance
    
class TargetSeializer(serializers.ModelSerializer):

    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'complete']

    def validate_mission(self, value):

        if Target.objects.filter(value).exists():
            raise serializers.ValidationError("Target can only have one mission")
        return value

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSeializer(many = True)
    cat_id = serializers.IntegerField(allow_null=True, required = False)

    class Meta:
        model = Mission
        fields = ['id', 'cat_id', 'complete', 'targets']

    def validate_targets(self, value):

        if len(value) < 1:
            raise serializers.ValidationError("Not able to have less than 1 target")
        if len(value) > 3:
            raise serializers.ValidationError("More than 3 targets - not an option ")
        return value
    
    def create(self, validated_data):

        cat_id = validated_data.pop('cat_id', None)

        if cat_id is not None:
            try:
                kitty = SpyCat.objects.get(id=cat_id)
            except SpyCat.DoesNotExist:
                kitty = None
        else:
            kitty = None
                
        targets = validated_data.pop('targets')
        mission = Mission.objects.create(cat=kitty, **validated_data)
        for target_data in targets:
            Target.objects.create(mission=mission, **target_data)
        return mission
    
    def update(self, instance, validated_data):
        cat_id = validated_data.pop('cat_id', None)
        #targets = validated_data.pop('targets')

        if cat_id is not None:
            try:
                kitty = SpyCat.objects.get(id=cat_id)
                instance.cat = kitty
            except SpyCat.DoesNotExist:
                instance.cat = None
        else:
            instance.cat = None


        """
        TODO
        There should be part where we can update targets through missions, but I was stuck and didn't come up with any solution...

        """


        instance.save()

        return instance
           

        