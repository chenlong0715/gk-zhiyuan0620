from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__, static_folder='static')

college_df = pd.read_csv('college_data.csv')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    score = data.get('score')
    province = data.get('province')
    want_major = data.get('major', '')

    res_df = college_df[
        (college_df['province'] == province) &
        (college_df['line_score'] <= score) &
        (college_df['major'].str.contains(want_major, na=False))
    ].sort_values(by='employment_rate', ascending=False)

    results = res_df.to_dict(orient='records')
    return jsonify({'code': 0, 'result': results})

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
