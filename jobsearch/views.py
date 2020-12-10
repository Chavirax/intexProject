
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Employee
from .models import State
from .models import Contact_Information
from .models import Applicant
import json 
import os

# Create your views here.
def indexPageView(request):
    return render(request, 'jobsearch/index.html')

def aboutPageView(request):
    return render(request, 'jobsearch/about.html')  

def employerPageView(request):
    return render(request, 'jobsearch/employer.html')

def jobseekerPageView(request):
    return render(request, 'jobsearch/jobseeker.html')

#This is wheere the CRUD function starts

def empPageView(request) :
    data = Employee.objects.all()

    context = {
        "our_emps" : data
    }
    return render(request, 'jobsearch/displayEmps.html', context)

def findEmpPageView(request) :
    return render(request, 'jobsearch/searchemp.html')
            
def searchEmpPageView(request) :
    sFirst = request.GET['first_name']
    sLast = request.GET['last_name']
    data = Employee.objects.filter(emp_first=sFirst, emp_last=sLast)

    if data.count() > 0:
        context = {
            "our_emps" : data
        }
        return render(request, 'jobsearch/displayEmps.html', context)
    else:
        return HttpResponse("Not found")

def addEmpPageView(request):
    states = State.objects.all() 
    context = {
        "states": states,
        "titles" : [
                    ('Ms.', 'MISS'),
                    ('Mr.', 'MR.'),
                    ('Mrs.', 'MRS.'),
                    ('Mx', 'MX')
                    ]
    }    

    return render(request, 'jobsearch/addEmp.html', context)

def storeEmpPageView(request):
    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_employee = Employee()

        #Store the data from the form to the new object's attributes (like columns)
        new_employee.emp_first = request.POST.get('emp_first')
        new_employee.emp_last = request.POST.get('emp_last')
        new_employee.emp_title = request.POST.get('emp_title')

        #Get all of the State objects (record or records) for the current employee state
        new_state = State.objects.get(state_abbrev = request.POST.get('emp_state'))

        #Create a new Contact Information object (record)
        new_contact = Contact_Information()

        #Store the data from the form to the contact phone attribute (column) 
        new_contact.contact_phone = request.POST.get('contact_info')

        #Save the contact information record which will generate the autoincremented id
        new_contact.save()

        #Store the newly created contact information id (object or record reference) to the employee record
        new_employee.contact_information = new_contact

        #Store the State reference found to the employee state
        new_employee.emp_state = new_state

        #Save the employee record
        new_employee.save()

        #Make a list of all of the employee records and store it to the variable
        data = Employee.objects.all()

        #Assign the list of employee records to the dictionary key "our_emps"
        context = {
            "our_emps" : data
    }
    return render(request, 'jobsearch/displayEmps.html', context)    

def updateEmpPageView(request):
    sFirst = request.GET['emp_first']
    sLast = request.GET['emp_last']
    sNewLast = request.GET['new_last_name']

    #Find the employee record
    emp = Employee.objects.get(emp_first=sFirst, emp_last=sLast)  
    emp.emp_last = sNewLast  
    emp.save()  
    data = Employee.objects.all()

    #Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_emps" : data
    }
    return render(request, 'jobsearch/displayEmps.html', context )


def deleteEmpPageView(request):
    emp = Employee.objects.filter(emp_first=request.GET['emp_first'], emp_last=request.GET['emp_last']).delete()
    data = Employee.objects.all()

    #Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_emps" : data
    }
    return render(request, 'jobsearch/displayEmps.html', context) 

# functions for the IntexBase Database
def applicantPageView(request) :
    data = Applicant.objects.all()

    context  = {
        "our_applicants" : data
    }
    return render(request, 'jobsearch/displayA.html', context)

def findApplicantPageView(request) :
    return render(request, 'jobsearch/searchApplicant.html')

def searchApplicantPageView(request) :
    sFirst = request.GET['first_name']
    sLast = request.GET['last_name']
    
    data = Applicant.objects.filter(AFirstName=sFirst, ALastName=sLast)

    if data.count() > 0:
        context = {
            "our_applicants" : data
        }
        return render(request, 'jobsearch/displayA.html', context)
    else:
        return HttpResponse("Not found")

def addApplicantPageView(request):
    return render(request, 'jobsearch/addApplicant.html')

def storeApplicantPageView(request):
    #Check to see if the form method is a get or post
    if request.method == 'POST':

        #Create a new employee object from the model (like a new record)
        new_applicant = Applicant()

        #Store the data from the form to the new object's attributes (like columns)
        new_applicant.AFirstName = request.POST.get('AFirstName')
        new_applicant.ALastName = request.POST.get('ALastName')
        new_applicant.AEmail = request.POST.get('AEmail')
        new_applicant.AUsername = request.POST.get('AUsername')


        #Save the employee record
        new_applicant.save()

        #Make a list of all of the employee records and store it to the variable
        data = Applicant.objects.all()

        #Assign the list of employee records to the dictionary key "our_emps"
        context = {
            "our_applicants" : data
    }
    return render(request, 'jobsearch/displayA.html', context)   

def compatibilityPageView(request):
    return render(request, 'jobsearch/compatibility.html')

def job_candidatesPageView(request):
    return render(request, 'jobsearch/candidate_recommender1.html')

def job_candidates(request):
    import urllib 
    import urllib.request

    data1 =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["user_id", "job_title"],
                        "Values": [ [ request.GET['user_id'], request.GET['job_title'] ] ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data1))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/1a27dcdb0d174630b4eeb70b444132d5/services/20ea2bc2ab4943f4a50aa3092a5546a2/execute?api-version=2.0&details=true'
    api_key = '5rtEXKhY/xYTt1g7IHvjKsAXE8gtIGSw1u3NPonmvEfhSELq/mGw0cs/8Yfxq+QDXHKabdaeyTKp4His0goGQg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 
    response = urllib.request.urlopen(req)
    
    result = response.read()
    result = json.loads(result) # Convert JSON byte stream into dictionary
    prediction = result['Results']['output1']['value']['Values'][0]
    data1 = {'reco':str(f'1) {prediction[0]}, 2){prediction[1]},3) {prediction[2]}, 4){prediction[3]},5) {prediction[4]},6) {prediction[5]},7) {prediction[6]},8){prediction[7]}, 9){prediction[8]},10){prediction[9]}')}
    #data = 'candidate1:' + str([prediction[0]]) + os.linesep + 'candidate2:' + str([prediction[1]])  + os.linesep + 'candidate3:' + str([prediction[2]]) + os.linesep + 'candidate4:' + str([prediction[3]]) + os.linesep  +'candidate5:' + str([prediction[4]])+ os.linesep   +'candidate6:' +  str([prediction[5]]) + os.linesep+ 'candidate7:' +  str([prediction[6]]) + os.linesep + 'candidate8:' +  str([prediction[7]]) + os.linesep   + 'candidate9:' +  str([prediction[8]]) + os.linesep +  'candidate10:' +  str([prediction[9]]) + os.linesep 
    return render(request, 'jobsearch/result-candidate.html', data1)

def regression(request):

    import urllib
    # If you are using Python 3+, import urllib instead of urllib2
    import urllib.request
    import json 
    import os


    data2 =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["job_title", "matching_skills"],
                        "Values": [ [ request.GET['job_title'], request.GET['matching_skills'] ] ]
                        #"Values": [[ "Assistant Principal", '0']]
                    },        
                    },
                "GlobalParameters": 
                {
    }
        }

    body = str.encode(json.dumps(data2))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/1a27dcdb0d174630b4eeb70b444132d5/services/e0d15584469644f2b1b97737f0dba799/execute?api-version=2.0&details=true'
    api_key = 'tLJQUoIq0hfUpaDDdRHmxvsX/9YymvU2NGbvloXvtuNDk5kYaOMTs0dlQCrf5UxiiQC65cn4KoonjvYaVPINqQ==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}


    req = urllib.request.Request(url, body, headers) 
    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result) # Convert JSON byte stream into dictionary
    prediction = result['Results']['output1']['value']['Values'][0]
    data2 = {'result':str(f'{prediction[0]} compatibility with your profile is {prediction[1]}')}
    return render(request, 'jobsearch/result-co.html', data2)

def job_recommenderPageView(request) :
    return render(request, 'jobsearch/job_recommender.html')

def job_recommender(request):

    import urllib
    # If you are using Python 3+, import urllib instead of urllib2
    import urllib.request
    import json 
    import os
    data3 =  {
        "Inputs": {
            "input1":
                {
                    "ColumnNames": ["user_id", "job_title"],
                    "Values": [[request.GET['user_id1'], request.GET['job_title1']]]
                },        
            },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data3))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/1a27dcdb0d174630b4eeb70b444132d5/services/b9572b9dc9484c3a8ebb161a76226e66/execute?api-version=2.0&details=true'
    api_key = 'ZNvbQNZ5LRgGHxynwKrciIEWckhRzbzG5VVkUVNyytnGeAQQK1+elquTvSvOkIFGbTuGfGy8a18uoGFvxsB2Dg==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}


    req = urllib.request.Request(url, body, headers) 
    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result) # Convert JSON byte stream into dictionary
    prediction = result['Results']['output1']['value']['Values'][0]
    data3 = {'job':str(f'1) {prediction[0]}, 2){prediction[1]},3) {prediction[2]}, 4){prediction[3]},5) {prediction[4]},6) {prediction[5]},7) {prediction[6]},8){prediction[7]}, 9){prediction[8]},10){prediction[9]}')}
    #data = 'candidate1:' + str([prediction[0]]) + os.linesep + 'candidate2:' + str([prediction[1]])  + os.linesep + 'candidate3:' + str([prediction[2]]) + os.linesep + 'candidate4:' + str([prediction[3]]) + os.linesep  +'candidate5:' + str([prediction[4]])+ os.linesep   +'candidate6:' +  str([prediction[5]]) + os.linesep+ 'candidate7:' +  str([prediction[6]]) + os.linesep + 'candidate8:' +  str([prediction[7]]) + os.linesep   + 'candidate9:' +  str([prediction[8]]) + os.linesep +  'candidate10:' +  str([prediction[9]]) + os.linesep 
    return render(request, 'jobsearch/result-jobs.html', data3)