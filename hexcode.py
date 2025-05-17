from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

def valid_hex_chars(parameter_name):
    # Ensure it's 6 characters long before validating characters
    if len(hex_code) != 6:
        return False

    hex_code = hex_code.upper()  # Make case-insensitive

    for char in hex_code:
        if not (char.isdigit() or char in 'ABCDEF'):
            return False

    return True

# Code the 'valid_hex_chars' function here:

@app.route('/hex_form', methods=['GET', 'POST'])
def hex_form():
    hex = ''
    feedback = ''

    if request.method == 'POST':
        hex = request.form['hex']

        if len(hex) != 6:
            feedback = "Hex code must be exactly 6 characters long."
            hex = ''
        elif not valid_hex_chars(hex):
            feedback = "Hex code must only contain digits (0–9) and letters (A–F)."
            hex = ''
        else:
            feedback = ''  # Input is valid

    return render_template('hex_form.html', hex=hex, feedback=feedback)
if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
