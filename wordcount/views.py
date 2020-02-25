from django.http import HttpResponse
from django.shortcuts import render
#we need to import the code for the operator
import operator

def homepage(request):
    return render(request, 'home.html')

#this variable is to call the about page template
def about(request):
    return render(request, 'about.html')

def count(request):

    #the fulltext comes from the url and then with request.GET we will get the elements
    #it has to be set equal to a variable, in this case the same fulltext
    fulltext = request.GET['fulltext']

    #this is to separate the words
    wordlist = fulltext.split()

    #the variable has to be equal to an empty dictionary
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    #to sort the words I define this variable and then I use it in the dictionary below
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    #dictionary. The attributes of the dictionary can be then inserted in the count.html file with
    #len is the length of the wordlist
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
