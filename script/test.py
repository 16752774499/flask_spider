# # # from datetime import date
# # #
# # # from sqlalchemy import create_engine, func
# # # from sqlalchemy import create_engine
# # # from sqlalchemy.orm import sessionmaker
# # # from models.jobs import Jobs
# # # import config
# # #
# # # DATABOSS: dict = {
# # #     "page_1": {
# # #         "dom_1": [
# # #             "高性能计算研发工程师（OD）",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-30K·14薪",
# # #             "经验不限",
# # #             "本科",
# # #             "华为",
# # #             "https://www.zhipin.com/gongsi/02cd05cce753437e33V50w~~.html",
# # #             "不需要融资",
# # #             "10000人以上",
# # #             "高性能计算研发工程师（OD）\n西安·雁塔区·高新软件园\n15-30K·14薪\n经验不限\n本科\n余女士HR",
# # #             "https://www.zhipin.com/job_detail/374f22b12d22b2461HVz09q_ElBU.html?lid=8WME50j5ZHB.search.1&securityId=-P4OyUKx1KYBp-e1IMLmfCFGBk12CNyVg9TADSe7IlpUzdHnH_3uo8WT4R8A-dtr-v-70CfoZAxWs7ra-FfcLC8YBMjxg_t6qDCQDaBlWgyBy3I~&sessionId="
# # #         ],
# # #         "dom_10": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·玫瑰大楼",
# # #             "8-13K",
# # #             "5-10年",
# # #             "本科",
# # #             "陕西源天科技",
# # #             "https://www.zhipin.com/gongsi/10a8fc8d5d458a270ndz3tq5.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "Java开发工程师\n西安·雁塔区·玫瑰大楼\n8-13K\n5-10年\n本科\n赵女士人力资源总监",
# # #             "https://www.zhipin.com/job_detail/087b90ef93d57c8603V42t2_FVI~.html?lid=8WME50j5ZHB.search.10&securityId=vtHBAdeXgADnW-n1WFPdNIRepyEgENHkveNazaCQaMffuBPNVTpv6Qd5FRpAn9vf4PQ4KPpFL83jIm0CPfRf_zcxzotdFFntzfzD7eDRePYXliI~&sessionId="
# # #         ],
# # #         "dom_11": [
# # #             "云计算开发工程师",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-16K",
# # #             "1-3年",
# # #             "本科",
# # #             "华为技术有限公司",
# # #             "https://www.zhipin.com/gongsi/21124e51a5ea83a80nR80ti8.html",
# # #             "不需要融资",
# # #             "10000人以上",
# # #             "云计算开发工程师\n西安·雁塔区·高新软件园\n15-16K\n1-3年\n本科\n马先生研发工程师",
# # #             "https://www.zhipin.com/job_detail/8592eafe204435071Xd83dW6EFNX.html?lid=8WME50j5ZHB.search.11&securityId=90KJL4IxyQLW2-21tgN8xn7QBqre-V0iKksjhSEr7RfcBXI3xeuyRLqfbfhx6zd44yutWFfiVnxrUN6YJl_M0xWTe-huFUN6VzweKolMBr40uk2l&sessionId="
# # #         ],
# # #         "dom_12": [
# # #             "java中级开发工程师",
# # #             "西安·雁塔区·科技二路",
# # #             "20-40K",
# # #             "3-5年",
# # #             "本科",
# # #             "民生科技",
# # #             "https://www.zhipin.com/gongsi/204f0cb13397709a1XBz0t64Eg~~.html",
# # #             "不需要融资",
# # #             "1000-9999人",
# # #             "java中级开发工程师\n西安·雁塔区·科技二路\n20-40K\n3-5年\n本科\n司先生前端开发",
# # #             "https://www.zhipin.com/job_detail/ddce564a2000a73a1XN43dm1E1VT.html?lid=8WME50j5ZHB.search.12&securityId=_s28z9fdFWdP1-31ylktM9hqtTWNFmseev3RwqEFDNqPrkaTNNBPSW2ij0cjXOIO__IGDyoy2EQvZI6Sd6dhzULLQhrjcogKYGN3ZUO007OC5Ir4NQ~~&sessionId="
# # #         ],
# # #         "dom_13": [
# # #             "JAVA开发工程师",
# # #             "西安·雁塔区·丈八",
# # #             "6-12K",
# # #             "3-5年",
# # #             "本科",
# # #             "流程服务专家",
# # #             "https://www.zhipin.com/gongsi/21836247c75688491XF_396_Eg~~.html",
# # #             "不需要融资",
# # #             "20-99人",
# # #             "JAVA开发工程师\n西安·雁塔区·丈八\n6-12K\n3-5年\n本科\n潘先生招聘者",
# # #             "https://www.zhipin.com/job_detail/d4d38fcbfb92fb491XF6292_GFE~.html?lid=8WME50j5ZHB.search.13&securityId=Yeum-BXHcL9Uk-710BBcqmMiiNNdwO5NNW1T-Z3-Hoj12uXNowmt32QFOn37zjiAVn9MegVWVQP_KzTAMEV5dPGzZ4sI-60kBfO2ekyY7hIsenoY&sessionId="
# # #         ],
# # #         "dom_14": [
# # #             "信创研发工程师(J11828)",
# # #             "西安·未央区·北辰大道",
# # #             "15-25K",
# # #             "5-10年",
# # #             "本科",
# # #             "联通西部创新研究院",
# # #             "https://www.zhipin.com/gongsi/9a18b5b4d48da7831XVz2Ny1FlQ~.html",
# # #             "100-499人",
# # #             "NULL",
# # #             "信创研发工程师(J11828)\n西安·未央区·北辰大道\n15-25K\n5-10年\n本科\n吴女士HR",
# # #             "https://www.zhipin.com/job_detail/c93b31e528ed70591Hd53Ny4E1tX.html?lid=8WME50j5ZHB.search.14&securityId=mXaa1YjQo3gQn-g1LWaW1AcySb86l8bvCz8aLePLIMnjCZZ9uzLY56xcED4qo8jaMrhMDkEggOrvIf5M06avtQIyq_Z5btd4MtJ8nf2h2RBj_b1s6GhR&sessionId="
# # #         ],
# # #         "dom_15": [
# # #             "Java高级工程师",
# # #             "西安·雁塔区·小寨",
# # #             "12-16K·14薪",
# # #             "3-5年",
# # #             "本科",
# # #             "文都教育",
# # #             "https://www.zhipin.com/gongsi/94eb615af8c144391X1929o~.html",
# # #             "已上市",
# # #             "1000-9999人",
# # #             "Java高级工程师\n西安·雁塔区·小寨\n12-16K·14薪\n3-5年\n本科\n肖先生技术总监",
# # #             "https://www.zhipin.com/job_detail/bcb6d06abfd31cf233Z52tS-EVY~.html?lid=8WME50j5ZHB.search.15&securityId=IR-oOUZbN9-hA-616vVOH7vbvk74js_vBmkhJDnQy6q-vb2XcpaBep61Ul26N1uAXRE_G378sQWkfB662mJqXzhiQHWxqcLvjoSwuprIuA~~&sessionId="
# # #         ],
# # #         "dom_16": [
# # #             "软件开发",
# # #             "西安",
# # #             "13-26K",
# # #             "经验不限",
# # #             "本科",
# # #             "华为终端有限公司",
# # #             "https://www.zhipin.com/gongsi/1fcb005b2df3d7d303J73dW4Ew~~.html",
# # #             "不需要融资",
# # #             "10000人以上",
# # #             "软件开发\n西安\n13-26K\n经验不限\n本科\n朱先生hr",
# # #             "https://www.zhipin.com/job_detail/f90304fd196a3cb81Hd53tS-ElVY.html?lid=8WME50j5ZHB.search.16&securityId=w97C-pUuMebi8-y1G83Sb6M6rqaQW7J-VDnHG9nGAkbs_YM_TVqVnwkMYOc655GGdeaBNjvxiYMyjEU5wy5blWZYDdvp6uc7NGKHpAeiZt2ZioQ5xoU~&sessionId="
# # #         ],
# # #         "dom_17": [
# # #             "初级Java开发工程师",
# # #             "西安·长安区·韦曲",
# # #             "7-9K·14薪",
# # #             "1-3年",
# # #             "本科",
# # #             "中科天塔",
# # #             "https://www.zhipin.com/gongsi/84167d05569616491HB40ty4Fw~~.html",
# # #             "未融资",
# # #             "",
# # #             "初级Java开发工程师\n西安·长安区·韦曲\n7-9K·14薪\n1-3年\n本科\n韩女士HR",
# # #             "https://www.zhipin.com/job_detail/d4bff858ae72aa071HBz3dq1EVBR.html?lid=8WME50j5ZHB.search.17&securityId=RA0JOb2FoXxxt-21UQwd-2wLkaxInG_bqSmC_3wTvuMku9Qs8Gm5ZfyNcFqqUBUG0ipMm0UgOcHUekLcQl0cPcOkURX5WjgWvdekqX62iJ8RxA5h9g~~&sessionId="
# # #         ],
# # #         "dom_18": [
# # #             "游戏服务端工程师",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-20K",
# # #             "3-5年",
# # #             "本科",
# # #             "民安信西安分公司",
# # #             "https://www.zhipin.com/gongsi/69620a9dd7ad77ae1XR80920GVI~.html",
# # #             "未融资",
# # #             "100-499人",
# # #             "游戏服务端工程师\n西安·雁塔区·高新软件园\n15-20K\n3-5年\n本科\n张女士总经理助理",
# # #             "https://www.zhipin.com/job_detail/de4deaf18733f4a41HZ50929EFVQ.html?lid=8WME50j5ZHB.search.18&securityId=vpb3RUqfWscI9-f1DBvVTUcUb5Pax6i_kCOQW49G67F7pEke2Ijbc5-rJcHrEqv5SWThTW6-f-zuZ7iU5cEJOJxCttEQDovs1oQ9qP7tt8r5m0ccA6FH&sessionId="
# # #         ],
# # #         "dom_19": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·高新软件园",
# # #             "11-19K·13薪",
# # #             "1-3年",
# # #             "本科",
# # #             "研華科技",
# # #             "https://www.zhipin.com/gongsi/89aad2ff4ee566661nV609-_.html",
# # #             "未融资",
# # #             "1000-9999人",
# # #             "Java开发工程师\n西安·雁塔区·高新软件园\n11-19K·13薪\n1-3年\n本科\n李女士HR",
# # #             "https://www.zhipin.com/job_detail/01a36f283f6815b61XV52dm6GVRU.html?lid=8WME50j5ZHB.search.19&securityId=srST_lhn126F4-q1xNtB2tyQ0zDykGiUk5eSmtwo0JpVc8ObZk663onDFnQsVDYItEcDhxuLV3A9mEZ9l0DxMPnxor8sMTXIot0vYpRdoKpkkn1V&sessionId="
# # #         ],
# # #         "dom_2": [
# # #             "Java开发工程师",
# # #             "西安·灞桥区·矿山路",
# # #             "15-16K",
# # #             "5-10年",
# # #             "本科",
# # #             "卓软智慧",
# # #             "https://www.zhipin.com/gongsi/f5cb4d98e5e889f01Xx83920FFE~.html",
# # #             "0-20人",
# # #             "NULL",
# # #             "Java开发工程师\n西安·灞桥区·矿山路\n15-16K\n5-10年\n本科\n郭先生人事主管",
# # #             "https://www.zhipin.com/job_detail/6d7d1f43a31b8d2a1X1_3Ni9E1VW.html?lid=8WME50j5ZHB.search.2&securityId=qfULSIDp26yKV-V1NrNTN5VufEJtywAp5ziH0cm6XupYasRKDfTJbxhvbBomnCRxea8X9jbKSXgXIHmtNzQqD0fYfFgQ9pbMIz0rnTZCDInW4L9y9js~&sessionId="
# # #         ],
# # #         "dom_20": [
# # #             "Java软件工程师",
# # #             "西安·雁塔区·高新路",
# # #             "6-12K",
# # #             "1年以内",
# # #             "本科",
# # #             "西安雁兆隆计算机",
# # #             "https://www.zhipin.com/gongsi/4cfc6a4f9a6fbfd61HN73tq9.html",
# # #             "未融资",
# # #             "100-499人",
# # #             "Java软件工程师\n西安·雁塔区·高新路\n6-12K\n1年以内\n本科\n樊女士就业老师",
# # #             "https://www.zhipin.com/job_detail/59f8c8813fcc42aa1n1z2NS5EFc~.html?lid=8WME50j5ZHB.search.20&securityId=HHHwdEqjntCZH-214W1oNPfBCHCXUmyCNOA5Cqjo0s05KEgQ4i9FBGDgqL1mBqfZ8RQdmNG_ocxlA-JdRLmSS5KgfyhO0ZiL23rmTVNxtZSHpJs~&sessionId="
# # #         ],
# # #         "dom_21": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·高新软件园",
# # #             "7-12K",
# # #             "3-5年",
# # #             "大专",
# # #             "大宽物联",
# # #             "https://www.zhipin.com/gongsi/88ee1b5a73a83e820Hd63tq4GA~~.html",
# # #             "0-20人",
# # #             "NULL",
# # #             "Java开发工程师\n西安·雁塔区·高新软件园\n7-12K\n3-5年\n大专\n陈女士公司主管",
# # #             "https://www.zhipin.com/job_detail/9622755e948fe0761XZ-29i4E1pR.html?lid=8WME50j5ZHB.search.21&securityId=KnQY2zyiurvym-o1VS6G5e3DROKlKLAZOhBRvTSYnzZqscX27ltlbXHhKN452TkYgsVtVrwfZWa0UpoJEvTWrOg4CWYCmvf0dmOoJq0k01FKmYYDdA~~&sessionId="
# # #         ],
# # #         "dom_22": [
# # #             "中级java工程师（西安中行）",
# # #             "西安·灞桥区·十里铺",
# # #             "10-15K",
# # #             "5-10年",
# # #             "本科",
# # #             "宇信科技",
# # #             "https://www.zhipin.com/gongsi/b0045d381ce69c711XZ639Q~.html",
# # #             "已上市",
# # #             "1000-9999人",
# # #             "中级java工程师（西安中行）\n西安·灞桥区·十里铺\n10-15K\n5-10年\n本科\n张女士招聘专员\n在线",
# # #             "https://www.zhipin.com/job_detail/f5ed9b92bd8e1f0b1X152Nq6GVpU.html?lid=8WME50j5ZHB.search.22&securityId=CVSZWxqnZ7Ose-X1nelNgZUaklynGUQ8SVPkqD4dUKvykrKFhEqIbBvfDLSOjspSuLJ3-qmvwI1PeLBUfNR0Id2VhWZV2R4XHdSI-obbeYeUD4rIRYQAWQClXAq-OVyd5ifCiofRdacwn_Po-ps~&sessionId="
# # #         ],
# # #         "dom_23": [
# # #             "Java",
# # #             "西安·雁塔区·紫薇田园都市",
# # #             "15-20K",
# # #             "5-10年",
# # #             "本科",
# # #             "云基智慧",
# # #             "https://www.zhipin.com/gongsi/1f3daa3c1eb1dedb33142dk~.html",
# # #             "不需要融资",
# # #             "1000-9999人",
# # #             "Java\n西安·雁塔区·紫薇田园都市\n15-20K\n5-10年\n本科\n夏先生软件开发",
# # #             "https://www.zhipin.com/job_detail/2f7dafb020c3334b0X1609q0EFc~.html?lid=8WME50j5ZHB.search.23&securityId=Ib5ldW8hACShC-w14jN2WRNAGObGw8HEpaZ7ohMaiUNcVTjhjQ41q7MnMrySHsnwe7VYlIItIb1yPYdphE3tZsyBd_u7mdnvFspWQT2h-xHlxg~~&sessionId="
# # #         ],
# # #         "dom_24": [
# # #             "后端开发工程师",
# # #             "西安",
# # #             "10-15K",
# # #             "3-5年",
# # #             "硕士",
# # #             "科达自控",
# # #             "https://www.zhipin.com/gongsi/0c2ad7c106b7f15e1nd939W5EVU~.html",
# # #             "已上市",
# # #             "100-499人",
# # #             "后端开发工程师\n西安\n10-15K\n3-5年\n硕士\n渠女士人事经理",
# # #             "https://www.zhipin.com/job_detail/1a8e4035f5fecc781X153dm9E1VZ.html?lid=8WME50j5ZHB.search.24&securityId=z29MnfIqct94L-W1ShWkpZrloYVsEY0IH4ChLKx5mxVRayB4D8CGFzYdOKxD8t2lfZB8hn8PQvb1PiXEOEEcY-JSp7P6CZWjONZVn8HH3xUGlRJj-zct&sessionId="
# # #         ],
# # #         "dom_25": [
# # #             "Java开发工程师",
# # #             "西安·长安区·航天城",
# # #             "1-4K",
# # #             "1年以内",
# # #             "本科",
# # #             "华西云",
# # #             "https://www.zhipin.com/gongsi/c0cd2fe508024b0833N63d64Fw~~.html",
# # #             "天使轮",
# # #             "0-20人",
# # #             "Java开发工程师\n西安·长安区·航天城\n1-4K\n1年以内\n本科\n邹先生HR\n在线",
# # #             "https://www.zhipin.com/job_detail/5de108272d7806861Xd639W6GFRR.html?lid=8WME50j5ZHB.search.25&securityId=gxyWJJDes7dkw-21XvAz08LAMDLOUK9uRGuY2Z6frvrYz-wHWp2oqF-7Bvk5wMHgIWK8BWaB04mu7GY2xkUYFfTL4W7NyODsja0Hd6ky3tS0_m_0-QT8DEhKipG1mWJnvEpRqrQYaPiZSIoOrpOElA~~&sessionId="
# # #         ],
# # #         "dom_26": [
# # #             "java中级开发工程师",
# # #             "西安·雁塔区·沣惠南路",
# # #             "9-14K",
# # #             "3-5年",
# # #             "本科",
# # #             "天维信息",
# # #             "https://www.zhipin.com/gongsi/bf7b445ce3da011a3nZ52NW_.html",
# # #             "已上市",
# # #             "500-999人",
# # #             "java中级开发工程师\n西安·雁塔区·沣惠南路\n9-14K\n3-5年\n本科\n赵女士HR",
# # #             "https://www.zhipin.com/job_detail/5ffa0b5907c4d2fb1HB829S6GVZZ.html?lid=8WME50j5ZHB.search.26&securityId=_0nSmON2ycVYa-J1-Ge4FTrhOyoxCyP_ooHIci8moBNFMxZXYTrJaMabzJ9z8Fc22GCBeJlRcnJG7liRM8pkqBKiKPN0tK7XPCbYm_95OBHINbBd&sessionId="
# # #         ],
# # #         "dom_27": [
# # #             "java架构师",
# # #             "西安·未央区·三桥",
# # #             "15-22K",
# # #             "5-10年",
# # #             "本科",
# # #             "航轮远智能科技",
# # #             "https://www.zhipin.com/gongsi/64184266ef7031e31HRy3dW8FFI~.html",
# # #             "不需要融资",
# # #             "20-99人",
# # #             "java架构师\n西安·未央区·三桥\n15-22K\n5-10年\n本科\n王女士人事主管",
# # #             "https://www.zhipin.com/job_detail/75ec79dd1ea98af01HV_2tS1GFpZ.html?lid=8WME50j5ZHB.search.27&securityId=oltg8ZKgAvHSt-Y1XzBjGkiO2aEfVthnKGEauQ8Sp_N-120f4wpbM6GkDFU7ol1r3Iyl8tKG4gwZbOUF55Ma4xU5MDie-StRoiv6mLxvrw3y7ElFZKpe&sessionId="
# # #         ],
# # #         "dom_28": [
# # #             "高级后端工程师",
# # #             "西安·雁塔区·长安路",
# # #             "6-10K",
# # #             "1-3年",
# # #             "本科",
# # #             "艾克森",
# # #             "https://www.zhipin.com/gongsi/748dbc2934955fae1HB609y-ElU~.html",
# # #             "20-99人",
# # #             "NULL",
# # #             "高级后端工程师\n西安·雁塔区·长安路\n6-10K\n1-3年\n本科\n曹女士人事专员",
# # #             "https://www.zhipin.com/job_detail/74cac1167458c9921HBz2dm4ElRZ.html?lid=8WME50j5ZHB.search.28&securityId=WfUlxMQwjPpZ0-P1cNvKfvJ9Why4MCbBfm5rmvEZjn10VWS2SIXqdu_VzR9BbSfhaIzbrkqdBcvK_bmMbpKd7pLqVy2sj6lR61cJHuH-dHPeRzf-vO8P&sessionId="
# # #         ],
# # #         "dom_29": [
# # #             "Java开发（银行驻场，双休，餐补）",
# # #             "西安·雁塔区·高新软件园",
# # #             "12-14K",
# # #             "3-5年",
# # #             "本科",
# # #             "信雅达科技股份",
# # #             "https://www.zhipin.com/gongsi/57516d195c7b21a21nd92dq0E1Q~.html",
# # #             "已上市",
# # #             "1000-9999人",
# # #             "Java开发（银行驻场，双休，餐补）\n西安·雁塔区·高新软件园\n12-14K\n3-5年\n本科\n钱女士招聘顾问",
# # #             "https://www.zhipin.com/job_detail/309aef3c47716f821Xd-39i4GFdT.html?lid=8WME50j5ZHB.search.29&securityId=QMwmwYSzkGMte-21DLakugfzjgN8SX8HLoJUwUtidfwRFhrlJPwZ3vrVBTi-55hmayjPhAEoHtWMh_MEChiPP1042aEPmOf3QS12dVmb216o5m38dFc~&sessionId="
# # #         ],
# # #         "dom_3": [
# # #             "Java",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-30K",
# # #             "3-5年",
# # #             "本科",
# # #             "西安华为",
# # #             "https://www.zhipin.com/gongsi/d6210a32fe10b00e1XV_2N-6.html",
# # #             "未融资",
# # #             "10000人以上",
# # #             "Java\n西安·雁塔区·高新软件园\n15-30K\n3-5年\n本科\n申先生HR",
# # #             "https://www.zhipin.com/job_detail/8e5d2510d80584ca1nd63Ny4ElVQ.html?lid=8WME50j5ZHB.search.3&securityId=EnL7ioNu9EgYR-s1g9iSU0atYizu3dmmC8pGuCVVlqXGwnCmTV_RMTusQw4-s8LQw7rxJ1wGCZRBYEZsKe8lTWKWg8Oqu_NcMyKQbkigMPDvAFvC&sessionId="
# # #         ],
# # #         "dom_30": [
# # #             "Java 中级工程师",
# # #             "西安·雁塔区·绿地世纪城",
# # #             "9-13K",
# # #             "3-5年",
# # #             "学历不限",
# # #             "创想信达",
# # #             "https://www.zhipin.com/gongsi/ba1367d7dfe2ce8b1nB_3Nq1GFo~.html",
# # #             "0-20人",
# # #             "NULL",
# # #             "Java 中级工程师\n西安·雁塔区·绿地世纪城\n9-13K\n3-5年\n学历不限\n张先生主管",
# # #             "https://www.zhipin.com/job_detail/366dfb2a6ac415481nJ-3t2-GVVZ.html?lid=8WME50j5ZHB.search.30&securityId=jQPoA4N50mCBc-m13Ob4nwPugN7h4GQW4wyXYTSuMYUCLu0ApoZZjS5-NGSpZ0wKN25r2kUh_UEb2uM6X_kc6zL18JSCh9CT98Ey25HuDYwI7sb67iuG&sessionId="
# # #         ],
# # #         "dom_4": [
# # #             "Java开发工程师",
# # #             "西安·长安区·航天城",
# # #             "15-30K",
# # #             "3-5年",
# # #             "本科",
# # #             "几何数字",
# # #             "https://www.zhipin.com/gongsi/393c9d7e307bb3aa1nR939y0GQ~~.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "Java开发工程师\n西安·长安区·航天城\n15-30K\n3-5年\n本科\n郭女士HR\n在线",
# # #             "https://www.zhipin.com/job_detail/5ac5b2156e7dc1c21XF63du8ElNX.html?lid=8WME50j5ZHB.search.4&securityId=r2xSUiHXt34zU-R1tU84nJkNSrarrOZVwPdrHQFpblWO1utcnJ5KB_tsVHf7Go84Tk2JQBCI-Na5qzEnM74agFZMx9QjSlhDdxsnGSMrnzDIEbmxXD1DSIMUVpo2o-Nl5b5XWPr--Tuq7tiwoMuMtg~~&sessionId="
# # #         ],
# # #         "dom_5": [
# # #             "Java研发工程师",
# # #             "西安·未央区·龙首村",
# # #             "8-12K",
# # #             "3-5年",
# # #             "本科",
# # #             "北大软件",
# # #             "https://www.zhipin.com/gongsi/ee6abeef0127dc520XFy3tW4.html",
# # #             "不需要融资",
# # #             "1000-9999人",
# # #             "Java研发工程师\n西安·未央区·龙首村\n8-12K\n3-5年\n本科\n宛女士区域组长",
# # #             "https://www.zhipin.com/job_detail/7c504a47370261ef1nJ72dy8FVpW.html?lid=8WME50j5ZHB.search.5&securityId=gL1MUH5bEP665-z1-ufTH4CNEsQeeoevJQgoCZUwaUnpbRlXMKsSS5eTds7k7Xf9VpC8rZo1szus9723qARihvJkM7aOc9gGvd4CPhMl2YbU0ixXCA~~&sessionId="
# # #         ],
# # #         "dom_6": [
# # #             "java开发工程师",
# # #             "西安",
# # #             "14-25K",
# # #             "3-5年",
# # #             "本科",
# # #             "华为云",
# # #             "https://www.zhipin.com/gongsi/f78cf3c8ff0eae761nV42NW9FFo~.html",
# # #             "不需要融资",
# # #             "10000人以上",
# # #             "java开发工程师\n西安\n14-25K\n3-5年\n本科\n刘女士招聘专员",
# # #             "https://www.zhipin.com/job_detail/105fd784afba96241XB62tm0F1pT.html?lid=8WME50j5ZHB.search.6&securityId=c939mwWg9o3og-K1IsHY5s-3UEACIRcRTdJLo0weakhMTn5lSOlEXzIu1mHbkHgYI1G1TSHia5V8RMcLsHF1soF-V4b1FzP_9oISzScLDWkt6ctJTVTU&sessionId="
# # #         ],
# # #         "dom_7": [
# # #             "软件工程师",
# # #             "西安",
# # #             "10-15K",
# # #             "5-10年",
# # #             "硕士",
# # #             "路客文化",
# # #             "https://www.zhipin.com/gongsi/fa77658d0117d1eb1nF53tS4GQ~~.html",
# # #             "不需要融资",
# # #             "20-99人",
# # #             "软件工程师\n西安\n10-15K\n5-10年\n硕士\n吴女士设计师",
# # #             "https://www.zhipin.com/job_detail/73a220cc1628dc471XV93dq_EFI~.html?lid=8WME50j5ZHB.search.7&securityId=UxBYwPPL1Cr7K-41iet3LMlIPlYC7gXls7hhriwlZWNaUngwKoB03JRPfumqyO1-7797tYAbBCBMNPk6xAU38GFBgbbxKc7MGbUslLMg6qnKbpGl&sessionId="
# # #         ],
# # #         "dom_8": [
# # #             "Java",
# # #             "西安·雁塔区·沣惠南路",
# # #             "10-15K·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "北笙科技",
# # #             "https://www.zhipin.com/gongsi/d18e42eb9992b3c01XN62d-9EFM~.html",
# # #             "未融资",
# # #             "0-20人",
# # #             "Java\n西安·雁塔区·沣惠南路\n10-15K·13薪\n3-5年\n本科\n王先生技术总监",
# # #             "https://www.zhipin.com/job_detail/10dc9ecfd2ffeee31HV43tq6FFFU.html?lid=8WME50j5ZHB.search.8&securityId=VAqLW93q0FFbu-F1OqAEYC6V6EBgxvPfG6O_zCE_qnRnxMBdDtkNIXS3vpMi6QBGDweEuu-bab1St2d1ZnVP93PFwKYxm3pZMk7t7gX9zDsqVOOCouw~&sessionId="
# # #         ],
# # #         "dom_9": [
# # #             "Java工程师",
# # #             "西安·雁塔区·高新路",
# # #             "9-10K",
# # #             "5-10年",
# # #             "本科",
# # #             "迈思途软件",
# # #             "https://www.zhipin.com/gongsi/d54b7188846c3c471nB42Nm5ElE~.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "Java工程师\n西安·雁塔区·高新路\n9-10K\n5-10年\n本科\n张女士综合部经理\n在线",
# # #             "https://www.zhipin.com/job_detail/02b32dfbfa9fee4a1XF70tm1EVpW.html?lid=8WME50j5ZHB.search.9&securityId=lddQ6v-sKG6ev-31CZAUiVUwrLHg6rqvtKUOCdQFQq4Ar2QP6dEJDlFkwYegVKHw3Yy6rG_PNcYVffkEgP2j7OluOAG1wmy6uZ6xLubpxpLUYf2XsJf-cwqgwfcWIQcyTigdyzJKDWO6mdaOjY0KN69I&sessionId="
# # #         ]
# # #     },
# # #     "page_2": {
# # #         "dom_1": [
# # #             "开发工程师",
# # #             "西安·雁塔区·枫林绿洲",
# # #             "12-24K·14薪",
# # #             "1年以内",
# # #             "本科",
# # #             "腾讯云",
# # #             "https://www.zhipin.com/gongsi/e0f635e27a94e2c90HFz09u1EA~~.html",
# # #             "已上市",
# # #             "1000-9999人",
# # #             "开发工程师\n西安·雁塔区·枫林绿洲\n12-24K·14薪\n1年以内\n本科\n王先生后端开发\n在线",
# # #             "https://www.zhipin.com/job_detail/16136a9aa01e82711HR809S9GFVR.html?lid=8WME50j5ZHB.search.31&securityId=4SLPbiHJW0xLL-W1As4zTSv3OqGqcBJiUz8YIEhZ_FQZlHDpDoV891T1iCOajC-avyIwCI6z1-WXWJFr36l4ixa50rfbDQvhJ_9J036cKJCirBcZzjGBbeJGxHAL29hQmKweScEAovkc0nF-HgiWkA~~&sessionId="
# # #         ],
# # #         "dom_10": [
# # #             "webgis开发工程师",
# # #             "西安",
# # #             "8-10K",
# # #             "1-3年",
# # #             "本科",
# # #             "北京特里尼斯",
# # #             "https://www.zhipin.com/gongsi/6c7c30d4703d92181Xd539u4.html",
# # #             "不需要融资",
# # #             "100-499人",
# # #             "webgis开发工程师\n西安\n8-10K\n1-3年\n本科\n马先生技术总监",
# # #             "https://www.zhipin.com/job_detail/338b263ed687c5a41nRz29i0FlA~.html?lid=8WME50j5ZHB.search.40&securityId=LpS8SAcrD90IG-a1hbclFzQKBTi-EQs4wf-lYHUgVUso7o_u17ggTTO_WAFJMkxQfE63GqaLouWLYpiQ8nnYyMydfp0G8Mc2WNQwHX5wLBpn4p8~&sessionId="
# # #         ],
# # #         "dom_11": [
# # #             "高级java开发",
# # #             "西安",
# # #             "15-30K",
# # #             "5-10年",
# # #             "本科",
# # #             "隆基绿能科技",
# # #             "https://www.zhipin.com/gongsi/6486569b54f521b01nNy3t68FVQ~.html",
# # #             "10000人以上",
# # #             "NULL",
# # #             "高级java开发\n西安\n15-30K\n5-10年\n本科\n杨先生计划订单物流组IT负责人",
# # #             "https://www.zhipin.com/job_detail/2dc21f7c6d470f051Xx509u5E1FX.html?lid=8WME50j5ZHB.search.41&securityId=EPHox1rfwGiR9-R1cPfLZYLW0-RYfKlr_vU0AduLmXYFuxUNrscidPU8QHNxxFI8rLwtTYR7ivoIygz_l9Qs2d_r3of1q8E0pJ4nbre4p8ORzU7MUbbO&sessionId="
# # #         ],
# # #         "dom_12": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·紫薇田园都市",
# # #             "11-18K",
# # #             "3-5年",
# # #             "本科",
# # #             "三维天地",
# # #             "https://www.zhipin.com/gongsi/d2b3b58e76f18a720nN709-6.html",
# # #             "不需要融资",
# # #             "1000-9999人",
# # #             "Java开发工程师\n西安·雁塔区·紫薇田园都市\n11-18K\n3-5年\n本科\n王女士招聘主管",
# # #             "https://www.zhipin.com/job_detail/5cfc9f2108374a8c1nB-2Ni6EldV.html?lid=8WME50j5ZHB.search.42&securityId=Yq8vIxZNUcmkg-X1DYqI_IgdfU6B6rhKiogwsV6VaqbCLuKOys8TpffZSCg7AHtk6mh1GQyeGjtj4OyRNLEKQTOLCRcVWPADpTxqd3IOCzQ6qjOn&sessionId="
# # #         ],
# # #         "dom_13": [
# # #             "后端开发工程师",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-20K·15薪",
# # #             "经验不限",
# # #             "本科",
# # #             "中移系统集成有限公司",
# # #             "https://www.zhipin.com/gongsi/4bfd55aa0d45aaca1nZ60t66FFI~.html",
# # #             "未融资",
# # #             "1000-9999人",
# # #             "后端开发工程师\n西安·雁塔区·高新软件园\n15-20K·15薪\n经验不限\n本科\n李先生项目经理",
# # #             "https://www.zhipin.com/job_detail/4fef3afbde331ac11XR63dS5GFVQ.html?lid=8WME50j5ZHB.search.43&securityId=kZciNxJfyPpKy-m1LPCXCaT2D3mzAp-hTsWceb_pFDTl8wyhaKqmxV2sPwjh3Jdqv24bMfkYlrYpS88DNYZvlRXmau6cuo2616rxFYKSzbR-Txqe_pg~&sessionId="
# # #         ],
# # #         "dom_14": [
# # #             "高级Java开发工程师",
# # #             "西安",
# # #             "30-50K",
# # #             "3-5年",
# # #             "本科",
# # #             "阿里巴巴集团",
# # #             "https://www.zhipin.com/gongsi/5d627415a46b4a750nJ9.html",
# # #             "已上市",
# # #             "10000人以上",
# # #             "高级Java开发工程师\n西安\n30-50K\n3-5年\n本科\n王先生招聘者",
# # #             "https://www.zhipin.com/job_detail/bd48cf6841e3cec00HZz0tm8FlQ~.html?lid=8WME50j5ZHB.search.44&securityId=I0rRkdvIaGtS8-H11bpwoH0ZppCHF8N7x5KCwsivDFwLAStSh71tTZKAdAW4I4jhy7yZ2o8bYxSl70voMOxzvfQqykPfgs3whn2Pz9SNCVAh&sessionId="
# # #         ],
# # #         "dom_15": [
# # #             "后端开发实习生",
# # #             "西安·碑林区·长安路",
# # #             "100-150元/天",
# # #             "5天/周",
# # #             "6个月",
# # #             "北京新华时代数据系统",
# # #             "https://www.zhipin.com/gongsi/7f9e1279bd3a66de1XFy39W1EVI~.html",
# # #             "20-99人",
# # #             "NULL",
# # #             "后端开发实习生\n西安·碑林区·长安路\n100-150元/天\n5天/周\n6个月\n本科\n穆女士HR人事",
# # #             "https://www.zhipin.com/job_detail/2864ce8d24641b811HBz3t-1FFtW.html?lid=8WME50j5ZHB.search.45&securityId=T9jHY8DSzjluk-E1h7JOJmATizKQVe-V9e8tIF1x5NyH5CSxjUHsJIvOwjPo-GGzphpFZ0SB53crtRX_rAvUw40c7OHCycpkn3Bv6e8G2wySjzuZLDE~&sessionId="
# # #         ],
# # #         "dom_16": [
# # #             "Java开发中高级【13薪+全额公积金】",
# # #             "西安·雁塔区·沣惠南路",
# # #             "11-13K·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "中软国际",
# # #             "https://www.zhipin.com/gongsi/2d208a8834e4a58203d43Q~~.html",
# # #             "已上市",
# # #             "10000人以上",
# # #             "Java开发中高级【13薪+全额公积金】\n西安·雁塔区·沣惠南路\n11-13K·13薪\n3-5年\n本科\n姚女士招聘专员\n在线",
# # #             "https://www.zhipin.com/job_detail/2fab57ec4cf0d0571HJ40t-1EFtZ.html?lid=8WME50j5ZHB.search.46&securityId=9mK07AVtTHRRg-U19yaTVzHy_gX5xgqRynnGYY7xKujJsDNqsuLYfLKpsr3Y9yckg6emDCFhA9Gh_mAURYzptEV7z-eesantDQjOjzSnEMpg_n6i3AbsCteMOYadV_MFvqTtSiPzHDdjH0kV5Q~~&sessionId="
# # #         ],
# # #         "dom_17": [
# # #             "高级java开发",
# # #             "西安·雁塔区·沣惠南路",
# # #             "12-23K·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "陕西联筑科技有限公司",
# # #             "https://www.zhipin.com/gongsi/5a4b2d1b5d8830db1HV80t-6FFU~.html",
# # #             "不需要融资",
# # #             "0-20人",
# # #             "高级java开发\n西安·雁塔区·沣惠南路\n12-23K·13薪\n3-5年\n本科\n胡先生招聘",
# # #             "https://www.zhipin.com/job_detail/382ef0e956c2522c1HB_3Nu8FlRS.html?lid=8WME50j5ZHB.search.47&securityId=9pVoAP4VbPLeQ-71Dj8KZZRvzabsuppJraRzdoV55WLijQK6QJIwvLuIBZGdX0tDUfJE-IsvFO-LJoscOQrDyYkDWKlkj1XD3JlQSdE_evvY7EZ8t_U~&sessionId="
# # #         ],
# # #         "dom_18": [
# # #             "Java",
# # #             "西安·雁塔区·电子城",
# # #             "10-15K",
# # #             "3-5年",
# # #             "大专",
# # #             "盛元广通科技",
# # #             "https://www.zhipin.com/gongsi/d0832b32e200a7851nd80tm1FFE~.html",
# # #             "20-99人",
# # #             "NULL",
# # #             "Java\n西安·雁塔区·电子城\n10-15K\n3-5年\n大专\n袁先生人事主管",
# # #             "https://www.zhipin.com/job_detail/a82b45ee1be926bc1XZ72dW1FVBZ.html?lid=8WME50j5ZHB.search.48&securityId=tDwIqKi2vLgq7-r1IFpnJ_Y8cZ75ARruJ0MIx2JRNG-u6V0lwuzjDhSL_hXM_aAdmkxre2kTsMoMPeBNcuxg7b_NN1KVdOYI14s5SCR7iImOvr0WDYM5&sessionId="
# # #         ],
# # #         "dom_19": [
# # #             "JAVA高级开发",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-25K·14薪",
# # #             "3-5年",
# # #             "本科",
# # #             "华为",
# # #             "https://www.zhipin.com/gongsi/02cd05cce753437e33V50w~~.html",
# # #             "不需要融资",
# # #             "10000人以上",
# # #             "JAVA高级开发\n西安·雁塔区·高新软件园\n15-25K·14薪\n3-5年\n本科\n杜先生HR",
# # #             "https://www.zhipin.com/job_detail/504f908b2fd77c1a1nV43ty8FlBU.html?lid=8WME50j5ZHB.search.49&securityId=kmBrc3tm8VCpY-Q1FhxOjRWKGOPqNRDcvFFAU5sM5QtxMzAduaVwhRd_c55UxsjYZGnLB9RPVl-2T244TkGoWUkG3BIq5PxD8oKrtdUQufkbtuo~&sessionId="
# # #         ],
# # #         "dom_2": [
# # #             "Java高级开发工程师",
# # #             "西安·雁塔区·高新路",
# # #             "15-20K·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "德智臻观数据科技",
# # #             "https://www.zhipin.com/gongsi/5c47825eb5d5b9aa0HNz0t-7FQ~~.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "Java高级开发工程师\n西安·雁塔区·高新路\n15-20K·13薪\n3-5年\n本科\n马女士行政",
# # #             "https://www.zhipin.com/job_detail/829a8390fc87dbf71nZ63tS9EVNW.html?lid=8WME50j5ZHB.search.32&securityId=b3HBG834uCKjG-r1dk5WThcwArubycg3OAnzGBLUycwDjMRF3QWdrBGa_EuQ_fc0Py620OGj67JoZrrvTJ7BjvDaPmiQCCYGez4H0WWQwBU4N_ltVQ~~&sessionId="
# # #         ],
# # #         "dom_20": [
# # #             "高级java工程师",
# # #             "西安·长安区·南大学城",
# # #             "8-10K",
# # #             "5-10年",
# # #             "大专",
# # #             "西安博奥科技",
# # #             "https://www.zhipin.com/gongsi/bdff64c958603d391X1_09g~.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "高级java工程师\n西安·长安区·南大学城\n8-10K\n5-10年\n大专\n余女士行政",
# # #             "https://www.zhipin.com/job_detail/0d717447da3125811Xxy3929E1RX.html?lid=8WME50j5ZHB.search.50&securityId=i17MRKNXyHd1f-F1bXQ0PJSdthrVYWJ0sOf1fpEMfEmTHRBQKHf_rWtVrvH9D8PXyfOf41RcfsX63mVKmBZvmlVFFAnj7mk6YHttzL1Cs1pLzmJG&sessionId="
# # #         ],
# # #         "dom_21": [
# # #             "Java高级研发实施工程师（西安）",
# # #             "西安·雁塔区·等驾坡",
# # #             "10-15K",
# # #             "5-10年",
# # #             "硕士",
# # #             "昊恩星美",
# # #             "https://www.zhipin.com/gongsi/32a24a777e952d141Hxy2tm9Fw~~.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "Java高级研发实施工程师（西安）\n西安·雁塔区·等驾坡\n10-15K\n5-10年\n硕士\n高女士HRD",
# # #             "https://www.zhipin.com/job_detail/d6bb24a63667a8df1HV-3tq0E1RX.html?lid=8WME50j5ZHB.search.51&securityId=qXrqWmrRIsjpF-21-vHVPR9-ma29BcYCnxOCFnSxWcbG_Z6eBTg9X6VC8E84xIB0ZvO7KPolYeeS9scRYohwrGxk4WnuNUimtg5yYjA9dZyt5a9iYw~~&sessionId="
# # #         ],
# # #         "dom_22": [
# # #             "java后端开发工程师",
# # #             "西安·雁塔区·高新路",
# # #             "5-6K·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "优得科技",
# # #             "https://www.zhipin.com/gongsi/2caa83a2b180dd6a1XR539-4FVo~.html",
# # #             "不需要融资",
# # #             "0-20人",
# # #             "java后端开发工程师\n西安·雁塔区·高新路\n5-6K·13薪\n3-5年\n本科\n田先生总经理",
# # #             "https://www.zhipin.com/job_detail/17f82bdced811e991XJ52Nu6E1tQ.html?lid=8WME50j5ZHB.search.52&securityId=JfwT-s64hqpVP-v1e8FJOXaDCXH4vUUg0NzIine30Hutg_4qJN5vJhAX9g7XWs4W5QdgJ0PMyyP-HA0lqpfWsMZY74Eq-aM8ZvumORiHVGjfA7E-JMdv&sessionId="
# # #         ],
# # #         "dom_23": [
# # #             "【西安】JAVA高级工程师/技术经理",
# # #             "西安·雁塔区·高新软件园",
# # #             "15-30K·14薪",
# # #             "5-10年",
# # #             "本科",
# # #             "华润股份",
# # #             "https://www.zhipin.com/gongsi/2c655d732342165c1HZ83Ny6Fg~~.html",
# # #             "不需要融资",
# # #             "10000人以上",
# # #             "【西安】JAVA高级工程师/技术经理\n西安·雁塔区·高新软件园\n15-30K·14薪\n5-10年\n本科\n陈先生招聘者",
# # #             "https://www.zhipin.com/job_detail/c1971a9c05c5c7a11XJ72d6_FlpW.html?lid=8WME50j5ZHB.search.53&securityId=-zCitWeppNP2P-w1YOOHnrINR2xQOTJf883URTIfJpB67T6GKr-Ji2gbr9ALQBNY8U32Tt_zFYcO2YshBgv-DepIrMd6wMiB-UofLfd4FKl7W9ZCLQ~~&sessionId="
# # #         ],
# # #         "dom_24": [
# # #             "java中级开发工程师",
# # #             "西安·雁塔区·紫薇田园都市",
# # #             "11-18K·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "敦煌智旅",
# # #             "https://www.zhipin.com/gongsi/3c38dd4f907456131XV539W9Eg~~.html",
# # #             "不需要融资",
# # #             "20-99人",
# # #             "java中级开发工程师\n西安·雁塔区·紫薇田园都市\n11-18K·13薪\n3-5年\n本科\n吴先生研发总监",
# # #             "https://www.zhipin.com/job_detail/080548ced9ecf7fc1nZ-2t67E1BU.html?lid=8WME50j5ZHB.search.54&securityId=xfYI2xKOq5014-r10gJ3QidZ_8gY8INhu7E03eD8M9U7Kao46zvCmA4tdOFN9X3CeSgWS5_pNE-u57bLUbrk3aNIoYmm0x4jmm6gDPw_Bw5Bv1Egpw~~&sessionId="
# # #         ],
# # #         "dom_25": [
# # #             "java高级开发工程师",
# # #             "西安·长安区·航天城",
# # #             "10-15K",
# # #             "3-5年",
# # #             "本科",
# # #             "瀚光数科",
# # #             "https://www.zhipin.com/gongsi/bb0dac0d5fd1d52d1XF43dq8EVA~.html",
# # #             "天使轮",
# # #             "0-20人",
# # #             "java高级开发工程师\n西安·长安区·航天城\n10-15K\n3-5年\n本科\n祝女士人力",
# # #             "https://www.zhipin.com/job_detail/1987c7936ec3d8f51XN639i-E1FQ.html?lid=8WME50j5ZHB.search.55&securityId=xPx4wBygLKVNs-D1Ghr_SRhaN80IwctcE_4xXdl4zl3xHD1k0cUhcMS185FuMHjjVPE-_hHY6Av5Gtnhv8d6h0k2iC-VkR0tSH118sQ7vcBjyrWdwhPB&sessionId="
# # #         ],
# # #         "dom_26": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·科技路西口",
# # #             "9-10K",
# # #             "1-3年",
# # #             "本科",
# # #             "鼎轩科技",
# # #             "https://www.zhipin.com/gongsi/292b74829644584233B50tW_.html",
# # #             "未融资",
# # #             "100-499人",
# # #             "Java开发工程师\n西安·雁塔区·科技路西口\n9-10K\n1-3年\n本科\n任先生技术经理",
# # #             "https://www.zhipin.com/job_detail/94f0091405945c9a1nZ40tm1FVFT.html?lid=8WME50j5ZHB.search.56&securityId=cP2Mt8dU47djR-V1DOaCPpwNetvtT7GoY06G0PRxE1YXqJZHpLQw6mXwi8chwmhC_rBRYsybs7FeZ0aTvIv4ftU6BkibVLGyEkasxdWVx_Q5S2sNPw~~&sessionId="
# # #         ],
# # #         "dom_27": [
# # #             "程序员",
# # #             "西安·碑林区·东大街",
# # #             "7-12K",
# # #             "3-5年",
# # #             "本科",
# # #             "西安智容道合科技",
# # #             "https://www.zhipin.com/gongsi/352490e2f2b4a2581XVz2d6_FVY~.html",
# # #             "0-20人",
# # #             "NULL",
# # #             "程序员\n西安·碑林区·东大街\n7-12K\n3-5年\n本科\n张先生招聘者",
# # #             "https://www.zhipin.com/job_detail/6a52091654e5de441HV729q7E1ZU.html?lid=8WME50j5ZHB.search.57&securityId=7iJNLLcQ1PznR-41zgjo1C6NZXX0uVdu376rw0e8a_Cgd3mz7v5-VTDzXMUx04U-fbvhasXUxFecU97ojJOFZVupl3uy4xSC4PzRtwzKzu6malLIbaU7&sessionId="
# # #         ],
# # #         "dom_28": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·科技路西口",
# # #             "18-25K·14薪",
# # #             "1-3年",
# # #             "硕士",
# # #             "中信建投证券",
# # #             "https://www.zhipin.com/gongsi/18d63def57edb25f1X1y3Nk~.html",
# # #             "已上市",
# # #             "10000人以上",
# # #             "Java开发工程师\n西安·雁塔区·科技路西口\n18-25K·14薪\n1-3年\n硕士\n谢先生高级工程师",
# # #             "https://www.zhipin.com/job_detail/6303ab4eaf8cc82d1XRz3dS6F1dU.html?lid=8WME50j5ZHB.search.58&securityId=dpTE-QUvxQyfW-u1atoDyYxRvtXWN7NcUcEaqmMu3U0lF6t-ME_KHLsdHCkKC_VzJLoIAV-5SXSdFnSB3-zfrgi4tBr3itzGLfTvQI7WZrAWsxc~&sessionId="
# # #         ],
# # #         "dom_29": [
# # #             "软件工程师",
# # #             "西安·雁塔区·沣惠南路",
# # #             "6-10K·13薪",
# # #             "1-3年",
# # #             "本科",
# # #             "陕西通力数智科技",
# # #             "https://www.zhipin.com/gongsi/3c0d3205fc2403111Hd53tm8E1E~.html",
# # #             "未融资",
# # #             "0-20人",
# # #             "软件工程师\n西安·雁塔区·沣惠南路\n6-10K·13薪\n1-3年\n本科\n韦女士行政总监",
# # #             "https://www.zhipin.com/job_detail/ae489f82f08782cb1HB42965EVtR.html?lid=8WME50j5ZHB.search.59&securityId=WvC8-LLSk9L0T-41mMg5VDFs55XwAXg4iwHUyC6uBbZchKJ8b57fAiOao8WviRj0r-0dZZMN_-GXNkZkDIcjXPkfGnaePG5jQaLPIMM-LDrdAF74wipu&sessionId="
# # #         ],
# # #         "dom_3": [
# # #             "软件开发岗",
# # #             "西安·雁塔区·电子城",
# # #             "8-10K",
# # #             "1-3年",
# # #             "本科",
# # #             "西安商鼎",
# # #             "https://www.zhipin.com/gongsi/5dc00132a649d7820nNz2d21FQ~~.html",
# # #             "不需要融资",
# # #             "100-499人",
# # #             "软件开发岗\n西安·雁塔区·电子城\n8-10K\n1-3年\n本科\n王女士经理",
# # #             "https://www.zhipin.com/job_detail/a74f58d4338d772c1XB63tS-GVVR.html?lid=8WME50j5ZHB.search.33&securityId=XbKMNbXu5TiWE-r1xba5pD8NrG0c3hCjuPepa00zVUCYgLb0EjygEYGyCIqRyGC3eMeKOPdTPJpdiqzwgBlfmrjhfE0HIwi50v4pZHSmvInF50Dz0w~~&sessionId="
# # #         ],
# # #         "dom_30": [
# # #             "资深java开发工程师（自研/社交产品）",
# # #             "西安·雁塔区·高新软件园",
# # #             "20-30K·15薪",
# # #             "5-10年",
# # #             "本科",
# # #             "西安趣联网络科技...",
# # #             "https://www.zhipin.com/gongsi/25604d408e6962921nJ53tm6FVI~.html",
# # #             "未融资",
# # #             "100-499人",
# # #             "资深java开发工程师（自研/社交产品）\n西安·雁塔区·高新软件园\n20-30K·15薪\n5-10年\n本科\n颜女士HRBP\n在线",
# # #             "https://www.zhipin.com/job_detail/5b82cc3ccffe1dbd1HZ93Ny5F1tU.html?lid=8WME50j5ZHB.search.60&securityId=qZz0D7C9YLExb-q1btfV_U6PSo53DfToJCObOwYqF56iq-bnkkyQM8woH9VgVyq8QrjHUmluAK4S3KdzS5cgSlNINsG7rFotU6CqEOvgKBhRuuBzjXcBSj1HqPJc2ogo2APYZIGM4zpPD-HJ0I5X7_o~&sessionId="
# # #         ],
# # #         "dom_4": [
# # #             "软件开发工程师",
# # #             "西安·雁塔区·西安高新区",
# # #             "10-13K",
# # #             "3-5年",
# # #             "本科",
# # #             "北京慧泊金",
# # #             "https://www.zhipin.com/gongsi/a9a5dbbd5a9421100nJy09S8GQ~~.html",
# # #             "天使轮",
# # #             "20-99人",
# # #             "软件开发工程师\n西安·雁塔区·西安高新区\n10-13K\n3-5年\n本科\n立即沟通",
# # #             "https://www.zhipin.com/job_detail/cf5dba8292d1fa2a1Hd939-6EVtV.html?lid=8WME50j5ZHB.search.34&securityId=QxeDI3ebGP1UY-O1XmxGePokCaOXLfvCBkcZ6YykXEuZuy7QmT-rjdwVDXAE_4krLNODHJGulMC4tJ1lYkRxxZIMnuTJi1uYnugi-aeos-_f3T_WtmY~&sessionId="
# # #         ],
# # #         "dom_5": [
# # #             "Java",
# # #             "西安·雁塔区·高新路",
# # #             "11-15K",
# # #             "5-10年",
# # #             "大专",
# # #             "泰玛亚信",
# # #             "https://www.zhipin.com/gongsi/aa62b77f8ff101c91nFy3t-7GVs~.html",
# # #             "20-99人",
# # #             "NULL",
# # #             "Java\n西安·雁塔区·高新路\n11-15K\n5-10年\n大专\n曹先生招聘者",
# # #             "https://www.zhipin.com/job_detail/07bc634fbd96d9411nxz3t-0FFBS.html?lid=8WME50j5ZHB.search.35&securityId=1qHcjtWAq8dWA-51xwSJH_f4axUpqMwqFYTvjZerKWZz2DEj1OTCG5I52AVsn2ce6a2DjQzIj561PmQ8NP5c5AGDYBgqPKTqxkfc05OS13UAzT2Gv28~&sessionId="
# # #         ],
# # #         "dom_6": [
# # #             "计算机实习生",
# # #             "西安·新城区·金花路",
# # #             "150-200元/天",
# # #             "4天/周",
# # #             "3个月",
# # #             "恒愿公司",
# # #             "https://www.zhipin.com/gongsi/39924246f35a1cb71XFz29q6FFA~.html",
# # #             "未融资",
# # #             "0-20人",
# # #             "计算机实习生\n西安·新城区·金花路\n150-200元/天\n4天/周\n3个月\n本科\n王女士财务",
# # #             "https://www.zhipin.com/job_detail/43dfebd6842386d11HRz3tu8EVBT.html?lid=8WME50j5ZHB.search.36&securityId=If7INyC4SrAcB-v1siQ4uYa7sxiDz2wGq8BUPQncmEJsefCTJqtCPYV9ax1BuhirWtIccFLy4Ev3gV9heIpqcIg7lVyykOYgpHtnZkjQqynIr-hLPWVK&sessionId="
# # #         ],
# # #         "dom_7": [
# # #             "文档开发工程师-外包",
# # #             "西安·雁塔区·沣惠南路",
# # #             "12-13K",
# # #             "3-5年",
# # #             "本科",
# # #             "卓越际联科技有限公司",
# # #             "https://www.zhipin.com/gongsi/b58a0d258894b3c51HZ_0928EFQ~.html",
# # #             "1000-9999人",
# # #             "NULL",
# # #             "文档开发工程师-外包\n西安·雁塔区·沣惠南路\n12-13K\n3-5年\n本科\n刘女士人事经理",
# # #             "https://www.zhipin.com/job_detail/1c4bb6fb8d46fb4f1Hd62t-1FVVS.html?lid=8WME50j5ZHB.search.37&securityId=dwDRUjVjClvZu-o1jWAaSQBA-CXHPDazEZ1NsRNYt7O16waev3Fdqt3Bdbum3oQA-xC2bbB35MX6hT6-E7kCNNosnyTfpHhqeL6Z4y35LTdK_ilM9g~~&sessionId="
# # #         ],
# # #         "dom_8": [
# # #             "Java开发工程师",
# # #             "西安·未央区·未央路沿线",
# # #             "12-15K",
# # #             "3-5年",
# # #             "本科",
# # #             "锐角科技",
# # #             "https://www.zhipin.com/gongsi/d41fc2421438bc0833xy3920Eg~~.html",
# # #             "未融资",
# # #             "20-99人",
# # #             "Java开发工程师\n西安·未央区·未央路沿线\n12-15K\n3-5年\n本科\n蒋先生招聘者",
# # #             "https://www.zhipin.com/job_detail/870a71eedac0203033d609-8EVE~.html?lid=8WME50j5ZHB.search.38&securityId=or8hx2eZKZT5T-01DicYJAsGHgPQ-TrQVQz_VupvOQ4yvv4ilmWtT44y1Sk-Uqg7w8OxF-JkEiOAOxxmQMvJ6FfRye-xQGY8PzxW0mbRV_96H1hzbQ~~&sessionId="
# # #         ],
# # #         "dom_9": [
# # #             "Java开发工程师",
# # #             "西安·雁塔区·高新路",
# # #             "8-13K",
# # #             "3-5年",
# # #             "本科",
# # #             "西安蓝海之星",
# # #             "https://www.zhipin.com/gongsi/9ddcac12937c2e9e1nd_0t60E1s~.html",
# # #             "20-99人",
# # #             "NULL",
# # #             "Java开发工程师\n西安·雁塔区·高新路\n8-13K\n3-5年\n本科\n李女士财务",
# # #             "https://www.zhipin.com/job_detail/32557a389125b4df1nZ63tu_FFBQ.html?lid=8WME50j5ZHB.search.39&securityId=qOoeCsPcSphqJ-T1xvwaTEmcH-KkKhQJjmanu-o_6ngBtzh8QqIzii3K81JLa_7PGhl4MeFexleV4Z5jW694cO0aitE3VOZvmQuKRZyVFYGO7iwJnk75&sessionId="
# # #         ]
# # #     }
# # # }
# # # DATAZHILIAN: dict = {
# # #     "page_1": {
# # #         "dom_1": [
# # #             "java开发初级工程师",
# # #             "http://jobs.zhaopin.com/CC308088580J40116362308.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·长安·韦曲",
# # #             "4千-6千",
# # #             "1-3年",
# # #             "本科",
# # #             "西安中科图像技术有限公司",
# # #             "http://company.zhaopin.com/CC308088585.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_10": [
# # #             "开发工程师（JAVA）",
# # #             "http://jobs.zhaopin.com/CC153424414J90250803000.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·未央·张家堡",
# # #             "7千-1.4万·13薪",
# # #             "1-3年",
# # #             "本科",
# # #             "普联软件股份有限公司",
# # #             "https://pansoft.zhaopin.com/?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_11": [
# # #             "JAVA开发工程师",
# # #             "http://jobs.zhaopin.com/CC000402820J40395842902.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1万-1.5万",
# # #             "3-5年",
# # #             "本科",
# # #             "金航数码科技有限责任公司",
# # #             "http://company.zhaopin.com/CZ000402820.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "国企",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_12": [
# # #             "煤矿Java高级开发工程师",
# # #             "http://jobs.zhaopin.com/CC193399810J40273938807.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·新城·西一路",
# # #             "8千-1.6万·13薪",
# # #             "3-5年",
# # #             "大专",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_13": [
# # #             "java开发工程师",
# # #             "http://jobs.zhaopin.com/CC649781480J40214716405.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "7千-1.4万",
# # #             "经验不限",
# # #             "本科",
# # #             "东华医为科技有限公司",
# # #             "http://company.zhaopin.com/CZ649781480.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_14": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC000638920J40582263514.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "1.2万-1.3万",
# # #             "3-5年",
# # #             "本科",
# # #             "上海微创软件股份有限公司",
# # #             "http://company.zhaopin.com/CZ000638920.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "合资",
# # #             "10000人以上"
# # #         ],
# # #         "dom_15": [
# # #             "java开发工程师(24届)",
# # #             "http://jobs.zhaopin.com/CC193399810J40564104107.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "6千-1万",
# # #             "无经验",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_16": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC649781480J40257218505.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "7千-1.4万",
# # #             "1-3年",
# # #             "本科",
# # #             "东华医为科技有限公司",
# # #             "http://company.zhaopin.com/CZ649781480.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_17": [
# # #             "后端开发JAVA/C/C++/Python",
# # #             "http://jobs.zhaopin.com/CCL1476319810J40595565015.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "8千-1.2万",
# # #             "经验不限",
# # #             "本科",
# # #             "西安软玥信息技术有限公司",
# # #             "http://company.zhaopin.com/CZL1476319810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_18": [
# # #             "Java开发工程师(东华医为一站式组-西安)",
# # #             "http://jobs.zhaopin.com/CC193399810J40540880007.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "1万-1.8万",
# # #             "1-3年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_19": [
# # #             "java高级开发工程师",
# # #             "http://jobs.zhaopin.com/CC649781480J40459440905.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "1.4万-2.8万",
# # #             "5-10年",
# # #             "本科",
# # #             "东华医为科技有限公司",
# # #             "http://company.zhaopin.com/CZ649781480.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_2": [
# # #             "java软件开发工程师",
# # #             "http://jobs.zhaopin.com/CCL1421653950J40579287605.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·未央·张家堡",
# # #             "7千-9千",
# # #             "经验不限",
# # #             "大专",
# # #             "陕西博志弘达网络科技有限公司",
# # #             "http://company.zhaopin.com/CZL1421653950.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "其它",
# # #             "100-299人"
# # #         ],
# # #         "dom_20": [
# # #             "java实习生",
# # #             "http://jobs.zhaopin.com/CCL1461708100J40608870812.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "5千-9千",
# # #             "经验不限",
# # #             "学历不限",
# # #             "西安青树软件科技有限公司",
# # #             "http://company.zhaopin.com/CZL1461708100.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "100-299人"
# # #         ],
# # #         "dom_21": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC193399810J40238099007.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "面议",
# # #             "1-3年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_22": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC649781480J40551954505.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "7千-1.2万·13薪",
# # #             "1-3年",
# # #             "本科",
# # #             "东华医为科技有限公司",
# # #             "http://company.zhaopin.com/CZ649781480.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_23": [
# # #             "JAVA/C/C++/Python/go/web开发工程师 14薪，全额社保公积金 应届生/考研/考公失败可投",
# # #             "http://jobs.zhaopin.com/CC138117190J40584483105.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1万-2万·14薪",
# # #             "经验不限",
# # #             "本科",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_24": [
# # #             "Java开发工程师（银行经验优先）",
# # #             "http://jobs.zhaopin.com/CC193399810J40534918907.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·曲江",
# # #             "面议",
# # #             "3-5年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_25": [
# # #             "Java开发实施工程师",
# # #             "http://jobs.zhaopin.com/CC649781480J40134871905.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·新城·自强路",
# # #             "1.2万-1.8万",
# # #             "3-5年",
# # #             "本科",
# # #             "东华医为科技有限公司",
# # #             "http://company.zhaopin.com/CZ649781480.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_26": [
# # #             "java开发实习生",
# # #             "http://jobs.zhaopin.com/CCL1484160000J40559466716.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·杜城",
# # #             "5千-8千",
# # #             "经验不限",
# # #             "本科",
# # #             "西安正麦科技有限公司",
# # #             "http://company.zhaopin.com/CZL1484160000.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "20人以下",
# # #             "计算机软件"
# # #         ],
# # #         "dom_27": [
# # #             "Java开发工程师(东华医为-西安)",
# # #             "http://jobs.zhaopin.com/CC193399810J40540530707.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "1万-2万",
# # #             "3-5年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_28": [
# # #             "初级java开发工程师",
# # #             "http://jobs.zhaopin.com/CCL1427428230J40338124604.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "5千-9千",
# # #             "经验不限",
# # #             "大专",
# # #             "西安恒曜信息科技有限公司",
# # #             "http://company.zhaopin.com/CZL1427428230.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "股份制企业",
# # #             "20-99人"
# # #         ],
# # #         "dom_29": [
# # #             "Java开发",
# # #             "http://jobs.zhaopin.com/CC354987010J40493312411.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "6千-8千",
# # #             "经验不限",
# # #             "大专",
# # #             "西安亿才软件服务外包有限公司",
# # #             "http://company.zhaopin.com/CC354987012.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "其它",
# # #             "20-99人"
# # #         ],
# # #         "dom_3": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC138117190J40549113705.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1.5万-3万·14薪",
# # #             "经验不限",
# # #             "本科",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_30": [
# # #             "Java开发工程师(东华医为楼宇管控组-西安)",
# # #             "http://jobs.zhaopin.com/CC193399810J40540858007.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "1万-1.8万",
# # #             "3-5年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_4": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC212804510J40552699604.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1万-1.5万·13薪",
# # #             "1-3年",
# # #             "本科",
# # #             "北京国基科技股份有限公司",
# # #             "http://company.zhaopin.com/%E5%8C%97%E4%BA%AC%E5%9B%BD%E5%9F%BA%E7%A7%91%E6%8A%80%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8_CC212804513.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "100-299人"
# # #         ],
# # #         "dom_5": [
# # #             "java开发工程师中级",
# # #             "http://jobs.zhaopin.com/CC134310320J40549261906.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1.4万-1.5万",
# # #             "3-5年",
# # #             "本科",
# # #             "新拓尼克科技研发中心 / Syntronic Beijing R&D Center",
# # #             "http://company.zhaopin.com/CZ134310320.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "外商独资",
# # #             "500-999人"
# # #         ],
# # #         "dom_6": [
# # #             "软件开发工程师C/C++/Java/Python 接受23届",
# # #             "http://jobs.zhaopin.com/CC138117190J40547355505.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1.5万-3万",
# # #             "经验不限",
# # #             "本科",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_7": [
# # #             "Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC225692020J40621276712.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1.1万-1.5万",
# # #             "5-10年",
# # #             "本科",
# # #             "陕西协通智能科技有限公司",
# # #             "http://company.zhaopin.com/CZ225692020.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_8": [
# # #             "java开发工程师（接受江浙区域长期出差）",
# # #             "http://jobs.zhaopin.com/CCL1280870410J40444895806.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·丈八沟",
# # #             "1.5万-2万·13薪",
# # #             "3-5年",
# # #             "本科",
# # #             "北京神州数字科技有限公司",
# # #             "http://company.zhaopin.com/CZL1280870410.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "10000人以上"
# # #         ],
# # #         "dom_9": [
# # #             "Java开发工程师(东华医为通用技术组-西安)",
# # #             "http://jobs.zhaopin.com/CC193399810J40540859407.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "西安·雁塔·鱼化寨",
# # #             "1万-1.8万",
# # #             "经验不限",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=854dea7d-553e-427d-b6df-586f8ed34eb8",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ]
# # #     },
# # #     "page_2": {
# # #         "dom_1": [
# # #             "软件开发实习生",
# # #             "http://jobs.zhaopin.com/CCL1484160000J40559206016.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·杜城",
# # #             "5千-9千",
# # #             "经验不限",
# # #             "本科",
# # #             "西安正麦科技有限公司",
# # #             "http://company.zhaopin.com/CZL1484160000.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "20人以下",
# # #             "计算机软件"
# # #         ],
# # #         "dom_10": [
# # #             "对日开发（西安）",
# # #             "http://jobs.zhaopin.com/CC378016610J40511770616.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·鱼化寨",
# # #             "8千-1.2万",
# # #             "3-5年",
# # #             "大专",
# # #             "上海朗裕信息科技有限公司",
# # #             "http://company.zhaopin.com/CC378016613.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_11": [
# # #             "初级java开发工程师",
# # #             "http://jobs.zhaopin.com/CC138117190J40533316105.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "NULL",
# # #             "1.5万-3万·14薪",
# # #             "NULL",
# # #             "NULL",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_12": [
# # #             "技术类简历优化师（JAVA/Web/测试）+居家办公",
# # #             "http://jobs.zhaopin.com/CCL1446817030J40564058201.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "NULL",
# # #             "20-40元/次",
# # #             "NULL",
# # #             "NULL",
# # #             "河北品聚网络科技有限公司",
# # #             "http://company.zhaopin.com/CZL1446817030.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "100-299人",
# # #             "企业服务"
# # #         ],
# # #         "dom_13": [
# # #             "对日Java开发",
# # #             "http://jobs.zhaopin.com/CC378016610J40247128316.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "7千-1万",
# # #             "1-3年",
# # #             "大专",
# # #             "上海朗裕信息科技有限公司",
# # #             "http://company.zhaopin.com/CC378016613.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_14": [
# # #             "人工智能开发助理",
# # #             "http://jobs.zhaopin.com/CCL1427428230J40294695404.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "7千-9千",
# # #             "经验不限",
# # #             "大专",
# # #             "西安恒曜信息科技有限公司",
# # #             "http://company.zhaopin.com/CZL1427428230.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "股份制企业",
# # #             "20-99人"
# # #         ],
# # #         "dom_15": [
# # #             "中高级Java开发（需要出差）",
# # #             "http://jobs.zhaopin.com/CCL1232301260J40545493913.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "9千-1.2万",
# # #             "3-5年",
# # #             "大专",
# # #             "陕西德易通信息科技有限公司",
# # #             "http://company.zhaopin.com/CZL1232301260.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_16": [
# # #             "对日JAVA软件开发工程师",
# # #             "http://jobs.zhaopin.com/CC515910530J40535159506.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "6千-1.2万",
# # #             "经验不限",
# # #             "大专",
# # #             "济南淘扑云信息技术有限公司",
# # #             "http://company.zhaopin.com/CZ515910530.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "20-99人",
# # #             "计算机软件"
# # #         ],
# # #         "dom_17": [
# # #             "对日Java开发工程师",
# # #             "http://jobs.zhaopin.com/CC621497980J40197159409.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "8千-1.2万·14薪",
# # #             "1-3年",
# # #             "大专",
# # #             "八六三软件",
# # #             "http://company.zhaopin.com/CZ621497980.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "国企",
# # #             "500-999人"
# # #         ],
# # #         "dom_18": [
# # #             "诚聘Java开发转渗透测试开发 培养 (23 届应届生）",
# # #             "http://jobs.zhaopin.com/CC000544460J40527146816.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·长安·王寺",
# # #             "8千-1万",
# # #             "1-3年",
# # #             "本科",
# # #             "软通动力信息技术(集团)股份有限公司",
# # #             "https://company.zhaopin.com/CZ000544460.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "10000人以上"
# # #         ],
# # #         "dom_19": [
# # #             "软件开发工程师 对日方向",
# # #             "http://jobs.zhaopin.com/CC536834620J40158512602.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "4千-5千",
# # #             "经验不限",
# # #             "大专",
# # #             "创未科技(大连)有限公司",
# # #             "http://company.zhaopin.com/CZ536834620.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "其它",
# # #             "20-99人"
# # #         ],
# # #         "dom_2": [
# # #             "JAVA开发实习生",
# # #             "http://jobs.zhaopin.com/CC478051780J40125694203.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "2千-3千",
# # #             "无经验",
# # #             "大专",
# # #             "中译语通科技(陕西)有限公司",
# # #             "http://company.zhaopin.com/CZ478051780.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "国企",
# # #             "20-99人"
# # #         ],
# # #         "dom_20": [
# # #             "软件开发+不限语言Java/python/c/c++/js等",
# # #             "http://jobs.zhaopin.com/CC138117190J40393128305.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "NULL",
# # #             "1.4万-2.8万·16薪",
# # #             "NULL",
# # #             "NULL",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_21": [
# # #             "软件工程师",
# # #             "http://jobs.zhaopin.com/CC562772130J40422507704.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·电子城",
# # #             "1.2万-1.6万",
# # #             "1-3年",
# # #             "本科",
# # #             "西安佳力海电子科技有限公司",
# # #             "http://company.zhaopin.com/CZ562772130.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "股份制企业",
# # #             "20人以下"
# # #         ],
# # #         "dom_22": [
# # #             "JAVA开发工程师（兼职）",
# # #             "http://jobs.zhaopin.com/CC414410210J40228155110.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "7千-1.4万元/月",
# # #             "3-5年",
# # #             "大专",
# # #             "西安海润通信技术有限公司",
# # #             "http://company.zhaopin.com/CZ414410210.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_23": [
# # #             "全国均有岗位java/c/c++/python开发/测试/算法/数据",
# # #             "http://jobs.zhaopin.com/CC138117190J40569636005.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "NULL",
# # #             "1.5万-3万·16薪",
# # #             "NULL",
# # #             "NULL",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_24": [
# # #             "c++开发（可接受研究生做java想转c++的）",
# # #             "http://jobs.zhaopin.com/CC867334950J40522652206.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·等驾坡",
# # #             "1.2万-1.8万·14薪",
# # #             "1-3年",
# # #             "本科",
# # #             "西安天宇星控信息科技有限公司",
# # #             "http://company.zhaopin.com/CZ867334950.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_25": [
# # #             "java开发工程师助理",
# # #             "http://jobs.zhaopin.com/CCL1484160000J40559452216.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·杜城",
# # #             "6千-1.1万",
# # #             "经验不限",
# # #             "本科",
# # #             "西安正麦科技有限公司",
# # #             "http://company.zhaopin.com/CZL1484160000.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "20人以下",
# # #             "计算机软件"
# # #         ],
# # #         "dom_26": [
# # #             "Java开发 开源社区方向 接受23届",
# # #             "http://jobs.zhaopin.com/CC138117190J40547375905.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "1.5万-3万",
# # #             "经验不限",
# # #             "本科",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_27": [
# # #             "研发工程师",
# # #             "http://jobs.zhaopin.com/CCL1421653950J40561157705.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "NULL",
# # #             "9千-1.6万·13薪",
# # #             "NULL",
# # #             "NULL",
# # #             "陕西博志弘达网络科技有限公司",
# # #             "http://company.zhaopin.com/CZL1421653950.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "其它",
# # #             "100-299人"
# # #         ],
# # #         "dom_28": [
# # #             "java测试工程师",
# # #             "http://jobs.zhaopin.com/CCL1427759050J40601134415.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "NULL",
# # #             "4千-6千",
# # #             "NULL",
# # #             "NULL",
# # #             "西安蓝衡科技有限公司",
# # #             "http://company.zhaopin.com/CZL1427759050.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_29": [
# # #             "Java开发实习",
# # #             "http://jobs.zhaopin.com/CCL1373581710J40207447813.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "150-200/天",
# # #             "无经验",
# # #             "本科",
# # #             "西安恒创金信网络科技有限公司",
# # #             "http://company.zhaopin.com/CZL1373581710.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "20-99人"
# # #         ],
# # #         "dom_3": [
# # #             "Java开发工程师(东华医为CLMS事业部-西安)",
# # #             "http://jobs.zhaopin.com/CC193399810J40540747007.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·鱼化寨",
# # #             "1万-1.8万",
# # #             "3-5年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_30": [
# # #             "初级java开发工程师",
# # #             "http://jobs.zhaopin.com/CC280026710J40534691810.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "5千-8千",
# # #             "经验不限",
# # #             "本科",
# # #             "西安绿创电子科技有限公司",
# # #             "http://company.zhaopin.com/CZ280026710.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "100-299人"
# # #         ],
# # #         "dom_4": [
# # #             "后端开发实习生",
# # #             "http://jobs.zhaopin.com/CCL1461708100J40612961512.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "6千-9千",
# # #             "无经验",
# # #             "大专",
# # #             "西安青树软件科技有限公司",
# # #             "http://company.zhaopin.com/CZL1461708100.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "100-299人"
# # #         ],
# # #         "dom_5": [
# # #             "java软件开发工程师（实习）",
# # #             "http://jobs.zhaopin.com/CCL1310537910J40502983709.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·碑林·长安路",
# # #             "3千-5千",
# # #             "经验不限",
# # #             "大专",
# # #             "北京铃锋科技有限公司",
# # #             "http://company.zhaopin.com/CZL1310537910.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "20-99人",
# # #             "计算机软件"
# # #         ],
# # #         "dom_6": [
# # #             "中级java开发工程师（银行信贷、小贷公司或金融行业从业经验）",
# # #             "http://jobs.zhaopin.com/CC193399810J40457738207.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·曲江",
# # #             "面议",
# # #             "3-5年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_7": [
# # #             "java全栈实习生",
# # #             "http://jobs.zhaopin.com/CCL1461708100J40608086412.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "6千-9千",
# # #             "无经验",
# # #             "大专",
# # #             "西安青树软件科技有限公司",
# # #             "http://company.zhaopin.com/CZL1461708100.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "民营",
# # #             "100-299人"
# # #         ],
# # #         "dom_8": [
# # #             "java/c++/C/Python/前端开发工程师",
# # #             "http://jobs.zhaopin.com/CC138117190J40588343305.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·丈八沟",
# # #             "1.6万-2万·14薪",
# # #             "经验不限",
# # #             "本科",
# # #             "外企德科",
# # #             "http://company.zhaopin.com/CZ138117190.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "合资",
# # #             "1000-9999人"
# # #         ],
# # #         "dom_9": [
# # #             "Java高级开发工程师",
# # #             "http://jobs.zhaopin.com/CC193399810J40373457407.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "西安·雁塔·鱼化寨",
# # #             "面议",
# # #             "5-10年",
# # #             "本科",
# # #             "东华软件股份公司",
# # #             "http://company.zhaopin.com/CZ193399810.htm?refcode=4019&srccode=401901&preactionid=c6884c89-1518-4e97-8c47-275fba2ec027",
# # #             "上市公司",
# # #             "1000-9999人"
# # #         ]
# # #     }
# # # }
# # # # 第一步：生成engine对象
# # # engine = create_engine(
# # #     "mysql+pymysql://{0}:{4}@{1}:{2}/{3}".format(config.dbcfg["user"], config.dbcfg["address"], config.dbcfg["port"],
# # #                                                  config.dbcfg["dbname"], config.dbcfg["passwd"]),
# # #     max_overflow=0,  # 超过连接池大小外最多创建的连接
# # #     pool_size=5,  # 连接池大小
# # #     pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
# # #     pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
# # # )
# # #
# # #
# # # # 格式化数据（需要可视化的数据）
# # # def formattingData(domain_name: str, data: dict) -> list:
# # #     dataList: list = returnList(data=data)
# # #     if domain_name == "www.zhipin.com":
# # #
# # #         for i, j in enumerate(dataList):
# # #             j[1], j[10] = j[10], j[1]
# # #             j[3], j[10] = j[10], j[3]
# # #             j[5], j[10] = j[10], j[5]
# # #             j[6], j[10] = j[10], j[6]
# # #             j[7], j[10] = j[10], j[7]
# # #             j[9], j[10] = j[10], j[9]
# # #             j[8], j[9] = j[9], j[8]
# # #             # print(i, j)
# # #
# # #     elif domain_name == "sou.zhaopin.com":
# # #
# # #         for i, j in enumerate(dataList):
# # #             j[2], j[3] = j[3], j[2]
# # #             j[4], j[5] = j[5], j[4]
# # #             j[8], j[9] = j[9], j[8]
# # #
# # #     return dataList
# # #
# # #
# # # def returnList(data: dict) -> list:
# # #     tempList: list = []
# # #     iter_data = iter(data.items())
# # #     while True:
# # #         try:
# # #             K, V = next(iter_data)
# # #             iter_V = iter(V.items())
# # #             while True:
# # #                 try:
# # #                     k, v = next(iter_V)
# # #                     tempList.append(v)
# # #                 except StopIteration:
# # #                     break
# # #         except StopIteration:
# # #             break
# # #     return tempList
# # #
# # #
# # # # print(formattingData(domain_name="www.zhipin.com", data=DATABOSS))
# # # # 第二步：拿到一个Session类,传入engine
# # # Session = sessionmaker(bind=engine)
# # # # 第三步：拿到session对象,相当于连接对象（会话）
# # # session = Session()
# # # # for i in formattingData(domain_name="www.zhipin.com", data=DATABOSS):
# # # #     job = Jobs(jobName=i[0], jobUrl=i[1], jobPay=i[2], jobAddress=i[3], jobQualification=i[4], jobEXP=i[5],
# # # #                jobCorporation=i[6], jobCorporationUrl=i[7], jobCorporationBg1=i[8], jobCorporationBg2=i[9])
# # # #     session.add(job)
# # # #     session.commit()
# # # # # 第五步：关闭session对象
# # # # session.close()
# # #
# # # # # 模糊搜索
# # # # like_pattern = '%新城%'
# # # # results = session.query(Jobs).filter(Jobs.jobAddress.like(like_pattern)).all()
# # # #
# # # # for i, user in enumerate(results):
# # # #     print(user.jobName,user.jobAddress,user.jobUrl,i+1)
# # # # cityRegions = ["碑林", "莲湖", "新城", "未央", "灞桥", "雁塔", "周至", "鄠邑", "长安", "蓝田", "临潼", "阎良", "高陵"]
# # # # for i in cityRegions:
# # # #     # like_pattern = '%{0}%'.format(i)
# # # #     # results = session.query(Jobs).filter(Jobs.jobAddress.like(like_pattern)).all()
# # # #     # result_count = results.count()
# # # #     search_term = i  # 模糊搜索关键词
# # # #     query = session.query(Jobs).filter(Jobs.jobAddress.like(f'%{search_term}%'))
# # # #     result_count = query.count()
# # # #
# # # #     # 打印查询到的数量
# # # #     print("{0}岗位数有{1}个！".format(i, result_count))
# # # # session.close()
# # #
# #
# # salaries = ["15-25K·14薪", "8-10K", "1.5万-2万·13薪", "7千-9千", "9千-1.2万", "10-15K·13薪", "12-16K·14薪"]
# #
# #
# # def setPayFormat(PayString):
# #     # 存在“·”
# #     tempList1: list = []
# #     if "·" in PayString:
# #         split_list = PayString.split("·")
# #         # 打印分割后的结果
# #         for item1 in split_list:
# #             tempList1.append(item1)
# #         # 处理“·”前的薪资
# #         # 存在“-”
# #         # 去除"薪"
# #         tempList1[1] = tempList1[1][:-1]
# #         tempList2: list = []
# #         if "-" in tempList1[0]:
# #             split_list = tempList1[0].split("-")
# #             for item2 in split_list:
# #                 tempList2.append(item2)
# #             # 如果-前后两个字符串结尾不一样且后面字符串结尾为K时
# #             if (tempList2[0][-1] != tempList2[1][-1]) and tempList2[1][-1] == "K":
# #                 tempList2[1] = tempList2[1][:-1]
# #                 Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1) * 1000
# #                 return Pay
# #             # 都为万
# #             if tempList2[0][-1] == tempList2[1][-1] == "万":
# #                 tempList2[0] = int(float(tempList2[0][:-1]) * 10000)
# #                 tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
# #                 Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1)
# #                 return Pay
# #                 # 都为千
# #             elif tempList2[0][-1] == tempList2[1][-1] == "千":
# #                 tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
# #                 tempList2[1] = int(float(tempList2[1][:-1]) * 1000)
# #                 Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1)
# #                 return Pay
# #             # 前为千,后为万
# #             elif (tempList2[0][-1] != tempList2[1][-1]) and (tempList2[0][-1] == "千" and tempList2[1][-1] == "万"):
# #                 tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
# #                 tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
# #                 Pay = round((((int(tempList2[0]) + int(tempList2[1])) / 2) * int(tempList1[1])) / 12, 1)
# #                 return Pay
# #
# #     else:
# #         tempList2: list = []
# #         if "-" in PayString:
# #             split_list = PayString.split("-")
# #             for item2 in split_list:
# #                 tempList2.append(item2)
# #             # 如果-前后两个字符串结尾不一样且后面字符串结尾为K时
# #             if (tempList2[0][-1] != tempList2[1][-1]) and tempList2[1][-1] == "K":
# #                 tempList2[1] = tempList2[1][:-1]
# #                 Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1) * 1000
# #                 return Pay
# #             # 都为万
# #             if tempList2[0][-1] == tempList2[1][-1] == "万":
# #                 tempList2[0] = int(float(tempList2[0][:-1]) * 10000)
# #                 tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
# #                 Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1)
# #                 return Pay
# #                 # 都为千
# #             elif tempList2[0][-1] == tempList2[1][-1] == "千":
# #                 tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
# #                 tempList2[1] = int(float(tempList2[1][:-1]) * 1000)
# #                 Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1)
# #                 return Pay
# #             # 前为千,后为万
# #             elif (tempList2[0][-1] != tempList2[1][-1]) and (tempList2[0][-1] == "千" and tempList2[1][-1] == "万"):
# #                 tempList2[0] = int(float(tempList2[0][:-1]) * 1000)
# #                 tempList2[1] = int(float(tempList2[1][:-1]) * 10000)
# #                 Pay = round(((int(tempList2[0]) + int(tempList2[1])) / 2), 1)
# #                 return Pay
# #

import redis

# 连接到本地的 Redis 实例
r = redis.Redis(host='192.168.43.53', port=6379, db=0, password='redis_QBc2mF')

# 设置一个 key
r.set('name', 'xiaohua')

# 获取一个 key
print(r.get('name'))