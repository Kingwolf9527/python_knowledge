# ! /usr/bin/env python
# - * - coding:utf-8 - * -
# __author__ : KingWolf
# createtime : 2018/12/22 3:58

import json

dict1 = {'log_id': 8210485853468967382, 'words_result': [{'words': ', house', 'probability': {'average': 0.988221, 'variance': 0.000139, 'min': 0.976443}, 'location': {'width': 139, 'top': 12, 'left': 0, 'height': 27}, 'min_finegrained_vertexes_location': [{'y': 12, 'x': 0}, {'y': 12, 'x': 137}, {'y': 38, 'x': 137}, {'y': 38, 'x': 0}], 'finegrained_vertexes_location': [{'y': 12, 'x': 0}, {'y': 12, 'x': 22}, {'y': 12, 'x': 48}, {'y': 12, 'x': 73}, {'y': 12, 'x': 98}, {'y': 12, 'x': 123}, {'y': 12, 'x': 137}, {'y': 24, 'x': 137}, {'y': 37, 'x': 137}, {'y': 38, 'x': 137}, {'y': 38, 'x': 112}, {'y': 38, 'x': 87}, {'y': 38, 'x': 61}, {'y': 38, 'x': 36}, {'y': 38, 'x': 11}, {'y': 38, 'x': 0}, {'y': 26, 'x': 0}, {'y': 13, 'x': 0}], 'vertexes_location': [{'y': 12, 'x': 0}, {'y': 12, 'x': 137}, {'y': 38, 'x': 137}, {'y': 38, 'x': 0}]}], 'words_result_num': 1, 'direction': 0}

res = json.dumps(dict1)
print(res)