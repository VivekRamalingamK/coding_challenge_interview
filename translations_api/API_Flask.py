from flask import Flask, make_response
import pandas as pd


data_df = pd.read_csv("translation_data_cleaned.csv")

app = Flask(__name__)

#api = Api(app)

@app.route("/api/v1/status")
def get_status():
    message = f"This page contains no content expect for this statement"
    return make_response(message, 200)

@app.route("/api/v1/sentences")
def get_sentences():
    #return make_response(data_df.sample(n=10,replace=False,ignore_index=True).to_json(),200)
    return make_response(data_df.sample(n=10,replace=False,ignore_index=True).to_html(),200)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run()


#data_df.sample(n=10,replace=False,ignore_index=True).to_html