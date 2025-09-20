"""
Flask web application for Python Foundation project.
"""
from flask import Flask, render_template, request, jsonify
from main import calculate_sum

app = Flask(__name__)


@app.route('/')
def index():
    """Main page of the web application."""
    return render_template('index.html')


@app.route('/demo')
def demo():
    """Demo page showing the original functionality."""
    # Example data from the original main.py
    numbers = [1, 2, 3, 4, 5]
    squared = [x**2 for x in numbers]
    sum_result = calculate_sum(numbers)
    
    demo_data = {
        'original_numbers': numbers,
        'squared_numbers': squared,
        'sum_result': sum_result,
        'message': 'Welcome to your Python Foundation Web App!'
    }
    
    return render_template('demo.html', data=demo_data)


@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    """API endpoint to calculate sum of numbers."""
    try:
        data = request.get_json()
        numbers = data.get('numbers', [])
        
        # Validate input
        if not isinstance(numbers, list):
            return jsonify({'error': 'Numbers must be provided as a list'}), 400
        
        if not all(isinstance(n, (int, float)) for n in numbers):
            return jsonify({'error': 'All items must be numbers'}), 400
        
        # Calculate results
        sum_result = calculate_sum(numbers)
        squared = [x**2 for x in numbers]
        
        return jsonify({
            'original_numbers': numbers,
            'sum': sum_result,
            'squared_numbers': squared,
            'count': len(numbers)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/calculator')
def calculator():
    """Interactive calculator page."""
    return render_template('calculator.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
