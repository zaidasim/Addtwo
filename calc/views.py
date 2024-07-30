from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        # Process form submission
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')
        
        if number1 and number2:
            # Calculate the result (for example, add the numbers)
            try:
                result = int(number1) + int(number2)
                return HttpResponse(f'The sum of {number1} and {number2} is {result}')
            except ValueError:
                return HttpResponse('Invalid input. Please enter valid numbers.')
        else:
            return HttpResponse('Both numbers are required.')
    
    # Display the form
    return render(request, 'home.html')
