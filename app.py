from flask import Flask, request, redirect, render_template_string
import requests

app = Flask(__name__)

form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enter Your Age</title>
</head>
<body>
    <h1>Please provide your age</h1>
    <form action="/submit" method="post">
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

collected_data = []

@app.route('/')
def home():
    return render_template_string(form_html)

@app.route('/submit', methods=['POST'])
def submit():
    age = request.form.get('age')
    ip = request.remote_addr
    
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    
    location = data.get('loc', 'Unknown')
    
    user_data = {
        "ip": ip,
        "location": location,
        "age": age
    }
    
    collected_data.append(user_data)
    print(f"Zozbierané údaje: {user_data}")
    
    return redirect("https://www.youtube.com/watch?v=xyz")

if __name__ == '__main__':
    app.run(debug=True)
