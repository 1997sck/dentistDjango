from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})
	
def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		subject = request.POST['subject']
		
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			subject,
			message, # message
			message_email, # from email
			[''], # To Email
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def blog(request):
	return render(request, 'blog.html', {})

def doctors(request):
	return render(request, 'doctors.html', {})


def services(request):
	return render(request, 'services.html', {})


def about(request):
	return render(request, 'about.html', {})
	
def appointment(request):
	if request.method == "POST":

		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_time = request.POST['your-time']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']
		
		# send an email
		appointment = "Name: " + your_name +  " Email: " + your_email +" Schedule: " + your_time + " Time: " + your_date + " Message: " + your_message

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			[''], # To Email
			)
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_email': your_email,
			'your_time': your_time,
			'your_date': your_date,
			'your_message': your_message
			})

	else:
		return render(request, 'home.html', {})


	