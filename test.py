# coding=gbk
data = {"status":"success","data":{"id":"5b8b9572e116fb3714e6fb02","content":"黄鹤一去不复返，白云千载空悠悠。","popularity":1170000,"origin":{"title":"黄鹤楼 / 登黄鹤楼","dynasty":"唐代","author":"崔颢","content":["昔人已乘黄鹤去，此地空余黄鹤楼。","黄鹤一去不复返，白云千载空悠悠。","晴川历历汉阳树，芳草萋萋鹦鹉洲。","日暮乡关何处是，烟波江上使人愁。"],"translate":["昔日的仙人已乘着黄鹤飞去，这地方只留下空荡的黄鹤楼。","黄鹤一去再也没有返回这里，千万年来只有白云飘飘悠悠。","汉阳晴川阁的碧树历历可辨，更能看清芳草繁茂的鹦鹉洲。","时至黄昏不知何处是我家乡？看江面烟波渺渺更使人烦愁！"]},"matchTags":["华中","黄鹤楼"],"recommendedReason":"","cacheAt":"2021-07-15T20:13:24.839482"},"token":"SJxUGvwLDvqvge4z4/L+NWsdN1m0zj88","ipAddress":"113.57.176.188","warning":"null"}
data = data['data']['origin']
title = data['title']
dynasty = data['dynasty']
author = data['author']
content = data['content']
print(   "  《"+title+"》"+'\n'+"    作者·"+dynasty+"·"+author)
print(*content, sep='\n')
