import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify, make_response

app = Flask(__name__)
@app.route('/home',methods=['GET','POST'])
def home():
    req = request.get_json(silent=True, force=True)
    print(req)
    name = Response(req)
    url = "https://sheet.best/api/sheets/08bc4328-074b-4776-ba8a-753e33783ca3/Your Name as Per Aadhar/{}".format(name)
    res = requests.get(url)
    final_res=json.loads(res.text)[0]
    
    final_res=json.loads(res.text)[0]
    return "Here is the result \n Mobile Number:{} \n Email: {}".format(final_res['Mobile Number'],final_res['Email Address'])

@app.route('/response',methods=['GET','POST'])
def Response(req):
  try:
     result = req.get("queryResult")
     intent = result.get("intent").get('displayName')
     parameters = result.get("parameters")
     if intent == 'Default Welcome Intent':
        name = parameters.get("name")
        return name
        # url = "https://sheet.best/api/sheets/08bc4328-074b-4776-ba8a-753e33783ca3/Your Name as Per Aadhar/{}".format(name)
        # res = requests.get(url)
        
        # final_res=json.loads(res.text)[0]
        # print("Here is the result \n Mobile Number:{} \n Email: {}".format(final_res['Mobile Number'],final_res['Email Address']))
        # return "Here is the result \n Mobile Number:{} \n Email: {}".format(final_res['Mobile Number'],final_res['Email Address'])
  except IndexError:
    print("No user exists with that name")


if __name__ == "__main__":
    app.run(debug=True)


