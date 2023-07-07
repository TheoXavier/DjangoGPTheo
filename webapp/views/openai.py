from django.shortcuts import render, redirect
from django.contrib import messages

linguagens = [
"c",
"cpp",
"clike",
"csharp",
"css",
"csv",
"django",
"go",
"html",
"markup",
"markup-templating",
"php",
"powershell",
"python",
"cshtml",
"java",
"javascript",
"jsx",
"ruby",
"rust",
"sql",
"typescript",
]

# Create your views here.
def redirect_correcao(request):
    return redirect('correcao')

def correcao(request):
    params = {
        "view":{
            "id":"correcao",
            "titulo": "Correção de código"
        },
        "linguagens":linguagens
    }
    if request.method == "POST":
        params["code"] = request.POST["code"]
        params["linguagens"] = request.POST["linguagem"]
        if params["linguagens"] == "Selecione a linguagem de programação":
            messages.success(request, "por favor, selecione uma linguagem")
            return(render, "correcao.html", params)
        #request para openAI depois
        params["response"] = params["code"]
    return render(request, 'correcao.html', params)