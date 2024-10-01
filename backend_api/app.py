import time
import random

import requests
from flask import Flask, jsonify

app = Flask(__name__)


def generate_log():
    logs = [
        "Success",
        "Created",
        "Failed",
    ]
    return random.choice(logs)


@app.route('/api_1')
def api_call():
    log_message = generate_log()
    print(f"Operation log: {log_message}")
    time.sleep(0.5)  # Wait for half a second
    return f"completed: {log_message}"


@app.route('/download_external_logs', methods=['GET'])
def download_external_logs():
    #  Download External logs API : Authenticates with $external_integration_key
    #  Here the variable external_integration_key stores the authenticate key and is passed into http headers.
    #  In case of multiple environments,
    #  we can import the $external_integration_key from the environment variable set using os.environ.get()
    #  or we can also import it from the Vault 3rd party applications and define another API and assigning the value.
    external_api_url = "https://sampleexternallink/auth/me"
    external_integration_key = "BuZz9zaXplPTUweDNzc1NbVvvGtNjJ9"
    headers = {"Authorization": "Bearer {}".format(external_integration_key)}

    response = requests.get(external_api_url, headers=headers)

    if response.status_code == 200:
        return jsonify({"message": "External logs downloaded successfully"}), 200
    else:
        return jsonify({"error": "Failed to download external logs"}), response.status_code


@app.route('/health_check')
def health_check():
    return f"healthy"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)    # # Adding 0.0.0.0 to enable listening from all interface.
