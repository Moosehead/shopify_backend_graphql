from django.shortcuts import render
from random import randint

# Create your views here.

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
@api_view(['GET'])

def create_cart(request, format = None):
    cart_id = random_with_N_digits(4)
	return Response(cart_id)