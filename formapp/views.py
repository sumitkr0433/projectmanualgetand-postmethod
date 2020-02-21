from django.shortcuts import render
from django.http import HttpResponse
# from selenium import webdriver
# import time
# global driver
# driver=webdriver.Firefox(executable_path=r'E:\\proj23\geckodriver')
# driver.get('http://google.co.in')
# driver.maximize_windows()
# # Create your views here.


from formapp.models import Student
from formapp.forms import StudentForm

# Create your views here.
def student_input_view(request):
    markssubmitted=False
    name=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            form.save()
            markssubmitted=True
    form=StudentForm()
    return render(request,'testapp/input.html',{'form':form,'markssubmitted':markssubmitted,'name':name})


def home(request):
    return render(request, "home.html")


def clickwebsite(request):
	val1 = request.POST["num1"]
	res = val1
	try:
		parser=read_config_file()
		driver = webdriver.Firefox(executable_path='/Hadoop/dental_web_scraping/geckodriver',options=options)
		driver.maximize_window()
		driver.get(parser.get('read_section','site_url'))#Gets Signup page.
		#parser=read_config_file()
		driver=fill_form(driver,parser)
		sleep(10)
		driver.quit()
	except Exception as e:
		pass


	return render(request, "result.html", {"result": res})

