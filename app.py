from flask import Flask, request, jsonify
from supabase import create_client, Client
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

# Initialize Supabase client
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    logger.error("Supabase credentials not found in environment variables")
    raise ValueError("Missing Supabase credentials")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

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
        
        # Optional: Add beacon IP address for tracking
        data['source_ip'] = request.remote_addr
        
        logger.info(f"Received beacon data: {data}")
        
        # Insert into Supabase
        result = supabase.table('beacon_messages').insert(data).execute()
        
        logger.info(f"Data saved to Supabase successfully")
        
        return jsonify({
            'success': True,
            'message': 'Data received and stored',
            'id': result.data[0]['id'] if result.data else None
        }), 201
        
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
        
        result = supabase.table('beacon_messages')\
            .select('*')\
            .order('received_at', desc=True)\
            .limit(limit)\
            .execute()
        
        return jsonify({
            'success': True,
            'count': len(result.data),
            'data': result.data
        }), 200
        
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
