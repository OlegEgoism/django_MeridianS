from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render

from .models import About_us, Worker, Clients, Contac, Certificates, Feedback
from .forms import FeedbackForm


def home(request):
    """Главная страница с информацией"""
    about_us = About_us.objects.filter(published=True)
    worker = Worker.objects.all()
    clients = Clients.objects.filter(published=True)
    contac = Contac.objects.all()
    certificates = Certificates.objects.filter(published=True)
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name='feedback.html')  # Переход после заполнения формы
    context = {
        'about_us': about_us,
        'worker': worker,
        'clients': clients,
        'contac': contac,
        'certificates': certificates,
        'form': form,
    }
    return render(request, template_name='home.html', context=context)


@receiver(post_save, sender=Feedback)
def my_handler(sender, **kwargs):
    """Отправка сообщений на почту через форму обратной связи"""
    name = kwargs['instance']
    mine = Feedback.objects.filter(name=name.name).last()  # Берет с QuerySet последний объект
    send_mail(
        subject='Новая заявка',
        message=f'Заявка от: {mine.name} Номер телефона: {mine.phone} Сообщение: {mine.message}',
        from_email="Starline",
        recipient_list=['olegpustovalov220@gmail.com'],  # почтовый ящик(и) куда отправляем письма
        fail_silently=False,
    )
