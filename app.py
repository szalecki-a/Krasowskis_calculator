from flask import Flask, request, jsonify, render_template
from integrator import data_converter

app = Flask(__name__)

@app.route('/main', methods=['POST'])
def main():
    data = request.json
    input_data = data.get('inputData', {})
    output_data = data_converter(input_data)

    return jsonify(output_data)


@app.route('/')
def index():
    return render_template('main.html')




if __name__ == '__main__':
    app.run(debug=True, port=5000)