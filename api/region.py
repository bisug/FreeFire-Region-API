from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/region', methods=['GET'])
def region_info():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "UID parameter is required"}), 400

    cookies = {
        'region': 'MA',
        'language': 'ar',
        'session_key': 'efwfzwesi9ui8drux4pmqix4cosane0y',
    }

    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'https://shop2game.com',
        'Referer': 'https://shop2game.com/app/100067/idlogin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'content-type': 'application/json',
        'x-datadome-clientid': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
    }

    json_data = {
        'app_id': 100067,
        'login_id': uid,
        'app_server_id': 0,
    }

    try:
        res = requests.post(
            'https://shop2game.com/api/auth/player_id_login',
            cookies=cookies, headers=headers, json=json_data
        )

        if res.status_code != 200 or not res.json().get('nickname'):
            return jsonify({"error": "ID NOT FOUND"}), 404

        player_data = res.json()
        return jsonify({
            "player_id": uid,
            "player_name": player_data.get('nickname', 'N/A'),
            "region": player_data.get('region', 'N/A')
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error"}), 500
