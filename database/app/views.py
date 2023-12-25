from os import name

from django.shortcuts import render
from .models import Account, Person


def index(request):
    # students = Student.objects.filter(course__name='History')
    # courses = Student.objects.get(id=1).courses.all()
    # return render(request, '', context={'students': students})
    # students = Student.objects.create(name = 'Tom')
    #  python = Course.objects.create(name='Python')
    # st = Student.objects.get(id=3)
    # his = Course.objects.get(name='History')
    #  his.Student_set.add(st)
    # res = Student.objects.get(id=3).course.all()
    # students = python.students_set.get_or_create(name="Bob")
    # res = his.Students_set.all()

    # django = Course2.objects.create(name="Django")
    # tom = Student2.objects.create(name="Tom")
    # res, _ = Enrollment.objects.create(students=tom, course=django, date='2023-11-11', mark=5)
    # st = Student2.objects.get(id=2)
    # crs = Course2.objects.get(id=1)
    # res = st.course.all()
    # res = crs.srudent2_ser.all()

    sam = Person.objects.create(name='qwradfassg')
    # res = Account.objects.get_or_create(login='Sam1233', password='Sam1233', user=Sam)
    # res = Account.objects.get(id=3)
    # res.user.name = 'Samuel'
    # res.save()
    # acc = Account(login='asdasdas', password='asdadsasd')
    # sam.account = acc
    # sam.account.save()
    res = Person.objects.get(account__login='Sam1233')
    return render(request, 'app/index.html', context={'students': res})





