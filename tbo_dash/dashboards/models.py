from django.db import models
from tbo_dash import users


class SensorValueType(models.Model):
    """Model definition for SensorValueType."""

    name = models.CharField("Имя", max_length=50)

    class Meta:
        verbose_name = 'Тип датчика'
        verbose_name_plural = 'Типы датчиков'

    def __str__(self):
        return self.name


class Sensor(models.Model):
    """Model definition for Sensor."""

    name = models.CharField("Имя", max_length=50)
    value_type = models.ForeignKey('SensorValueType',
                                   verbose_name='Тип датчика:',
                                   on_delete=models.SET_NULL,
                                   blank=True, null=True)
    device = models.ForeignKey('Device',
                               verbose_name='Устройство',
                               on_delete=models.CASCADE,
                               )

    class Meta:
        """Meta definition for Sensor."""

        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        """Unicode representation of Sensor."""
        return self.name


class SensorValue(models.Model):
    """Model definition for SensorValue."""

    sensor = models.ForeignKey(Sensor,
                               verbose_name="Датчик",
                               on_delete=models.CASCADE)
    timestamp = models.DateTimeField("Дата",
                                     auto_now=False,
                                     auto_now_add=False)

    value = models.CharField("Значение", max_length=128)

    class Meta:
        """Meta definition for SensorValue."""

        verbose_name = 'Значение сенсора'
        verbose_name_plural = 'Значения сенсоров'

    def __str__(self):
        return self.value


class Device(models.Model):
    """Model definition for Device."""

    name = models.CharField("Имя", max_length=50)
    fw_ver = models.CharField("Версия встроенного ПО",
                              max_length=20,
                              blank=True,
                              null=True)

    hw_info = models.CharField("Информация о железе",
                               max_length=128,
                               blank=True,
                               null=True)

    landfill = models.ForeignKey('Landfill',
                                 verbose_name="Полигон",
                                 on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Device."""

        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'

    def __str__(self):
        """Unicode representation of Device."""
        return self.name


class Landfill(models.Model):
    """Model definition for Landfill."""

    name = models.CharField("Имя", max_length=50)
    organization = models.ForeignKey(users.models.Organization,
                                     verbose_name="Организация",
                                     on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Landfill."""

        verbose_name = 'Полигон'
        verbose_name_plural = 'Полигоны'

    def __str__(self):
        """Unicode representation of Landfill."""
        return self.name


class Dashboard(models.Model):
    """Model definition for Dashboard."""

    name = models.CharField("Имя", max_length=50)
    landfills = models.ManyToManyField(Landfill)
    users = models.ManyToManyField(users.models.UserProfile)

    class Meta:
        """Meta definition for Dashboard."""

        verbose_name = 'Дашборд'
        verbose_name_plural = 'Дашборды'

    def __str__(self):
        """Unicode representation of Dashboard."""
        return self.name
