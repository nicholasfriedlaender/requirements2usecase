import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from plantuml import PlantUML
import json

app = Flask(__name__)

# Allow all origins (not recommended in production)
CORS(app)

@app.route('/llama/actors', methods=['POST'])
def api1():
    # Forward the POST request to the server behind the VPN
    print(request.json)
    response = requests.post('http://129.69.217.24:5000/llama/actors', json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/llama/useCases', methods=['POST'])
def api2():
    # Forward the POST request to the server behind the VPN
    print(request.json)
    response = requests.post('http://129.69.217.24:5000/llama/useCases', json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/llama/model', methods=['POST'])
def api3():
    # Forward the POST request to the server behind the VPN
    print(request.json)
    response = requests.post('http://129.69.217.24:5000/llama/model', json=request.json)
    print("This is my response from the LLM", response.json())
    plantuml = PlantUML('http://www.plantuml.com/plantuml/img/')

    # Get the diagram value from the response dictionary
    response_text = response.json().get('diagram', '')

    # Find the start and end of the PlantUML code block
    start_marker = '@startuml'
    end_marker = '@enduml'

    # Extract the PlantUML code between the start and end markers, inclusive
    start_index = response_text.find(start_marker)
    end_index = response_text.find(end_marker) + len(end_marker)

    if start_index != -1 and end_index != -1:
        plantuml_code = response_text[start_index:end_index].strip()

        # Get the URL of the model using the PlantUML code
        model_url = plantuml.get_url(plantuml_code)
    else:
        # Handle case where extraction fails
        print("Failed to extract PlantUML code")
        return jsonify({"error": "Failed to extract PlantUML code"}), 400

    # Find the start and end of the JSON block
    json_start_marker = 'jsonStart'
    json_end_marker = 'jsonEnd'

    # Extract the JSON code between the start and end markers, inclusive
    json_start_index = response_text.find(json_start_marker)
    json_end_index = response_text.find(json_end_marker)

    if json_start_index != -1 and json_end_index != -1:
        json_code = response_text[json_start_index + len(json_start_marker):json_end_index].strip()

        # Parse the JSON code
        try:
            json_object = json.loads(json_code)
        except json.JSONDecodeError as e:
            print("Failed to decode JSON:", e)
            return jsonify({"error": "Failed to decode JSON"}), 400

        # Return the model URL and the JSON object
        return jsonify({"plantUML": plantuml_code, "model_url": model_url, "json_object": json_object}), response.status_code
    else:
        # Handle case where JSON extraction fails
        print("Failed to extract JSON code")
        return jsonify({"error": "Failed to extract JSON code"}), 400

@app.route('/llama/refine', methods=['POST'])
def api4():
    # Forward the POST request to the server behind the VPN
    print(request.json)
    response = requests.post('http://129.69.217.24:5000/llama/refine', json=request.json)


    plantuml = PlantUML('http://www.plantuml.com/plantuml/img/')

    response_text = response.json().get('refinement', '')

    # Find the start and end of the PlantUML code block
    start_marker = '@startuml'
    end_marker = '@enduml'

    # Extract the PlantUML code between the start and end markers, inclusive
    start_index = response_text.find(start_marker)
    end_index = response_text.find(end_marker) + len(end_marker)

    if start_index != -1 and end_index != -1:
        plantuml_code = response_text[start_index:end_index].strip()

        # Get the URL of the model using the PlantUML code
        model_url = plantuml.get_url(plantuml_code)
    else:
        # Handle case where extraction fails
        print("Failed to extract PlantUML code")
        return jsonify({"error": "Failed to extract PlantUML code"}), 400

    # Find the start and end of the JSON block
    json_start_marker = 'jsonStart'
    json_end_marker = 'jsonEnd'

    # Extract the JSON code between the start and end markers, inclusive
    json_start_index = response_text.find(json_start_marker)
    json_end_index = response_text.find(json_end_marker)

    if json_start_index != -1 and json_end_index != -1:
        json_code = response_text[json_start_index + len(json_start_marker):json_end_index].strip()

        # Parse the JSON code
        try:
            json_object = json.loads(json_code)
        except json.JSONDecodeError as e:
            print("Failed to decode JSON:", e)
            return jsonify({"error": "Failed to decode JSON"}), 400

        # Return the model URL and the JSON object
        return jsonify(
            {"plantUML": plantuml_code, "model_url": model_url, "json_object": json_object}), response.status_code
    else:
        # Handle case where JSON extraction fails
        print("Failed to extract JSON code")
        return jsonify({"error": "Failed to extract JSON code"}), 400


if __name__ == '__main__':
    app.run(port=5000)
