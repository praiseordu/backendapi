from flask import Flask, request, jsonify
import datetime

app = Flask("my_app")  # Replace "my_app" with the desired name of your Flask application

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = "praise ordu"  # Set the Slack name to "praise ordu"
    track = "backend"  # Set the track to "backend"
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/praiseordu/backendapi/blob/main/app.py"
    github_repo_url = "https://github.com/praiseordu/backendapi"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
