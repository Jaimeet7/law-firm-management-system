from django.urls import path
from lawfirmmanagementsystem import views

urlpatterns = [
        path('advocate',views.casedetails,name='advocate'),
        path('enquiry',views.enquiry,name='enquiry'),
        path('appointment',views.appointment,name='appointment'),
        path('lawyer',views.lawyers,name='lawyer')
]