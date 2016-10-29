from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

LANGUAGES = settings.LANGUAGES
verbose_conteudo = _('Conteúdo')

class Exemplo(models.Model):
    conteudo = models.TextField(
        verbose_name = verbose_conteudo,
        )
    lang = models.CharField(
        verbose_name = _('Idioma'),
        max_length=20, 
        choices=LANGUAGES,
        default='pt-br')