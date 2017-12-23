from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField,SerializerMethodField

from posts.models import Post 


class PostCreateSerializer(ModelSerializer):
	class Meta:
		model=Post
		fields=[
			'title',
			'description',
			'content'
		]	
class PostListSerializer(ModelSerializer):
	url=HyperlinkedIdentityField(
			view_name='posts:detail',
			lookup_field='slug'
		)
	user=SerializerMethodField()
	class Meta:
		model=Post
		fields=[
			'url',
			'user',
			'title',
			'description',
			'content'
		]
	def get_user(self,obj):
		return str(obj.user.username)

class PostDetailSerializer(ModelSerializer):
	image=SerializerMethodField()
	class Meta:
		model=Post
		fields=[
			'title',
			'description',
			'content',
			'image'
		]

	def get_image(self,obj):
		try:
			image=obj.image.url
		except:
			image = None
		return image