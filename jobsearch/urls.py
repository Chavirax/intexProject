from django.urls import path
from .views import indexPageView, aboutPageView, employerPageView, jobseekerPageView, empPageView
#from 403 project
from .views import searchEmpPageView
from .views import findEmpPageView        
from .views import addEmpPageView
from .views import storeEmpPageView
from .views import updateEmpPageView
from .views import deleteEmpPageView
#from intexBase database
from .views import applicantPageView
from .views import searchApplicantPageView
from .views import findApplicantPageView
from .views import addApplicantPageView
from .views import storeApplicantPageView
from .views import job_candidates
from .views import regression
from .views import compatibilityPageView, job_candidatesPageView
from .views import job_recommender, job_recommenderPageView


urlpatterns = [
    path('job_recommenderView/', job_recommenderPageView, name='job_recommenderView'),
    path('job_recommender/', job_recommender, name='job_recommender'),
    path('jobcandidates/', job_candidatesPageView, name='jobcandidates'),
    path('compatibility/', compatibilityPageView, name='compatibility'),
    path('regression/', regression, name='regression'),
    path('job_candidates/', job_candidates, name='job_candidates'),
    path("storeapplicant/", storeApplicantPageView, name="storeapplicant"),
    path("addapplicant/", addApplicantPageView, name="addapplicant"),
    path("searchapplicant/", searchApplicantPageView, name="searchapplicant"),
    path("findapplicant/", findApplicantPageView, name="findapplicant"),   
    path('applicants/', applicantPageView, name='applicants'),
    path("update/", updateEmpPageView, name="update"),
    path("delete/", deleteEmpPageView, name="delete"),
    path("storeemp/", storeEmpPageView, name="storeemp"),
    path("addemp/", addEmpPageView, name="addemp"),
    path("searchemp/", searchEmpPageView, name="searchemp"),
    path("findemp/", findEmpPageView, name="findemp"),    
    path('emp/', empPageView, name='employee'),
    path('about/', aboutPageView, name='about'),
    path('jobseeker/', jobseekerPageView, name='jobseeker'),
    path('employer/', employerPageView, name='employer'),
    path("",indexPageView, name='index'),
    
]
