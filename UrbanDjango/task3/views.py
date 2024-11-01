from django.shortcuts import render


# Create your views here.
def main(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request,'main.html', context)


def shop(request):
    title = 'Три сокровища'
    product1 = 'Керамическая кружка'
    product2 = 'Керамическая кружка с авторским рисунком'
    product3 = 'Шерстяной плед'
    context = {
        'title': title,
        'product1': product1,
        'product2': product2,
        'product3': product3,
    }
    return render(request,'shop.html', context)


def basket(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request,'basket.html', context)