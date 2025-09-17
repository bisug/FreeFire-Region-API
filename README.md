Code is not working!

# 🌍 Free Fire Region Fetcher API

A simple Flask API that fetches the **player region** and **nickname** from a Free Fire UID.

---

## 📌 Features

- Lookup Free Fire player UID
- Returns nickname and region info
- Built with **Flask** + `requests`
- Deployable on **Vercel** in 1 click

---

## 📂 API Endpoint

### 🔍 Fetch Player Region

```
GET /region?uid=<free_fire_uid>
```

📥 Example Request:
```
https://sumiffregion.vercel.app/region?uid=123456789
```

📤 Example Response:
```json
{
  "player_id": "123456789",
  "player_name": "chfjdjs",
  "region": "US"
}
```

📛 Error Example:
```json
{
  "error": "ID NOT FOUND"
}
```

---

## 🧪 Local Setup (Optional)

```bash
git clone https://github.com/bisug/FreeFire-Region-API
cd ff-region-api
pip install -r requirements.txt
python app.py

```
## 🔗 One-Click Deploy to Vercel

Click below to instantly deploy your own Free Fire Region API.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/import?s=https://github.com/bisug/FreeFire-Region-API)

> ✏️ Replace `your-username` if you fork this repo.

---

## 📁 File Structure

```
ff-region-api/
├── app.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

## 🙏 Credits

- API made by [@dear_sumi](https://t.me/dear_sumi)
- Uses data from Garena’s shop2game.com

---

## ⚠️ Disclaimer

This is a free educational API and **not affiliated with Garena or Free Fire**. Use responsibly.
