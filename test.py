# coding=gbk
data = {"status":"success","data":{"id":"5b8b9572e116fb3714e6fb02","content":"�ƺ�һȥ������������ǧ�ؿ����ơ�","popularity":1170000,"origin":{"title":"�ƺ�¥ / �ǻƺ�¥","dynasty":"�ƴ�","author":"���","content":["�����ѳ˻ƺ�ȥ���˵ؿ���ƺ�¥��","�ƺ�һȥ������������ǧ�ؿ����ơ�","�紨�������������������������ޡ�","��ĺ��غδ��ǣ��̲�����ʹ�˳"],"translate":["���յ������ѳ��Żƺ׷�ȥ����ط�ֻ���¿յ��Ļƺ�¥��","�ƺ�һȥ��Ҳû�з������ǧ������ֻ�а���ƮƮ���ơ�","�����紨��ı��������ɱ棬���ܿ��巼�ݷ�ï�������ޡ�","ʱ���ƻ費֪�δ����Ҽ��磿�������̲������ʹ�˷��"]},"matchTags":["����","�ƺ�¥"],"recommendedReason":"","cacheAt":"2021-07-15T20:13:24.839482"},"token":"SJxUGvwLDvqvge4z4/L+NWsdN1m0zj88","ipAddress":"113.57.176.188","warning":"null"}
data = data['data']['origin']
title = data['title']
dynasty = data['dynasty']
author = data['author']
content = data['content']
print(   "  ��"+title+"��"+'\n'+"    ���ߡ�"+dynasty+"��"+author)
print(*content, sep='\n')
