from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/torikumi')
def torikumi():
    return render_template('torikumi.html')

@app.route('/docker_lec')
def docker_lec():
    return render_template('docker_lec.html')

@app.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory('media', filename)

if __name__ == '__main__':
    app.run(debug=True)
