from django.shortcuts import render,redirect , get_object_or_404
from .forms import JobForm, CompanyRegistrationForm ,StudentRegistrationForm, StudentProfileForm, CompanyProfileForm
from .models import CompanyProfile, Job ,StudentProfile, Application
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Create your views here.
# This is a home function which render a index page in templates
def home(request):
    return render(request, 'core/index.html')





# This function create a job for student by the company
@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            company = request.user.companyprofile
            job.company = company
            job.save()
            return redirect('home')
    else:
         form = JobForm()

    return render(request,'core/create_job.html',{'form':form})






def register_company(request):
    
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            CompanyProfile.objects.create(
                user = user,
                company_name = form.cleaned_data['company_name'],
                website = form.cleaned_data['website'],
                location = form.cleaned_data['location'],
                description = form.cleaned_data['description']

            )
            return redirect('home')
    else:
        form = CompanyRegistrationForm()


    return render(request,'core/register_company.html',{'form':form})






def company_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect('create_job')

    return render(request,'core/company_login.html')






def job_list(request):

    search = request.GET.get('search', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')

    jobs = Job.objects.all().order_by('-created_at')

    if search:
        jobs = jobs.filter(
            title__icontains=search
        )

    if location:
        jobs = jobs.filter(
            location__icontains=location
        )

    if job_type:
        jobs = jobs.filter(
            job_type__icontains=job_type
        )

    return render(
        request,
        'core/job_list.html',
        {
            'jobs': jobs,
            'search': search,
            'location': location,
            'job_type': job_type
        }
    )






def job_detail(request,job_id):

    job = get_object_or_404(Job,id=job_id)

    return render(request, 'core/job_detail.html', {'job':job})

    



def register_Student(request):
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            StudentProfile.objects.create(
                user = user,
                

            )
            return redirect('home')
    else:
        form = StudentRegistrationForm()


    return render(request,'core/register_student.html',{'form':form})






def student_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request,'core/student_login.html')






@login_required
def student_profile(request):
    profile = request.user.studentprofile

    return render(request,'core/student_profile.html',{'profile':profile})




@login_required
def edit_student_profile(request):
    profile = request.user.studentprofile

    if request.method == 'POST':
        print(request.FILES)
        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=profile    
        )

        if form.is_valid():
            form.save()

            return redirect('student_profile')

    else:
        form = StudentProfileForm(instance=profile)

    return render(request, 'core/edit_student_profile.html',{'form':form})





@login_required
def apply_job(request, job_id):

    if not hasattr(request.user, 'studentprofile'):
        return HttpResponseForbidden(
            "Only students can apply for jobs."
        )

    job = get_object_or_404(Job, id=job_id)

    student = request.user.studentprofile

    Application.objects.create(
        student=student,
        job=job
    )

    return redirect('job_detail', job_id=job.id)


    




@login_required
def my_application(request):
    student = request.user.studentprofile
    applications = Application.objects.filter(
        student = student   
    ).order_by('applied_at')

    return render(request, 'core/my_application.html',{'applications':applications})



@login_required
def job_applicants(request, job_id):

    if not hasattr(request.user, 'companyprofile'):
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    company = request.user.companyprofile

    job = get_object_or_404(
        Job,
        id=job_id,
        company=company
    )

    applications = Application.objects.filter(
        job=job
    ).select_related(
        'student',
        'student__user'
    )

    return render(
        request,
        'core/job_applicants.html',
        {
            'job': job,
            'applications': applications
        }
    )



@login_required
def my_jobs(request):
    company = request.user.companyprofile
    jobs = Job.objects.filter(
        company = company   
    ).order_by('created_at')

    return render(request, 'core/my_jobs.html',{'jobs':jobs})




@login_required
def update_application_status(request, application_id):

    if not hasattr(request.user, 'companyprofile'):
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    company = request.user.companyprofile

    application = get_object_or_404(
        Application,
        id=application_id,
        job__company=company
    )

    if request.method == 'POST':

        status = request.POST.get('status')

        application.status = status
        application.save()

        return redirect(
            'job_applicants',
            job_id=application.job.id
        )




def user_logout(request):
    logout(request)
    return redirect('home')



@login_required
def company_profile(request):

    profile = request.user.companyprofile

    return render(
        request,
        'core/company_profile.html',
        {'profile': profile}
    )




@login_required
def edit_company_profile(request):

    profile = request.user.companyprofile

    if request.method == 'POST':

        form = CompanyProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('company_profile')

    else:
        form = CompanyProfileForm(instance=profile)

    return render(
        request,
        'core/edit_company_profile.html',
        {'form': form}
    )








@login_required
def student_dashboard(request):

    if not hasattr(request.user, 'studentprofile'):
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    return render(
        request,
        'core/student_dashboard.html'
    )





@login_required
def company_dashboard(request):

    if not hasattr(request.user, 'companyprofile'):
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    return render(
        request,
        'core/company_dashboard.html'
    )










@login_required
def edit_job(request, job_id):

    if not hasattr(request.user, 'companyprofile'):
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    company = request.user.companyprofile

    job = get_object_or_404(
        Job,
        id=job_id,
        company=company
    )

    if request.method == 'POST':

        form = JobForm(
            request.POST,
            instance=job
        )

        if form.is_valid():
            form.save()
            return redirect('my_jobs')

    else:
        form = JobForm(instance=job)

    return render(
        request,
        'core/edit_job.html',
        {'form': form}
    )







@login_required
def delete_job(request, job_id):

    if not hasattr(request.user, 'companyprofile'):
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    company = request.user.companyprofile

    job = get_object_or_404(
        Job,
        id=job_id,
        company=company
    )

    if request.method == 'POST':
        job.delete()
        return redirect('my_jobs')

    return render(
        request,
        'core/delete_job.html',
        {'job': job}
    )







@login_required
def admin_dashboard(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )

    total_students = StudentProfile.objects.count()
    total_companies = CompanyProfile.objects.count()
    total_jobs = Job.objects.count()
    total_applications = Application.objects.count()

    return render(
        request,
        'core/admin_dashboard.html',
        {
            'total_students': total_students,
            'total_companies': total_companies,
            'total_jobs': total_jobs,
            'total_applications': total_applications,
        }
    )
