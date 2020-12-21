# # encoding:utf-8
#
# import requests
# import base64
#
# '''
# 细粒度图像识别
# '''
# import requests
#
# # client_id 为官网获取的AK， client_secret 为官网获取的SK
#
# API_KEY = 'MPzwq6uMmuwaKKb1BsgRi3L1'
# SECRET_KEY = "Z8aNrpaGPGbUvwx5gs25i8q91Ss1fgEq"
# params = {
#     'grant_type':"client_credentials",
#     "client_id":API_KEY,
#     'client_secret':SECRET_KEY
# }
#
# host = 'https://aip.baidubce.com/oauth/2.0/token'
# response = requests.get(host,params=params)
# print(response.url)
# # AppID
# # API Key
# # Secret Key
# # test_ai
# # 22981141
# # MPzwq6uMmuwaKKb1BsgRi3L1
# # Z8aNrpaGPGbUvwx5gs25i8q91Ss1fgEq隐藏
# # API列表：
# if response:
#     print(response.json())
# s = dict(response.json())
#
# # 方式一鉴权使用的Access_token必须通过API Key和Secret Key获取。
# token = s.get('access_token')
#
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/classify/ingredient"
# # 二进制方式打开图片文件
# f = open('aaa.png', 'rb')
# img = base64.b64encode(f.read())
#
# params = {"image": img}
# access_token = token
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())

# num = 1
# for i in range(5):
#     f = open('res.json','a+')
#     f.write(str(num) + '\n')
#     num+=1

s = '<p>\xa0\xa0<spanstyle="font-family:宋体,SimSun;font-size:17px;">有一种感情只能拿心去感受</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">人活这一辈子，总会碰到几个特别的人，这类人可能只是你纯粹的精神寄托，但他不能被单纯的划归为朋友，因为他对你倾注的关爱超出了一般朋友的界限和理念，可你和他又不曾有过将之升华为爱人的那种具体行为（身体的归属），你们之间或者常常淡如水。\xa0\xa0</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">所以，这一类人，应该是介于情人与朋友之间的。</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">那，你和他之间的那种情感，那种超乎于寻常的友情、又不能简单的归类到爱情的情感，也只能是介于友情与爱情之间，也许你将它凌驾于友情与爱情之上。</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">他，可能曾经因你悲伤难过轻拍过你的背，可能因你怕黑牵过你的手，可能因你迷茫哭泣拥你入怀安抚，却，仅止于此。他的心时刻对你敞开，他的肩膀时刻准备让你依靠，你却只将他的容颜刻在了心房上。</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">你们不会放任自己散出耀眼的爱情光芒，不会放任自己燃出炙热的爱情火焰。你静静的想他，默默地念他。在你快乐的想唱歌欢跳时，你会在第一时间告诉他，因为你希望他在你的身边一起分享你的快乐和无忧，一同拥抱幸福。\xa0\xa0\xa0\xa0\xa0</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">可是，当你忧愁烦恼的时候，你同样会想起他，你依然希望他能陪在你身边，给你个坚实的臂弯让你靠。尽管你不需要他的任何语言任何安慰，只要倚在他的身边，你就会心静如水，熬过所有锥心疼痛...</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">可事实上，你却不曾向他诉说过，你怕属于自己的那份忧伤妨碍他平静的生活，你不想让他同你一起承担痛苦，你只是热切的希望他的世界里只有阳光沐浴。你或许会因为一首怀旧的老歌、一幕恋人的牵手想起他，想起他的宽容，想起他的宠爱。你或许会因为一道似曾相识的风景、一种触动心灵的相似的容颜想起他，想起他的真诚，想起他的执着。你更会因为午夜的星空、遥远的月亮想起他，想起他曾经带给你的欢乐，想起他带给你的无眠的美好……\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">此时，你的心里总是暖暖的，有三分美好，有三分感动，有三分憧憬，更有一分执着。你会执着于与他的情，与他的缘。他的叮咛，他的嘱咐，让你含着泪水说：你好罗嗦好烦人哦。心里却酸酸的，感觉那么的窝心，想留住一切...</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">你不求拥有，只盼能痴痴的守侯。你想绑住他在身旁，却怕妨碍他在蓝天白云间翱翔的自由。那些世俗的传统的道德理念，因他而瓦解，即使成为世人眼中的叛离者。而你只是在心底深处为这个人留了一个小小的空间，静静地固守着那份说不清的情感。即使陪伴寂寞，你亦不会后悔！</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">生命有时是无奈的，生活有时又是残酷的。当你觉得生命象一潭死水，寂静的没有一圈涟漪泛起时，你会心慌；当你觉得生活如一棵枯树，风干的寻不到一点生命的迹象时，你会心悸，你怕被生命遗忘，你怕被生活吞噬，但是，因为有了他的存在，你的生命多了条雨后的彩虹，你的生活有了满目的苍翠。\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">也许，终其一生你们也不会产生经典的"执子之手，与子偕老"的爱情故事，但是，你会因为拥有了这样一个朋友，更加的热爱自己的生活，珍惜自己的生命。</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">其实，你和他注定是两条没有交集的线段、夜空中闪烁的两颗永不相撞的星，不会酝酿出爱情果实，而且，你觉得似乎谈起爱情就亵渎了你们之间这份感情，这只能是一种超乎自然的、凌驾于爱情和友情之上的纯纯的另类情感。因为拥有了这种超然的情感，你变得更加的懂得坚强的生活，含笑走过那平淡的生命。即使没有一起慢慢变老，你依然心醉，为你拥有了那些无尽的回想与幻想，回想从前幻想未来...</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">你会很高兴，曾经拥有过那样一位朋友，曾经拥有过那样一份感情，纯净而又淡然，真挚而又绵长。你想他念他，或许你们的相识相知只是瞬间，可要彻底地忘记他却将花费你的一生，甚至终其一生他都会盘踞在你的内心深处，但是，你却很感激命运，感谢上苍给了你这样一个人，一个让你在这个世界上不再孤单，不再寂寞的人，即使是痛苦，也甜过麻木和苍白…\xa0\xa0\xa0\xa0</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">在这复杂的社会当中，在这无奈的人生当中，有这样一个人，当你不慎跌倒时，只要一抬头就可以看到关爱，当你走得疲倦时，只要一转身就可以找到依靠；有这样一种情感，当你受伤时会及时给予你宽慰，当你绝望时会及时拯救你的灵魂，你还奢求什么？</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">这样一个人、这样一种情感，让你飘荡的心变得柔软脆弱，让饱受折磨的心拥有了温润的一隅，更让你独享着一生眷恋和牵伴、一世宽容和给予，拥有着今生的思念与回忆、来生的执着与寄托！</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">这到底是怎样一类朋友，怎样一种情感？你只知道它真无香、淡如水…</span></p><p><spanstyle="font-family:宋体,SimSun;font-size:17px;">有一种情感，只能拿心去感受；有一种情感，只能用心去储藏…</span></p>\n\n\n<pclass="con_info">\n\n<b>版权声明</b>\n本文属于本站<b>\xa0\xa0原创</b>作品，文章版权归本站及作者所有，请尊重作者的创作成果，转载、引用自觉附上本文永久地址：\nhttps://www.lujianxin.com/x/art/0wqmorygw0yf\n\n</p>\n\n'

# print(type(s))
# out = "".join(s.split())
# print(out)

# priceList = '\n\t\t\t\t\t\t\t\tCHF\xa0\r\n        \r\n    \t64.90',
for price in s:
    # for i in price.strip():
    print(''.join(price.strip()))



# print(''.join(i.strip() for i in price.strip().split('\t')) for price in priceList)
