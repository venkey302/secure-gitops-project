from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "project": "secure-gitops"})

@app.route('/')
def home():
    return jsonify({"message": "Secure GitOps Pipeline Running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
