from django.dispatch import receiver
from django.db.models.signals import post_save
from taekonline.models import Student, RankHistory, Rank
import datetime

@receiver(post_save, sender=Student)
def ensure_rank_history_exists(sender, instance, **kwargs):
    print(instance)
    if RankHistory.objects.filter(student=instance).count() == 0:
        if Rank.objects.all().count() > 0:
            first_rank = Rank.objects.all().order_by('order', 'id')[0]
            rh = RankHistory()
            rh.student = instance
            rh.rank = first_rank
            rh.exam_date = datetime.datetime.today()
            rh.save()
