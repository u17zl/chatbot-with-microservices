# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response, jsonify
import requests
from . import Resource
from .. import schemas


class Say(Resource):

    def post(self):
        print(g.json,'1111111')
        msg = g.json["message"]
        details = g.json["details"]

        query = {}
        print(g.json)
        print(details)
        # flow-based chat
        if msg == "handleBooking":
            query['time'] = details[0]['time']
            res = requests.post('http://127.0.0.1:5002/v1/timeslots/'+ str(details[0]['id']), params = query)
            if res.status_code == 200:
                data = res.json()
                return {'message':'booking successfully!','details':data}, 200, {'Access-Control-Allow-Origin': '*'}
            return {'message':'Not Found','details':[]}, 400, {'Access-Control-Allow-Origin': '*'}

        if msg == "handleInfo":
            res = requests.get('http://127.0.0.1:5001/v1/dentists')
            if res.status_code == 200:
                data = res.json()
                return {'message':'info','details':data}, 200, {'Access-Control-Allow-Origin': '*'}
            return {'message':'Not Found','details':[]}, 400, {'Access-Control-Allow-Origin': '*'}

        if msg == "handleInfoOfOne":
            print("hahah")
            res = requests.get('http://127.0.0.1:5001/v1/dentists/' +str(details[0]['name']))
            if res.status_code == 200:
                
                data = res.json()
                print(data)
                return {'message':'info of one','details':[data]}, 200, {'Access-Control-Allow-Origin': '*'}
            return {'message':'Not Found','details':[]}, 400, {'Access-Control-Allow-Origin': '*'}

        if msg == "handleCancel":
            id = details[0]['id']
            query['time'] = details[0]['time']
            print(id)
            print(query)
            res = requests.delete('http://127.0.0.1:5002/v1/timeslots/'+ str(id), params = query)
            if res.status_code == 200:
                data = res.json()
                return {'message':'booking cancel!','details':data},200, {'Access-Control-Allow-Origin': '*'}
            return {'message':'Not Found','details':[]}, 400, {'Access-Control-Allow-Origin': '*'}

        if msg == "handleAvailableTime":
            id = details[0]['id']
            res = requests.get('http://127.0.0.1:5002/v1/timeslots/'+ str(id))
            if res.status_code == 200:
                data = res.json()
                return {'message':'handleAvailableTime','details':data}, 200, {'Access-Control-Allow-Origin': '*'}
            return {'message':'Not Found','details':[]}, 400, {'Access-Control-Allow-Origin': '*'}


        print(g.json)
        headers = {'Authorization':'Bearer 3RZYZAXRLXFGPTMQAP47QQL3ZJLO4QDX'}
        url='https://api.wit.ai/message?v=20190801&q='+ msg
        r = requests.get(url, headers=headers)
        print(r,'111')
        data = r.json()
        print(data,'222')
        intent = data['entities']['intent'][0]['value']
        try:
            name = data['entities']['name'][0]['value']
        except:
            name = ''

        if intent == 'greeting':
            reply = {'message':intent,'details': []}
            response = make_response(jsonify(reply), 200)
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
            response.headers["Content-Type"] = 'POST, GET, OPTIONS, PUT, DELETE'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
            return response

        elif intent == 'noIntent':
            return {'message':intent,'details':[]}, 200, {'Access-Control-Allow-Origin': '*'}

        elif intent == 'bye':
            return {'message':intent,'details':[]}, 200, {'Access-Control-Allow-Origin': '*'}

        elif intent == 'showAvailableTime':
            res1 = requests.get('http://127.0.0.1:5001/v1/dentists')
            res1_data = res1.json()
            for i in res1_data:
                if i["name"] == name:
                    id = i["id"]
            res = requests.get('http://127.0.0.1:5002/v1/timeslots/'+ str(id))
            if res.status_code == 200:
                data = res.json()
                reply = {'message':intent,'details': data}
                response = make_response(jsonify(reply), 200)
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
                response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
                return response

        elif intent == 'showAvailableDoctors':
            res = requests.get('http://127.0.0.1:5001/v1/dentists')
            if res.status_code == 200:
                data = res.json()
                reply = {'message':intent,'details': data}
                response = make_response(jsonify(reply), 200)
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
                response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
                return response


        else:
            return {'message':'Not Found','details':[]}, 400, {'Access-Control-Allow-Origin': '*'}

        # return {'message':intent,'details':[]}, 200, None

# [{"id": 1, "location": "Zetland", "name": "Dr. Alex", "specialization": "Orthodontics"}, {"id": 2, "location": "Randwick", "name": "Dr. Lee", "specialization": "Paediatric Dentistry"}]