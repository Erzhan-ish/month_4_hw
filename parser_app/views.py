from django.shortcuts import HttpResponse
from . import models, forms
from django.views import generic


class KinoogoListView(generic.ListView):
    template_name = 'parser/kinoogo_list.html'
    context_object_name = 'kinoogo'
    model = models.KinoogoModel
    paginate_by = 5

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class KinoogoFormView(generic.FormView):
    template_name = 'parser/kinoogo_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('STATUS 200')
        else:
            return super(KinoogoFormView, self).post(request, *args, **kwargs)
