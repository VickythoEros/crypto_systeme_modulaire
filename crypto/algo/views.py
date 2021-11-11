from django.shortcuts import render
from .fonctions import *
from django.http import JsonResponse

def system_1(request):

    number_of_solution = 0
    results_final = []
    value_r_int = 0
    click = False

    if request.method == 'POST':
        value_r = request.POST.get("value_r")
        if value_r :
            value_r_int = int(value_r)
            click = True
            result = algo_general_1(27,value_r_int)

            if result :
                for k in range(0, len(result), 3):
                    number_of_solution +=1
                    results_final.append([result[k], result[k+1], result[k+2] ])

            print(result)
            print(results_final)

    context = {'number_of_solution': number_of_solution,'results':results_final,'value_r_int':value_r_int,'click':click}

    return render(request, 'equations/systeme1.html', context)


def system_1_verify_1(request):

    results_final = False
    click = False
    context  ={}
    if request.method == 'POST':
        value_a = request.POST.get("value_a")
        value_b = request.POST.get("value_b")
        value_c = request.POST.get("value_c")
        value_r = request.POST.get("value_r")

        if value_r and value_a and value_b and value_c:
            click = True

            if verify_a_b_c_r(int(value_a),int(value_b),int(value_c),int(value_r)):
                results_final = True

            print(results_final)

        context = {'results':results_final,'click':click,'a':value_a,'b':value_b,'c':value_c,'r':value_r}

    return render(request, 'equations/systeme1_verify_1.html', context)




def system_2(request):

    number_of_solution = 0
    results_final = []
    value_r_int = 0
    click = False

    if request.method == 'POST':
        value_r = request.POST.get("value_r")
        if value_r :
            value_r_int = int(value_r)
            click = True
            result = []


       
            if result :
                for k in range(0, len(result), 3):
                    number_of_solution +=1
                    results_final.append([result[k], result[k+1], result[k+2] ])

            print(result)
            print(results_final)

    context = {'number_of_solution': number_of_solution,'results':results_final,'value_r_int':value_r_int,'click':click}

    return render(request, 'equations/systeme2.html', context)



def compute(request):
    # Calcul de l'opération
    return JsonResponse({})

def home(request):
    context = {'title': 'Mon super titre'}
    return render(request, 'base.html', context)