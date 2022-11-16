from django.db import models
from django.template.defaultfilters import slugify
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Create your models here.
class Dispositivos(models.Model):
    code = models.CharField(verbose_name='Código', max_length=20)
    name = models.CharField(verbose_name='Descrição', max_length=50) 
    maquina = models.CharField(verbose_name='Máquina', max_length=50, default='Padrão')   
    data_rev = models.DateField(verbose_name='Data de Revisão')

    def __str__(self):
        return self.code

    def get_data_rev(self):
        return self.data_rev

    def confiabilidade(self):
        data_revisao = datetime.strptime(str(self.data_rev), "%Y-%m-%d")
        current_time = datetime.now() 
        data_atual = datetime.strptime(f"{current_time.year}-{current_time.month}-{current_time.day}", "%Y-%m-%d")

        dif = data_revisao - data_atual
        dif = dif.days

        if dif <= 15:
            p = 0
        elif dif <= 30 and dif > 15:
            p = 20
        elif dif <= 90 and dif > 30:
            p = 75
        elif dif > 90:
            p = 100

        return p

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Dispositivos', slugify(self.code), instance)
        return None

    image = models.ImageField(verbose_name='Imagem', default='default/no_image.jpg', upload_to=image_upload_to, max_length=255)

class Servico(models.Model):
    dispositivo = models.ForeignKey(Dispositivos, verbose_name="Dispositivo", on_delete=models.CASCADE)
    nome = models.CharField(verbose_name='Nome', max_length=250)
    operador = models.CharField(verbose_name='Matricula', max_length=50)
    defeito = models.CharField(verbose_name='Descrição do Defeito', max_length=250)
    data_entrada = models.DateField(verbose_name='Data da Solicitação')

    def __str__(self):
        texto = (f"Dispositivo {self.dispositivo} com defeito {self.defeito} em {self.data_entrada}")
        return texto