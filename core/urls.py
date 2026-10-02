from django.urls import path
from. import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_job/', views.create_job, name='create_job'),
    path('register_company/', views.register_company, name='register_company'),
    path('company_login/', views.company_login, name='company_login'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('register_student/', views.register_Student, name='register_student'),
    path('student_login/', views.student_login, name='student_login'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('edit_student_profile/',views.edit_student_profile,name='edit_student_profile'),
    path('apply_job/<int:job_id>/',views.apply_job,name='apply_job'),
    path('my_application/',views.my_application,name='my_application'),
    path('job_applicants/<int:job_id>/',views.job_applicants,name='job_applicants'),
    path('my-jobs/',views.my_jobs,name='my_jobs'),
    path('logout/',views.user_logout,name='logout'),
    path('company_profile/',views.company_profile,name='company_profile'),
    path('edit_company_profile/',views.edit_company_profile,name='edit_company_profile'),

    path('update-application-status/<int:application_id>/',views.update_application_status,name='update_application_status'),
]
