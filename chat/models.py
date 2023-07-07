from django.db import models
from django.contrib.auth.models import User
class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender",verbose_name="Отправитель")
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver",verbose_name="Получатель")
    message=models.CharField(max_length=500,verbose_name="Сообщение")
    date=models.DateTimeField(auto_now_add=True,verbose_name="Дата и время")
    is_read=models.BooleanField(default=False,verbose_name="Прочитано")


    def str(self) -> str:
        return f" {self.date} | {self.sender} | {self.receiver} | {self.message}"
    
    class Meta:
        verbose_name="Сообщение"
        verbose_name_plural="Сообщений"
        ordering=["-date"]