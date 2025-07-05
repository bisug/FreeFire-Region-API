from flask import Flask, request, jsonify
from vercel_wsgi import handle_request
import requests

app = Flask(__name__)

def get_player_info(Id):    
    url = "https://shop2game.com/api/auth/player_id_login"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://shop2game.com",
        "Referer": "https://shop2game.com/app",
        "User-Agent": "Mozilla/5.0",
        "x-datadome-clientid": "your-client-id"
    }
    payload = {
        "app_id": 100067,
        "login_id": f"{Id}",
        "app_server_id": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    return response

@app.route('/region', methods=['GET'])
def region():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"message": "Please provide a UID"}), 200
    
    response = get_player_info(uid)
    
    try:
        if response.status_code == 200:
            original_response = response.json()
            if not original_response.get('nickname') and not original_response.get('region'):
                return jsonify({"message": "UID not found, please check the UID"}), 200
            
            return jsonify({
                "uid": uid,
                "nickname": original_response.get('nickname', ''),
                "region": original_response.get('region', '')
            })
        else:
            return jsonify({"message": "UID not found, please check the UID"}), 200
    except Exception:
        return jsonify({"message": "UID not found, please check the UID"}), 200

# ✅ Export correct handler for Vercel
def handler(environ, start_response):
    return handle_request(app, environ, start_response)
