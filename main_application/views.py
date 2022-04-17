from math import sqrt,factorial,log,pow
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
import datetime
import logging
logger = logging.getLogger(__name__)

def render_calc(request):
	context = {"inputs" : "", "res" : ""}
	logger.warning('Calculator was accessed at ')
	return render(request, 'calc/calculator.html')

def perform(arg, ops):
	res = "PLEASE SELECT CORRECT OPERATION TO PERFORM"
	if ops == 'root':
		try:
			res = str(sqrt(int(arg)))
		except:
			res = "INVALID INPUT"
	elif ops == 'log':
		try:
			res = str(log(int(arg)))
		except:
			res = 'INVALID INPUT'
	elif ops == 'power':
		lis = arg.split(",")
		try:
			num = int(lis[0])
			exp = int(lis[1])
			res = str(pow(num, exp))
		except:
			res = 'INVALID INPUT'

	elif ops == 'fact':
		if(len(arg) >= 21):
			res = 'INVALID INPUT'
			return res
		try:
			res = str(factorial(int(arg)))
		except:
			res = 'INVALID INPUT'
	logger.warning('Operation result was '+ res)
	return res

def calculate(request):
	context = {"inputs" : "", "res" : ""}
	if request.method == 'POST':
		arg = request.POST["inputs"]	
		if not "inputs" in  request.POST:
			res = "PLEASE PROVIDE AN APPROPRIATE INPUT"
			context = {"inputs" : arg, "res" : res}
			logger.warning('Operation result was '+ res)
			return render(request, 'calc/calculator.html', context)

		if not "ops" in  request.POST:
			res = "PLEASE PROVIDE AN APPROPRIATE OPERATION"
			context = {"inputs" : arg, "res" : res}
			logger.warning('Operation result was '+ res)
			return render(request, 'calc/calculator.html', context)
		logger.warning('Reuest for performing operations with params ')
		ops = request.POST["ops"]
		if len(arg) == 0:
			res = "PLEASE PROVIDE AN APPROPRIATE INPUT"
			context = {"inputs" : arg, "res" : res}
			logger.warning('Operation result was '+ res)
			return render(request, 'calc/calculator.html', context)
        
		res = perform(arg, ops)
		context = {"inputs" : arg, "res" : res}

	return render(request, 'calc/calculator.html', context)
