from taekonline.models import Student, Rank, RankHistory
import datetime
from django.contrib import messages

class StudentBusiness:

    def increase_rank(self, request, student_id, exam_date=datetime.datetime.now()):
        student = Student.objects.get(id=student_id)

        next_rank = None
        # If student already have a rank
        if student.rankhistory_set.all().count() > 0:
            current_rank = student.rankhistory_set.filter(student=student).order_by('-rank__order')[0].rank
            if (current_rank):
                if Rank.objects.filter(order__gt=current_rank.order).order_by('order').count() > 0:
                    next_rank = Rank.objects.filter(order__gt=current_rank.order).order_by('order')[0]
                else:
                    msg = 'Student {name} is already in the higgest rank'.format(name=student.name)
                    messages.warning(request, msg)
        # If student does not have a rank
        else:
            # The rank will be the first rank
            next_rank = Rank.objects.all().order_by('order')[0]
        
        if exam_date and next_rank:
            rh = RankHistory()
            rh.student = student
            rh.exam_date = exam_date
            rh.rank = next_rank
            rh.save()
    
