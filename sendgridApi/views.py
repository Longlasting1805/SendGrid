from django.shortcuts import render

# Create your views here.

import json
from django.http import JsonResponse
from sendgrid import SendGridAPIClient, SendGridHelpers
from sendgrid.helpers.mail import Mail, Email, Content

def send_appointment_confirmation(request):
    # Retrieve appointment details from the request body
    appointment_details = json.loads(request.body.decode('utf-8'))['appointmentDetails']

    # Initialize SendGrid API client
    sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')

    # Construct email message
    message = Mail(
        from_email=Email('appointment@yourdomain.com'),
        to_emails=Email(appointment_details['patientEmail']),
        subject='Appointment Confirmation',
        html_content=_generate_appointment_confirmation_html(appointment_details)
    )

    # Send the email using SendGrid API
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(e.message)
        return JsonResponse({'status': 'error'})

def send_appointment_reminder(request):
    # Retrieve appointment details from the request body
    appointment_details = json.loads(request.body.decode('utf-8'))['appointmentDetails']

    # Initialize SendGrid API client
    sg = SendGridAPIClient('YOUR_SENDGRID_API_KEY')

    # Construct email message
    message = Mail(
        from_email=Email('appointment@yourdomain.com'),
        to_emails=Email(appointment_details['patientEmail']),
        subject='Appointment Reminder',
        html_content=_generate_appointment_reminder_html(appointment_details)
    )

    # Send the email using SendGrid API
    try:
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(e.message)
        return JsonResponse({'status': 'error'})

def _generate_appointment_confirmation_html(appointment_details):
    # Generate HTML content for appointment confirmation email
    html_content = """
    <html>
        <head>
            <title>Appointment Confirmation</title>
        </head>
        <body>
            <p>Dear {}</p>
            <p>Thank you for booking an appointment with our clinic.</p>
            <p>Here are your appointment details:</p>
            <ul>
                <li>Doctor: {}</li>
                <li>Date: {}</li>
                <li>Time: {}</li>
                <li>Location: {}</li>
            </ul>
            <p>Please arrive 15 minutes prior to your appointment time.</p>
            <p>If you need to reschedule or cancel your appointment, please contact us at (123) 456-7890.</p>
            <p>We look forward to seeing you soon.</p>
            <p>Sincerely,</p>
            <p>The Clinic Team</p>
        </body>
    </html>
    """.format(appointment_details['patientName'], appointment_details['doctorName'], appointment_details['appointmentDate'], appointment_details['appointmentTime'], appointment_details['clinicLocation'])

    return html_content

def _generate_appointment_reminder_html(appointment_details):
    # Generate HTML content for appointment reminder email
    html_content = """
    <html>
        <head>
            <title>Appointment Reminder</title>
        </head>
        <body>
            <p>Dear {}</p>
            <p>This is a friendly reminder of your upcoming appointment with our clinic.</p>
            <p>Here are your appointment details:</p>
        <ul>
            <li>Doctor: {}</li>
            <li>Date: {}</li>
            <li>Time: {}</li>
</body>
</html>
                """
