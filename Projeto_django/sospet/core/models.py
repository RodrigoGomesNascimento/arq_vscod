from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#criando as colunas da tabela do bd
# ver por que a class tem q ser criada como foi abaixo.
class Pet(models.Model):
    city = models.CharField(max_length=100)#campo e o tipo e a quantidade de caracter.
    description = models.TextField()# para inserção de textos longos mas ha outros
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    begin_date = models.DateTimeField(auto_now_add=True)# vair criar o horario que foi inserido os dados na tabela e incrementado automatico pelo auto
    photo = models.ImageField(upload_to='pet') # no banco fica o caminho da foto por isso esse imagefield
    active = models.BooleanField(default=True)#desafio para acertar o modo sempre que for criado vai estar ativo.
    user = models.ForeignKey(User, on_delete=models.CASCADE)# pois o django ja cria a tabela de user e vou importar para saber qual usuario criou o pet.
    # e vou deletar em cascata onde deletou o user deleto os pets dele.
    
    #Método para o pet obrigatorio para o django admin retornar uma string e criar o id automático.

    def __str__(self):
        return str(self.id)

#essa classe garante que onome do bd vai ser o da tabela.
    class Meta:
        db_table = 'pet'