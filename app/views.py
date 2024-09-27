from flask import request, jsonify
from . import app, db
from .models import Customer, Order
import africastalking

# Initialize Africa's Talking SMS service
africastalking.initialize(app.config['AFRICASTALKING_USERNAME'], app.config['AFRICASTALKING_API_KEY'])
sms = africastalking.SMS

# Add a customer
@app.route('/customer', methods=['POST'])
def add_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], code=data['code'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer added'}), 201

# Add an order and send SMS
@app.route('/order', methods=['POST'])
def add_order():
    data = request.get_json()
    customer = Customer.query.get(data['customer_id'])
    if customer:
        new_order = Order(item=data['item'], amount=data['amount'], customer_id=customer.id)
        db.session.add(new_order)
        db.session.commit()

        # Send SMS after adding the order
        try:
            sms_response = sms.send(f"Order for {new_order.item} added with amount {new_order.amount} at {new_order.time}.", [customer.code])
            return jsonify({'message': 'Order added, SMS sent successfully'}), 201
        except Exception as e:
            return jsonify({'message': 'Order added, but SMS failed', 'error': str(e)}), 500

    return jsonify({'error': 'Customer not found'}), 404
