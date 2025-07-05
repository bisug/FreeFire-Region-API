from flask import Flask, request, jsonify
import requests
from vercel_wsgi import handle_request

app = Flask(__name__)

def get_player_info(Id):    
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "x-datadome-clientid": "10BIK2pOeN3Cw42~..."  # Replace with valid one
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    return requests.post(url, headers=headers, json=payload)

@app.route('/region', methods=['GET'])
def region():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"message": "Please provide a UID"}), 200

    response = get_player_info(uid)

    try:
        if response.status_code == 200:
            data = response.json()
            if not data.get('nickname') and not data.get('region'):
                return jsonify({"message": "UID not found, please check the UID"}), 200

            return jsonify({
                "uid": uid,
                "nickname": data.get('nickname', ''),
                "region": data.get('region', '')
            })
        else:
            return jsonify({"message": "UID not found, please check the UID"}), 200
    except Exception as e:
        return jsonify({"message": "Internal Error", "error": str(e)}), 500

# ✅ This is what Vercel uses to invoke your Flask app
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
