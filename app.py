from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/story', methods=['POST'])
def story():
    noun = request.form['noun']
    verb = request.form['verb']
    adjective = request.form['adjective']
    place = request.form['place']

    story_text = f"Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb}."

    return render_template('story.html', story=story_text)

if __name__ == '__main__':
    app.run(debug=True)
