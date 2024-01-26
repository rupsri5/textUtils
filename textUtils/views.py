from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')
    # return HttpResponse('Home')

def analyze(request):
    #get the text
    djtext = request.POST.get("text", "default")
    
    #check for analyze type
    removepunc = request.POST.get("removepunc", "off")
    capitalize = request.POST.get("capitalize", "off")
    newlineremove = request.POST.get("newlineremove", "off")
    extraSpaceRemove = request.POST.get("extraSpaceRemove", "off")
    charCount = request.POST.get("charCount", "off")
    
    #variable which gives the analyzed string defined globally
    analyzed = ""
    
    #perform the required analyze task
    #1st-----------------------------------------------
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {"purpose": "Removed punctuations", "analyzed_text": analyzed}
        djtext=analyzed
        #analyze the text
        # return render(request, "analyze.html", params)
    
    #2nd-------------------------------------------------
    if capitalize == "on":
        for char in djtext:
            analyzed = analyzed + char.upper()
            
        params = {"purpose": "Convert text to Uppercase text.", "analyzed_text": analyzed} 
        djtext=analyzed   
        # return render(request, "analyze.html", params) 
    
    #3rd--------------------------------------------------
    if newlineremove == "on":
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
            
        params = {"purpose": "Removes the new line in text.", "analyzed_text": analyzed}   
        djtext=analyzed 
        # return render(request, "analyze.html", params) 
        
    #4th--------------------------------------------------
    if extraSpaceRemove == "on":
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]== " "):
                analyzed = analyzed + char
            
        params = {"purpose": "Removes extra space from text.", "analyzed_text": analyzed}
        djtext=analyzed    
        # return render(request, "analyze.html", params) 
        
    #5th--------------------------------------------------
    if charCount == "on":
        count = 0
        for char in djtext:
            count+=1
            
        params = {"purpose": "Convert text to Uppercase text.", "analyzed_text": count}
        djtext=analyzed    
        # return render(request, "analyze.html", params) 
                   
            
    if(charCount != "on" and extraSpaceRemove != "on"and newlineremove != "on"and capitalize != "on"and removepunc != "on"):
        return HttpResponse("Error! You havn't selected any operation. Please select any operation.")
    
    
    return render(request, "analyze.html", params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remover")

# def spaceremove(request):
#     return HttpResponse("Space remover")

# def charcount(request):
#     return HttpResponse("char count")