from flask import Flask, request, render_template_string

# Create the Flask app
app = Flask(__name__)

# HTML form template
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Court Data Fetcher</title>
</head>
<body>
    <h1>Court Data Fetcher</h1>
    <form method="POST">
        Case Type: <input name="case_type"><br><br>
        Case Number: <input name="case_number"><br><br>
        Filing Year: <input name="year"><br><br>
        <input type="submit" value="Search">
    </form>
</body>
</html>
"""

# Route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        case_type = request.form["case_type"]
        case_number = request.form["case_number"]
        year = request.form["year"]
        # For now, just display the input values
        return f"You searched for {case_type} {case_number}/{year}"
    return render_template_string(form_html)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
