from django.shortcuts import render,get_object_or_404
from django.contrib import messages

# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from .models import Freelancer
from .forms import FreelancerForm



# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FreelancerForm(request.POST)
        if form.is_valid():
            data = form.save()
            messages.success(request,'Data of  {} has been added!'.format(data.name))
    else:
        form = FreelancerForm()

    context = {
         'freelancers': Freelancer.objects.all(),
         'form':form,

     
     }
    return render(request, 'freelancer_profile/index.html', context=context)


def search_data(request):
    search = request.POST.get("search")
    form = FreelancerForm()
    try:
        freelancers = Freelancer.objects.filter(name__icontains=search)
    except:
        freelancers = None

    context = {
         'freelancers': freelancers,
         'form':form,
     }
    return render(request, 'freelancer_profile/search.html', context=context)



def get_behance_images(request,id):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    user = get_object_or_404(Freelancer,pk=id)

    img_urls =  set()
    driver.get(user.url)

    all_images = driver.find_elements_by_xpath('//div[@class="Cover-content-2R2"]/img')

    for actual_image in all_images:
        if actual_image.get_attribute('src') and 'https' in actual_image.get_attribute('src'):
            img_urls.add(actual_image.get_attribute('src'))


    print(all_images)
    driver.close()
    
    context = {
        'freelancer' : user,
        'all_images' : img_urls,
     }
    return render(request, 'freelancer_profile/get_images.html', context=context)

