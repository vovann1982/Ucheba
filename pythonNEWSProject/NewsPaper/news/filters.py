from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Post, Author
from django.forms import DateInput


class PostFilter(FilterSet):
    vremia_sosdania_soobsh = DateFilter(label='Созданно до данной даты(не включая):',
                      lookup_expr='lte',
                      widget=DateInput(
                          attrs={
                              'type': 'date'
                          }
                      )
    )
    zagolovok = CharFilter(
        lookup_expr='icontains',
        label='Название статьи',
    )
    author = ModelChoiceFilter(
         queryset=Author.objects.all(),
         label='Автор',
    )

    class Meta:
        model = Post
        fields = ('vremia_sosdania_soobsh', 'zagolovok', 'author')

