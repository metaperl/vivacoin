from steem import Steem
s = Steem()

for v in s.get_active_votes('awarenessraiser', 'vlog-13-introduced-high-level-music-ceo-to-steemit-luxury-clips-inside'):
    print(v)

'''
python3 get_active_votes.py
{'voter': 'berkah', 'weight': 1084, 'rshares': '9097363023', 'percent': 100, 'reputation': '59326661645', 'time': '2017-08-15T08:11:42'}
{'voter': 'supreme', 'weight': 2509, 'rshares': '21046330912', 'percent': 10000, 'reputation': '4004654739505', 'time': '2017-08-15T10:02:45'}
{'voter': 'pnc', 'weight': 432, 'rshares': 3622351772, 'percent': 100, 'reputation': '15115607464698', 'time': '2017-08-15T08:11:39'}
{'voter': 'adsactly', 'weight': 894895, 'rshares': '7506916007052', 'percent': 3000, 'reputation': '14513342009983', 'time': '2017-08-15T07:17:45'}
{'voter': 'full-measure', 'weight': 197867, 'rshares': '414957380117', 'percent': 10000, 'reputation': '5759487944232', 'time': '2017-08-15T00:16:57'}
{'voter': 'teamsteem', 'weight': 88298, 'rshares': '185174850252', 'percent': 100, 'reputation': '89956709508172', 'time': '2017-08-15T00:16:51'}
{'voter': 'nanzo-scoop', 'weight': 349357, 'rshares': '495682730204', 'percent': 1000, 'reputation': '113540244013467', 'time': '2017-08-15T00:04:42'}
{'voter': 'mummyimperfect', 'weight': 706, 'rshares': '5916745319', 'percent': 1000, 'reputation': '27490656076176', 'time': '2017-08-15T08:00:42'}
{'voter': 'ak2020', 'weight': 1213, 'rshares': '10181483823', 'percent': 1000, 'reputation': '5456071456055', 'time': '2017-08-15T08:00:42'}
{'voter': 'applecrisp', 'weight': 59, 'rshares': 498145449, 'percent': 2500, 'reputation': '2827974555183', 'time': '2017-08-15T04:52:15'}
{'voter': 'lauralemons', 'weight': 45, 'rshares': 374165961, 'percent': 50, 'reputation': '61096910775310', 'time': '2017-08-15T08:11:42'}
{'voter': 'hitmeasap', 'weight': 24, 'rshares': 205576832, 'percent': 100, 'reputation': '32957805738287', 'time': '2017-08-15T08:11:45'}
{'voter': 'beanz', 'weight': 234128, 'rshares': '1964008794778', 'percent': 10000, 'reputation': '58241520721567', 'time': '2017-08-15T03:58:12'}
{'voter': 'alexpmorris', 'weight': 12929, 'rshares': '108458787865', 'percent': 10000, 'reputation': '19240578983839', 'time': '2017-08-15T04:58:15'}
{'voter': 'theprophet0', 'weight': 1598538, 'rshares': '7588303064051', 'percent': 10000, 'reputation': '34814567701176', 'time': '2017-08-15T03:11:30'}
{'voter': 'cabelindsay', 'weight': 51, 'rshares': 216158632, 'percent': 10000, 'reputation': '126898947992', 'time': '2017-08-15T02:21:09'}
{'voter': 'michelnilles', 'weight': 1647, 'rshares': 3454043005, 'percent': 1000, 'reputation': '12352169106070', 'time': '2017-08-15T01:23:33'}
{'voter': 'lamech-m', 'weight': 24, 'rshares': 199562366, 'percent': 100, 'reputation': '998787616929', 'time': '2017-08-15T08:11:42'}
{'voter': 'richardcrill', 'weight': 53619, 'rshares': '112447243437', 'percent': 3300, 'reputation': '39099713735672', 'time': '2017-08-15T00:50:39'}
{'voter': 'swisswatcher', 'weight': 240, 'rshares': 2016393783, 'percent': 100, 'reputation': '2932523710927', 'time': '2017-08-15T08:11:42'}
{'voter': 'robertchr', 'weight': 287, 'rshares': 2409301674, 'percent': 900, 'reputation': '124240805799', 'time': '2017-08-15T05:51:12'}
{'voter': 't-bot', 'weight': 7011, 'rshares': '5669899200', 'percent': 1000, 'reputation': '812424241352', 'time': '2017-08-15T00:04:27'}
{'voter': 'samanthabonin', 'weight': 471, 'rshares': 989410402, 'percent': 200, 'reputation': '1151850704121', 'time': '2017-08-15T00:36:57'}
{'voter': 'mafeeva', 'weight': 1060, 'rshares': '8889286188', 'percent': 1000, 'reputation': 0, 'time': '2017-08-15T08:00:42'}
{'voter': 'road2wisdom', 'weight': 130954, 'rshares': '61501041974', 'percent': 10000, 'reputation': '12911801465263', 'time': '2017-08-15T00:03:00'}
{'voter': 'robert-call', 'weight': 496224, 'rshares': '1421936316043', 'percent': 10000, 'reputation': '1773947007427', 'time': '2017-08-15T01:57:42'}
{'voter': 'mrpomidor', 'weight': 6170, 'rshares': 480506354, 'percent': 10000, 'reputation': 453045280, 'time': '2017-08-14T23:53:06'}
{'voter': 'greenstar', 'weight': 115, 'rshares': 964375303, 'percent': 100, 'reputation': '586289741941', 'time': '2017-08-15T08:11:39'}
{'voter': 'mrwalt', 'weight': 138342, 'rshares': '1160496752034', 'percent': 10000, 'reputation': '7849054503534', 'time': '2017-08-15T05:10:42'}
{'voter': 'opinizeunltd', 'weight': 3357, 'rshares': '8172742054', 'percent': 5000, 'reputation': '583844691940', 'time': '2017-08-15T00:10:51'}
{'voter': 'stackin', 'weight': 53442, 'rshares': '112076207194', 'percent': 1500, 'reputation': '15718283072410', 'time': '2017-08-15T00:16:48'}
{'voter': 'mrviquez', 'weight': 46684, 'rshares': '97902363321', 'percent': 10000, 'reputation': '29905674656172', 'time': '2017-08-15T00:29:15'}
{'voter': 'sash-pacino', 'weight': 11204, 'rshares': '23496212227', 'percent': 10000, 'reputation': '1854243555429', 'time': '2017-08-15T00:30:24'}
{'voter': 'jjjjosue', 'weight': 1694, 'rshares': '14205042242', 'percent': 10000, 'reputation': '751162025064', 'time': '2017-08-15T03:14:15'}
{'voter': 'donquipex', 'weight': 80, 'rshares': 167836102, 'percent': 10000, 'reputation': '10819538279', 'time': '2017-08-15T00:26:18'}
{'voter': 'danyelk', 'weight': 1612, 'rshares': '13524225310', 'percent': 3000, 'reputation': '1299569256083', 'time': '2017-08-15T07:30:39'}
{'voter': 'jaquith', 'weight': 533, 'rshares': 2237008083, 'percent': 10000, 'reputation': '9700600519', 'time': '2017-08-15T02:02:54'}
{'voter': 'voyceatlas', 'weight': 887, 'rshares': 1858774136, 'percent': 10000, 'reputation': '340658000616', 'time': '2017-08-15T00:42:24'}
{'voter': 'luxurious', 'weight': 2045, 'rshares': 4288669593, 'percent': 10000, 'reputation': '1055752392064', 'time': '2017-08-15T00:54:03'}
{'voter': 'kevbot', 'weight': 4719, 'rshares': '9896318106', 'percent': 2100, 'reputation': '192981178142', 'time': '2017-08-15T00:39:42'}
{'voter': 'rest100', 'weight': 3862, 'rshares': '32396671737', 'percent': 10000, 'reputation': '8152242737961', 'time': '2017-08-15T05:31:09'}
{'voter': 'defjukie', 'weight': 1975, 'rshares': '8283599683', 'percent': 10000, 'reputation': '1239513945283', 'time': '2017-08-15T03:04:06'}
{'voter': 'conditionedminds', 'weight': 528, 'rshares': 2214017543, 'percent': 10000, 'reputation': '171978937174', 'time': '2017-08-15T02:31:54'}
{'voter': 'steemmeupscotty', 'weight': 45, 'rshares': 370969834, 'percent': 100, 'reputation': '646734557915', 'time': '2017-08-15T08:11:42'}
{'voter': 'alexandruionescu', 'weight': 14, 'rshares': 123482082, 'percent': 750, 'reputation': '169047686278', 'time': '2017-08-15T07:17:48'}
{'voter': 'better-life-tips', 'weight': 211, 'rshares': 440937121, 'percent': 10000, 'reputation': '1147539432364', 'time': '2017-08-15T01:53:30'}
{'voter': 'agcoeficiente10', 'weight': 95, 'rshares': 797880647, 'percent': 10000, 'reputation': '153132881979', 'time': '2017-08-15T03:37:33'}
{'voter': 'younitedstates', 'weight': 209, 'rshares': 439859200, 'percent': 10000, 'reputation': 2694118941, 'time': '2017-08-15T01:31:21'}
{'voter': 'kiwicanfly', 'weight': 84, 'rshares': 349186602, 'percent': 10000, 'reputation': '11062448993', 'time': '2017-08-15T02:41:03'}
{'voter': 'azievzhan', 'weight': 3582, 'rshares': 548275200, 'percent': 10000, 'reputation': '4999299143', 'time': '2017-08-14T23:56:39'}
{'voter': 'buildawhale', 'weight': 40122, 'rshares': '336568471640', 'percent': 4000, 'reputation': '625477262286', 'time': '2017-08-15T08:07:39'}
{'voter': 'tonygreene113', 'weight': 30, 'rshares': 249538335, 'percent': 10000, 'reputation': '9739016029', 'time': '2017-08-15T05:04:36'}
{'voter': 'yosecc', 'weight': 68, 'rshares': 568714968, 'percent': 10000, 'reputation': 1053271805, 'time': '2017-08-15T08:38:51'}
You have new mail in /var/mail/schemelab
schemelab@metta:~/prg/vivacoin/steem-voting/src/etc$
'''
