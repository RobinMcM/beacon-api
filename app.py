from flask import Flask, request, jsonify
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    logger.error("Supabase credentials not found in environment variables")
    raise ValueError("Missing Supabase credentials")

# Supabase REST API endpoint
SUPABASE_REST_URL = f"{SUPABASE_URL}/rest/v1/beacon_messages"

# Headers for Supabase API calls
HEADERS = {
    'apikey': SUPABASE_KEY,
    'Authorization': f'Bearer {SUPABASE_KEY}',
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/beacon/data', methods=['POST'])
def receive_beacon_data():
    """
    Endpoint to receive data from beacon via HTTP
    Expected JSON payload from beacon
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            logger.warning("Received empty payload")
            return jsonify({
                'error': 'No data provided',
                'success': False
            }), 400
        
        # Add server timestamp
        data['received_at'] = datetime.utcnow().isoformat()
        
        # Add beacon IP address for tracking
        data['source_ip'] = request.remote_addr
        
        logger.info(f"Received beacon data: {data}")
        
        # Insert into Supabase using REST API
        response = requests.post(
            SUPABASE_REST_URL,
            json=data,
            headers=HEADERS,
            timeout=10
        )
        
        if response.status_code in [200, 201]:
            result = response.json()
            logger.info("Data saved to Supabase successfully")
            
            return jsonify({
                'success': True,
                'message': 'Data received and stored',
                'id': result[0]['id'] if result else None
            }), 201
        else:
            logger.error(f"Supabase error: {response.status_code} - {response.text}")
            return jsonify({
                'error': f'Database error: {response.text}',
                'success': False
            }), 500
        
    except requests.exceptions.Timeout:
        logger.error("Supabase request timeout")
        return jsonify({
            'error': 'Database timeout',
            'success': False
        }), 504
        
    except Exception as e:
        logger.error(f"Error processing beacon data: {str(e)}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/beacon/data', methods=['GET'])
def get_beacon_data():
    """
    Optional: Endpoint to retrieve stored beacon data
    Query parameters:
    - limit: number of records to return (default: 100)
    """
    try:
        limit = request.args.get('limit', 100, type=int)
        
        # Query Supabase using REST API
        response = requests.get(
            f"{SUPABASE_REST_URL}?order=received_at.desc&limit={limit}",
            headers=HEADERS,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'success': True,
                'count': len(data),
                'data': data
            }), 200
        else:
            logger.error(f"Supabase error: {response.status_code} - {response.text}")
            return jsonify({
                'error': f'Database error: {response.text}',
                'success': False
            }), 500
        
    except Exception as e:
        logger.error(f"Error retrieving beacon data: {str(e)}")
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
