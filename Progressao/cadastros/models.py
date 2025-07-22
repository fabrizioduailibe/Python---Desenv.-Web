from django.db import models

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")

    def __str__(self):
    #    return super().__str__()

        # Formatação de estring de saída
        return "{} ({})".format(self.nome, self.descricao)