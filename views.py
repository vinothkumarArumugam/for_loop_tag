from django.shortccuts import render
def my_view (request):
  context={'data':[1,2,3,4,5,6]}   -----# context is for giving variable to the template ,we have to give key value(data here) as variable in html file like{{data}}
  return render(request,'app/display.html',context) it will render to the html file in teemplate
