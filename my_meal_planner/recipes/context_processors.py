from .models import Tag

def tag_context(request):
    tags = Tag.objects.all()
    return{
        'tags': tags
    }