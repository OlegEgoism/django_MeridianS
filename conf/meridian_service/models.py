from django.db import models


class About_us(models.Model):
    """Деятельность"""
    name = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание услуги', help_text='Не обязательное поле', blank=True)
    published = models.BooleanField('Опубликовать', default=False)

    class Meta:
        verbose_name = 'Деятельность'
        verbose_name_plural = 'Деятельность'

    def __str__(self):
        return self.name


class Worker(models.Model):
    """Сотрудники"""
    position = models.CharField('Должность сотрудника', max_length=250)
    name = models.CharField('ФИО сотрудника', max_length=250)
    phone = models.CharField('Телефон сотрудника', max_length=50, blank=True,
                             help_text='Не обязательное поле. Номер телефона указывать в формате +___(__)___-__-__')
    email = models.EmailField('Почта сотрудника', help_text='Не обязательное поле', max_length=250, blank=True)
    image = models.ImageField('Фото сотрудника', help_text='Рекомендуемый размер, ширина: 300, высота: 300',
                              upload_to='photos/%Y/%m/%d/', blank=True)
    published = models.BooleanField('Опубликовать', default=False)

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.position


class Clients(models.Model):
    """Наши клиенты"""
    name = models.CharField('Название клиента',
                            help_text='Для корректного отображения писать не более 22 символов', max_length=22)
    image = models.ImageField('Фото клиента', help_text='Рекомендуемый размер, ширина: 300, высота: 300',
                              upload_to='photos/%Y/%m/%d/', blank=True)
    published = models.BooleanField('Опубликовать', default=False)

    class Meta:
        verbose_name = 'Наш клиент'
        verbose_name_plural = 'Наши клиенты'

    def __str__(self):
        return self.name


class Contac(models.Model):
    """Контакты"""
    name = models.CharField('Название', max_length=200)
    address = models.CharField('Адрес офиса', max_length=100)
    phone1 = models.CharField('Номер телефона 1', max_length=50, blank=True,
                              help_text='Номер телефона указывать в формате +___(__)___-__-__')
    phone2 = models.CharField('Номер телефона 2', max_length=50, blank=True,
                              help_text='Номер телефона указывать в формате +___(__)___-__-__')
    email = models.EmailField('Почта офиса', max_length=250, blank=True)
    time_work1 = models.CharField('Время работы (будни)', max_length=100, blank=True)
    time_work2 = models.CharField('Время работы (выходные)', max_length=100, blank=True)
    maps = models.TextField('Расположение на карте', help_text='Вставить скрипт-ссылку с конструктора карт', blank=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class Certificates(models.Model):
    """Сертификаты"""
    name = models.CharField('Название сертификата', max_length=200)
    image = models.ImageField('Фото сертификата', help_text='Рекомендуемый размер, ширина: 400, высота: 600',
                              upload_to='photos/%Y/%m/%d/', blank=True)
    published = models.BooleanField('Опубликовать', default=False)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.name


class Feedback(models.Model):
    """Обратная связь"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=50)
    message = models.TextField('Сообщение')
    datetime = models.DateTimeField('Время отправки сообщения', auto_now=True)
    published = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return self.message
