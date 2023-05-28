from django.db import models
from .abstract import Base


class StopWord(models.Model):
    word = models.CharField(max_length=20, unique=True, verbose_name="Stop Word")

    def __str__(self) -> str:
        return self.word

    class Meta:
        verbose_name = "Stop word"
        verbose_name_plural= "Stop words"



class TelegramUser(Base):
    id = models.BigIntegerField(primary_key=True, verbose_name="Telegram User ID")
    chat_id = models.BigIntegerField(verbose_name="Telegram Chat ID")
    username = models.CharField(max_length=64, null=True, verbose_name="Telegram Username")
    active = models.BooleanField(default=False, verbose_name="Status is it available to send message")


    @property
    def available_to_send(self):
        return self.active
    
    def __str__(self) -> str:
        return str(self.id)
    
    class Meta:
        verbose_name = "Telegtam user"
        verbose_name_plural = "Telegtam users"
