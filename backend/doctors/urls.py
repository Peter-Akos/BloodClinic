from django.urls import path
from doctors.views import ListCreateDoctorView, RetrieveUpdateDestroyDoctorView, ListCreateClinicView, \
    RetrieveUpdateDestroyClinicView, ListCreateDonorView, RetrieveUpdateDestroyDonorView, ListCreateDoctorsDonorsView, \
    ListCreateBloodBagView, RetrieveUpdateDestroyBloodBagView, DoctorBloodBagReport, ClinicReport, DonorReport

urlpatterns = [
    path('doctors/', ListCreateDoctorView.as_view()),
    path('doctors/<int:pk>', RetrieveUpdateDestroyDoctorView.as_view()),
    path('doctors/<int:doctor>/donors', ListCreateDoctorsDonorsView.as_view()),
    path('clinics/', ListCreateClinicView.as_view()),
    path('clinics/nr-doctors-report', ClinicReport.as_view()),
    path('clinics/<int:pk>', RetrieveUpdateDestroyClinicView.as_view()),
    path('clinics/<int:clinic_id>/doctor-bloodbag-report/', DoctorBloodBagReport.as_view()),
    path('donors/', ListCreateDonorView.as_view()),
    path('donors/<int:pk>', RetrieveUpdateDestroyDonorView.as_view()),
    path('donors/report', DonorReport.as_view()),
    path('bloodbags/', ListCreateBloodBagView.as_view()),
    path('bloodbags/<int:pk>', RetrieveUpdateDestroyBloodBagView.as_view()),
]
