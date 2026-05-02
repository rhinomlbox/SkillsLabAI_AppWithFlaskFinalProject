''' Executing this function initiates the application of emotion detector
 to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request

# Import the emotion_analyzer function from the package created:
from EmotionDetection.emotion_detection import emotion_analyzer
#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    """
    Call the emotion_analyzer
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_analyzer(text_to_analyze)
    if 'dominant_emotion' in response:
        if response['dominant_emotion'] is None:
            return "Invalid text! Please try again!"
        message = "For the given statement, the system response is: "
        # Extract emotions and dominant emotion from response
        dom = ""
        for emote, score in response.items():
            if emote == 'dominant_emotion':
                dom = f"The dominant emotion is {score}."
            else:
                message += f"{emote}: {score} "
        message +=dom
    else:
        message = "For the given statement, the system response is: "
        for emote, score in response.items():
            message += f"{emote}: {score} "
    return message


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
