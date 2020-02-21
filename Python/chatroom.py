def solution(record):
    # 필요한 변수 선언
    enter_msg = "%s님이 들어왔습니다."
    leave_msg = "%s님이 나갔습니다."
    chat_list = []
    user_dict = {}
    
    for ele in record:
        str_list = ele.split(' ')
        
        # 'enter': id, enter_msg
        #           id, nickname mapping
        if str_list[0] == 'Enter':
            chat_list.append([str_list[1], enter_msg])
            user_dict[str_list[1]] = str_list[2]
        # 'leave': id, leave_msg
        elif str_list[0] == 'Leave':
            chat_list.append([str_list[1], leave_msg])
        # 'change': id, nickname 수정
        elif str_list[0] == 'Change':
            user_dict[str_list[1]] = str_list[2]
    return chat_list

record = ["Enter uid1234 Muzi", 
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan"]
        
print(solution(record))