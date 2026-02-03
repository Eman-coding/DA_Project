"""
Fake Product Reviews Detection Website
Lightweight Flask application for university project
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 20 Products with images
PRODUCTS = [
    {'id': 1, 'name': 'Modern Laptop', 'image': 'modern_laptop_setup.jpg'},
    {'id': 2, 'name': 'Sleek Smartphone', 'image': 'sleek_smartphone_minimal.jpg'},
    {'id': 3, 'name': 'Wireless Speaker', 'image': 'wireless_speaker_lifestyle.jpg'},
    {'id': 4, 'name': 'Over-Ear Headphones', 'image': 'overear_headphones_studio.jpg'},
    {'id': 5, 'name': 'Smartwatch', 'image': 'smartwatch_clean_design.jpg'},
    {'id': 6, 'name': 'Power Bank', 'image': 'powerbank_desk_minimal.jpg'},
    {'id': 7, 'name': 'Coffee Cup', 'image': 'aesthetic_coffee_cup.jpg'},
    {'id': 8, 'name': 'Premium Pet Food', 'image': 'premium_catfood_pack.jpg'},
    {'id': 9, 'name': 'Mechanical Keyboard', 'image': 'mechanical_keyboard_workspace.jpg'},
    {'id': 10, 'name': 'Ergonomic Mouse', 'image': 'ergonomic_mouse_setup.jpg'},
    {'id': 11, 'name': 'Tablet', 'image': 'tablet_productivity_scene.jpg'},
    {'id': 12, 'name': 'Ultra Monitor', 'image': 'ultra_monitor_workspace.jpg'},
    {'id': 13, 'name': 'Digital Camera', 'image': 'digital_camera_studio.jpg'},
    {'id': 14, 'name': 'Home Printer', 'image': 'home_printer_setup.jpg'},
    {'id': 15, 'name': 'WiFi Router', 'image': 'wifi_router_modern.jpg'},
    {'id': 16, 'name': 'Wireless Earbuds', 'image': 'true_wireless_earbuds.jpg'},
    {'id': 17, 'name': 'Bluetooth Speaker', 'image': 'bluetooth_speaker_modern.jpg'},
    {'id': 18, 'name': 'Gaming Controller', 'image': 'gaming_controller_console.jpg'},
    {'id': 19, 'name': 'USB Flash Drive', 'image': 'usb_flash_drive_clean.jpg'},
    {'id': 20, 'name': 'Fast Charging Adapter', 'image': 'fast_charging_adapter.jpg'},
]

# Lazy model loading
_predictor = None

def get_predictor():
    """Load model only when needed"""
    global _predictor
    if _predictor is None:
        from model import predictor
        _predictor = predictor
        _predictor.load_model()
    return _predictor

@app.route('/')
def index():
    """Homepage with 20 products"""
    return render_template('index.html', products=PRODUCTS)

@app.route('/review/<int:product_id>')
def review_page(product_id):
    """Review input page"""
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('review.html', product=product)

@app.route('/predict', methods=['POST'])
def predict():
    """Predict review authenticity"""
    import json
    log_path = r'c:\laragon\www\DA_Project\.cursor\debug.log'
    
    try:
        # #region agent log
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'location': 'app.py:60', 'message': 'predict endpoint called', 'data': {}, 'timestamp': __import__('time').time() * 1000, 'sessionId': 'debug-session', 'runId': 'run1', 'hypothesisId': 'G'}) + '\n')
        # #endregion
        
        data = request.get_json()
        review_text = data.get('review', '').strip()
        product_id = data.get('product_id')
        
        # #region agent log
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'location': 'app.py:67', 'message': 'Request data parsed', 'data': {'hasReview': bool(review_text), 'productId': product_id}, 'timestamp': __import__('time').time() * 1000, 'sessionId': 'debug-session', 'runId': 'run1', 'hypothesisId': 'G'}) + '\n')
        # #endregion
        
        if not review_text:
            return jsonify({'error': 'Review text is required'}), 400
        
        product = next((p for p in PRODUCTS if p['id'] == product_id), None)
        product_name = product['name'] if product else 'Product'
        
        predictor = get_predictor()
        result = predictor.predict(review_text)
        
        # #region agent log
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'location': 'app.py:78', 'message': 'Prediction result', 'data': {'resultIsNone': result is None, 'hasLabel': result is not None and 'label' in result if result else False, 'hasFakeProb': result is not None and 'fake_probability' in result if result else False}, 'timestamp': __import__('time').time() * 1000, 'sessionId': 'debug-session', 'runId': 'run1', 'hypothesisId': 'H,B'}) + '\n')
        # #endregion
        
        if result is None:
            return jsonify({'error': 'Prediction failed'}), 500
        
        result['product_name'] = product_name
        result['review_text'] = review_text
        
        # #region agent log
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'location': 'app.py:85', 'message': 'Returning response', 'data': {'responseKeys': list(result.keys())}, 'timestamp': __import__('time').time() * 1000, 'sessionId': 'debug-session', 'runId': 'run1', 'hypothesisId': 'B'}) + '\n')
        # #endregion
        
        return jsonify(result)
    
    except Exception as e:
        # #region agent log
        with open(log_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps({'location': 'app.py:90', 'message': 'Exception in predict', 'data': {'error': str(e), 'errorType': type(e).__name__}, 'timestamp': __import__('time').time() * 1000, 'sessionId': 'debug-session', 'runId': 'run1', 'hypothesisId': 'G,F'}) + '\n')
        # #endregion
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
# this is the end of the file