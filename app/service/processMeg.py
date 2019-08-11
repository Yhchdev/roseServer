import json



# 解析消息
def parsing_message(message):
    receivedMeg =  str(message.payload)
    meg_dic = json.loads(receivedMeg[2:-1])
    id = meg_dic["id"]
    pic_list = meg_dic["pic"]


    # 模式(1.单花朵评估模式(速度快)/2.整只评估模式)
    #model = meg_dic["model"]
    # 时间戳
    timestamp = meg_dic["now"]
    #


    print(meg_dic)

    print(id)
    print(pic_list)
    print(timestamp)


