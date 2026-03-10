import json
from flask import Blueprint, request

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def handle_webhook():
    data = json.loads(request.data)
    event_type = request.headers.get('X-Event-Name')

    if event_type == 'booking.created':
        handle_booking_created(data)
    elif event_type == 'booking.updated':
        handle_booking_updated(data)
    elif event_type == 'booking.canceled':
        handle_booking_canceled(data)

    return '', 200


def handle_booking_created(data):
    # Logic for handling a new booking
    print('Booking created:', data)


def handle_booking_updated(data):
    # Logic for handling an updated booking
    print('Booking updated:', data)


def handle_booking_canceled(data):
    # Logic for handling a canceled booking
    print('Booking canceled:', data)
