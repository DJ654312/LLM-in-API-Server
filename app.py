from flask import Flask, jsonify, request, render_template
from review_scraper import get_reviews
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Serve the homepage with the URL input form."""
    return render_template('index.html')

@app.route('/api/reviews', methods=['GET'])
def reviews():
    """Fetch reviews for a product based on the provided URL."""
    url = request.args.get('page')
    
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    try:
        reviews = get_reviews(url)
        reviews_count = len(reviews)
        return jsonify({
            "reviews_count": reviews_count,
            "reviews": reviews
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(debug=True, host='0.0.0.0', port=port)
