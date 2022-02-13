from django.shortcuts import render, redirect
from . models import Product
from . forms import ProductForm
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

# Create your views here.

def index(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()        

    context = {
        "products": products,
        "form": form
    }
    # url = 'https://etherscan.io/accounts/1?ps=100'
    # req = Request(url, headers={
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
    # response = urlopen(req, timeout=20).read()
    # response_close = urlopen(req, timeout=20).close()
    # page_soup = soup(response, "html.parser")
    # Transfers_info_table_1 = page_soup.find(
    #     "div", {"class": "table-responsive mb-2 mb-md-0"})
    # df = pd.read_html(str(Transfers_info_table_1))[0]
    # df.to_csv("TransferTable.csv", index=False)
    # tmp_data=pd.read_csv('TransferTable.csv',sep=';')
    # products = [
    #     Product(
    #         name = tmp_data.ix[row]['Address'],
    #         price = tmp_data.ix[row]['Balance'],
    #     )
    #     for row in tmp_data['Rank']
    # ]
    # Product.objects.bulk_create(products)

    return render(request, 'chartapp/index.html', context)


def pie(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pie')
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form
    }
    # url = 'https://etherscan.io/accounts/1?ps=100'
    # req = Request(url, headers={
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
    # response = urlopen(req, timeout=20).read()
    # response_close = urlopen(req, timeout=20).close()
    # page_soup = soup(response, "html.parser")
    # Transfers_info_table_1 = page_soup.find(
    #     "div", {"class": "table-responsive mb-2 mb-md-0"})
    # df = pd.read_html(str(Transfers_info_table_1))[0]
    # df.to_csv("TransferTable.csv", index=False)
    # tmp_data=pd.read_csv('TransferTable.csv',sep=';')
    # products = [
    #     Product(
    #         name = tmp_data.ix[row]['Address'],
    #         price = tmp_data.ix[row]['Balance'],
    #     )
    #     for row in tmp_data['Rank']
    # ]
    # Product.objects.bulk_create(products)

    return render(request, 'chartapp/pie.html', context)


def line(request):
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('line')
    else:
        form = ProductForm()

    context = {
        "products": products,
        "form": form
    }
    # url = 'https://etherscan.io/accounts/1?ps=100'
    # req = Request(url, headers={
    # 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'})
    # response = urlopen(req, timeout=20).read()
    # response_close = urlopen(req, timeout=20).close()
    # page_soup = soup(response, "html.parser")
    # Transfers_info_table_1 = page_soup.find(
    #     "div", {"class": "table-responsive mb-2 mb-md-0"})
    # df = pd.read_html(str(Transfers_info_table_1))[0]
    # df.to_csv("TransferTable.csv", index=False)
    # tmp_data=pd.read_csv('TransferTable.csv',sep=';')
    # products = [
    #     Product(
    #         name = tmp_data.ix[row]['Address'],
    #         price = tmp_data.ix[row]['Balance'],
    #     )
    #     for row in tmp_data['Rank']
    # ]
    # Product.objects.bulk_create(products)

    return render(request, 'chartapp/line.html', context)
