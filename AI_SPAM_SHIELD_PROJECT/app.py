from flask import Flask, render_template, request

app = Flask(__name__)

spam_words = [
    "free","winner","won","lottery","claim","prize","money",
    "offer","click here","urgent","iphone","gift",
    "congratulations","cash","reward","selected"
]

@app.route("/", methods=["GET","POST"])
def home():
    result = ""
    confidence = 0

    if request.method == "POST":
        message = request.form["message"].lower()
        score = 0

        for word in spam_words:
            if word in message:
                score += 1

        if score >= 2:
            result = "SPAM"
            confidence = min(60 + score * 8, 99)
        else:
            result = "NO SPAM"
            confidence = max(90 - score * 10, 70)

    return render_template("index.html", result=result, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
