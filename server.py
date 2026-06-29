from flask import Flask, render_template, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page"""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    API endpoint for emotion detection.
    Accepts a text parameter and returns emotion analysis in the required format.
    """
    # Get the text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Validate that text was provided
    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    
    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if the emotion detection failed (all None values)
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    
    # Format the response as requested
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    
    return response_text

if __name__ == '__main__':
    # Run the Flask app on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)
