import csv

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views import generic

from .models import File


class UploadCreateView(LoginRequiredMixin, generic.CreateView):
    '''Контроллер для загрузки файла'''
    model = File
    fields = ['upload_file', ]
    success_url = reverse_lazy('files:upload_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = File.objects.all()
        return context


class UploadListView(generic.ListView):
    '''Контроллер для просмотра списка файлов постранично по 3 файла на страницу'''
    model = File
    paginate_by = 3

    def get_queryset(self):
        '''Функция для получения набора обьектов из базы данных, в которой определяются 2 дополнительных поля с колонками и названием'''
        queryset = super().get_queryset()
        for i in queryset:
            file = str(i.upload_file)
            i.name = file[6:]
            with open("media/" + file, 'r', encoding='utf-8') as csv_file:
                li = list(csv.DictReader(csv_file))
                headers = ", ".join(li[0].keys())
            i.headers = headers
        return queryset


class UploadDetailView(LoginRequiredMixin, generic.DetailView):
    '''Контроллер для просмотра содержимого файла'''
    model = File

    def get_object(self):
        obj = super().get_object()
        with open("media/" + obj.upload_file.name, 'r', encoding='utf-8') as csv_file:
            li = list(csv.DictReader(csv_file))
            obj.li = li
            headers = li[0].keys()
            obj.headers = headers
            obj.save()
        return obj


class UploadDeleteView(generic.DeleteView):
    '''Контроллер для удаления файла'''
    model = File
    success_url = reverse_lazy('files:upload_list')
