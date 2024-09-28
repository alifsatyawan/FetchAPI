from flask import Flask, request, jsonify, abort
from datetime import datetime
app = Flask(__name__)

# Initialize data structures
transactions = []
payer_balances = {}

@app.route('/add', methods=['POST'])
@app.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    if not data or 'payer' not in data or 'points' not in data or 'timestamp' not in data:
        return 'Invalid request data', 400

    payer = data['payer']
    points = data['points']
    timestamp_str = data['timestamp']

    try:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%dT%H:%M:%SZ')
    except ValueError:
        return 'Invalid timestamp format', 400

    # Sort transactions by timestamp
    transactions.sort(key=lambda x: x['timestamp'])

    if points < 0:
        # Adjust previous transactions for negative points
        points_to_deduct = -points  # Make it positive
        total_available_points = sum(
            t['remaining_points'] for t in transactions
            if t['payer'] == payer and t['timestamp'] <= timestamp and t['remaining_points'] > 0
        )

        if total_available_points < points_to_deduct:
            return 'Not enough points to deduct', 400

        for t in transactions:
            if t['payer'] == payer and t['timestamp'] <= timestamp and t['remaining_points'] > 0:
                deduction = min(t['remaining_points'], points_to_deduct)
                t['remaining_points'] -= deduction
                points_to_deduct -= deduction
                if points_to_deduct == 0:
                    break

    else:
        # Append transaction
        transaction = {
            'payer': payer,
            'points': points,
            'timestamp': timestamp,
            'remaining_points': points
        }
        transactions.append(transaction)

    # Update payer balance
    payer_balances[payer] = payer_balances.get(payer, 0) + points

    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    data = request.get_json()
    if not data or 'points' not in data:
        return 'Invalid request data', 400

    points_to_spend = data['points']
    if not isinstance(points_to_spend, int) or points_to_spend < 0:
        return 'Invalid points value', 400

    total_points = sum(payer_balances.values())
    if points_to_spend > total_points:
        return 'Not enough points', 400

    spend_summary = {}
    points_remaining_to_spend = points_to_spend

    for transaction in transactions:
        if points_remaining_to_spend == 0:
            break
        if transaction['remaining_points'] <= 0:
            continue
        payer = transaction['payer']
        available_points = transaction['remaining_points']
        payer_balance = payer_balances[payer]
        if payer_balance <= 0:
            continue

        points_to_deduct = min(available_points, points_remaining_to_spend, payer_balance)
        if points_to_deduct <= 0:
            continue

        transaction['remaining_points'] -= points_to_deduct
        payer_balances[payer] -= points_to_deduct
        spend_summary[payer] = spend_summary.get(payer, 0) - points_to_deduct
        points_remaining_to_spend -= points_to_deduct

    if points_remaining_to_spend > 0:
        return 'Error processing spend', 500

    # Convert spend_summary to list of dicts
    spend_list = [{'payer': payer, 'points': points} for payer, points in spend_summary.items()]

    return jsonify(spend_list), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    return jsonify(payer_balances), 200

if __name__ == '__main__':
    app.run(port=8000)
