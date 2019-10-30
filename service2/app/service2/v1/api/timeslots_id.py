# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response, jsonify

from . import Resource
from .. import schemas
# from .data import timeslots, availableTime
timeslots=[
  {
    'time':"10:00 am",
    'owner':[1,2]
  },
  {
    'time':"11:00 am",
    'owner':[1]
  },
  {
    'time':"12:00 pm",
    'owner':[2]
  },
  {
    'time':"15:00 pm",
    'owner':[1]
  },
  {
    'time':"16:00 pm",
    'owner':[1,2]
  },
]
availableTime =[
{
    'time':"9:00 am"
},
{
    'time':"10:00 am"
},
{
    'time':"11:00 am"
},
{
    'time':"12:00 pm"
},
{
    'time':"13:00 pm"
},
{
    'time':"14:00 pm"
},
{
    'time':"15:00 pm"
},
{
    'time':"16:00 pm"
},
{
    'time':"17:00 pm"
},
]
print(availableTime,'222')
class TimeslotsId(Resource):
 
    def get(self, id):
        if id not in [1,2]:
            return {"code": 400, "message": "Not Found"}, 400
        timeOfId = []
        for i in availableTime:
            timeOfId.append(i)
        # print(timeOfId,'111')
        print( timeslots,'11ava')
        for time in timeslots:
            if id in time['owner']:
                # print(timeOfId,'222')
                timeOfId.remove({'time':time['time']})
                # print(timeOfId,'333')
        
        return timeOfId, 200, None

    def post(self, id):
        if id not in [1,2]:
            return {"code": 400, "message": "Not Found"}, 400
        print(g.args)
        temp = {}
        flag = 0
        for i in range(len(timeslots)-1):
            print(timeslots[i]['time'])
            if g.args['time'] == timeslots[i]['time']:
                # temp['time'] = g.args['time']
                # temp['owner'] g.args['time']
                if id in timeslots[i]['owner']:
                    return {"code": 400, "message": "Not Booked"}, 400
                timeslots[i]['owner'].append(id)
                print(timeslots,'apend')
                flag = 1
        if flag == 0:
            for time in availableTime:
                print(time,'qian')
                print(g.args['time'],'hou')
                if g.args['time'] == time['time']:
                    temp['time'] = g.args['time']
                    temp['owner'] = [id]
                    print(temp,'hahaha')
                    timeslots.append(temp)
                    print(timeslots,'ixixxi')
                    flag = 1
        if flag ==1:
            return make_response(jsonify(timeslots), 200)
        else:
            return {"code": 400, "message": "Not Booked"}, 400

    def delete(self, id):
        if id not in [1,2]:
            return {"code": 400, "message": "Not Found"}, 400
        delete_flag = 0
        print(g.args)
        for i in range(len(timeslots)):
            if g.args['time'] == timeslots[i]['time']:
                # temp['time'] = g.args['time']
                # temp['owner'] g.args['time']
                # print(timeslots[i],'t111')
                if id not in timeslots[i]['owner']:
                    # print(timeslots[i],'nonono')
                    return {"code": 400, "message": "Not Canceled"}, 400

                timeslots[i]['owner'].remove(id)
                delete_flag = 1
                if len(timeslots[i]['owner']) == 0:
                    timeslots.remove(timeslots[i])
        if delete_flag == 0:
            return {"code": 400, "message": "Not Canceled"}, 400
        return make_response(jsonify(timeslots), 200)