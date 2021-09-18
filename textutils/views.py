from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def response(request):
    # get text
    got_text = request.POST.get("text", 'default')
    print(got_text)
    # get actions
    upper = request.POST.get("upper", "off")
    print(upper)
    removepunc = request.POST.get("puncrem", "off")
    print(removepunc)
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    print(extraspaceremover)
    extralineremover = request.POST.get("Extralinesremover", "off")
    print(extralineremover)
    actions=[]
    analysed_text=""
    # checks
    if (upper!="off"):
        actions.append('UPPER CASE')
        got_text=got_text.upper()
    if (removepunc!="off"):
        actions.append('Remove Punctuation')
        string=""
        punctuations="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        for char in got_text:
            if  not(char in punctuations):
                string+=char
        got_text=string
    if (extraspaceremover!="off"):
        actions.append("Extra Space  Remover")
        string=""
        for index, char in enumerate(got_text):
            if not(got_text[index]==' ' and got_text[index+1]==' '):
                string+=char
        got_text=string
    if extralineremover=="on":
        actions.append("Extra Line Remover")
        analyzed=""
        for char in got_text:
            if char!="\n":
                analyzed=analyzed+char
        # Analyze the text
        got_text=analyzed
    print(got_text)
    print(actions)
    params = {"purpose": actions, "analysed_text": got_text}
    return render(request, 'response.html', params)