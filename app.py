from flask import Flask, request, jsonify
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
        "sec-ch-ua": '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "x-datadome-clientid": "10BIK2pOeN3Cw42~iX48rEAd2OmRt6MZDJQsEeK5uMirIKyTLO2bV5Ku6~7pJl_3QOmDkJoSzDcAdCAC8J5WRG_fpqrU7crOEq0~_5oqbgJIuVFWkbuUPD~lUpzSweEa",
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
