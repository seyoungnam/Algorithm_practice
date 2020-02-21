# My Code
def solution(bridge_length, weight, truck_weights):
    answer = 0
    done_list = []
    on_list = []
    cnt_list = []
    count = len(truck_weights)
    while len(done_list) != count :
        # 다리 위 트럭별 경과시간 카운팅
        for i in range(len(cnt_list)):
            cnt_list[i] += 1

        
        # 다리 통과한 트럭은 on_list에서 done_list로 이동
        if len(cnt_list) >= 1 and cnt_list[0] > bridge_length:
            done_list.append(on_list.pop(0))
            cnt_list.pop(0)
        
        # 무게 한도 내에서 다리 위에 트럭 추가
        if len(truck_weights) >= 1 and sum(on_list) + truck_weights[0] <= weight:
            on_list.append(truck_weights[0])
            truck_weights.pop(0)
            cnt_list.append(1)
            
        answer += 1
        print("answer: ", answer)
        print("done_list=", done_list)
        print("on_list=", on_list)
        print("cnt_list=", cnt_list)
        print("truck_weights=", truck_weights)
        print("=============================")
            
    return answer

print(solution(2,10,[7,4,5,6]))
        

# Best Code
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()