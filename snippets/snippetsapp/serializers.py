from rest_framework import serializers
from snippetsapp.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style','owner',
                  'highlighted',]
        #在post的地方不能写，只能读
        read_only_fields = ('owner','highlighted',)



class UserSerializer(serializers.ModelSerializer):
    #正向查询，1对多去查
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']



# class SnippetSerializer(serializers.Serializer):
#     #read_only=True 表示为只读的
#     id = serializers.IntegerField(read_only=True)
#     #required=False 不是必须的 下一个允许为空
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         validated_data 为前端传过来的数据
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def  update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         instance为当前对象
#         validated_data 前端传过来的数据
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance