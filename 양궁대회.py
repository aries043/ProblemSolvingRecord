from copy import deepcopy

def combinationSum(candidates, target): # candidates안 숫자로 target를 얻을 수 있는 조합 얻기
        answer = []
        if len(candidates) == 1 and candidates[0] > target:
            return answer
        
        def dfs(diff, index, combinations):
            if diff == 0:
                answer.append(combinations)
                return
            if diff < 0:
                return
            
            for i in range(index, len(candidates)):
                dfs(diff - candidates[i], i, combinations + [candidates[i]])
                
        dfs(target, 0, [])
        
        return answer

def solution(n, info):  
    
    can = { # key번 쏴서 value값을 얻을 수 있음, 1<=n<=10이므로 다음과같이 설정
        10:[],9:[],8:[],7:[],6:[],5:[],4:[],3:[],2:[],1:[],
        }
    k = 0 # can에 과녁값을 추가하기 위해 선언한 변수
    for i in info: # 받아온 info에서 정보를 하나씩 꺼내옴
        if i!=0: # 상대방이 쏜 적이 있는 과녁일 경우
            can[i+1].append((10-k)*2) # 점수X2 만큼의 가치가 있음
        else:
            can[i+1].append(10-k)
        k += 1 # 다음 과녁값을 얻기 위해 k에 +1을 해줌
        
    noempty=[i for i in list(can.keys()) if can[i]!=[]] # 필요없는 can 추리기
    
    combinations = combinationSum(noempty, n) # noempty로 나올 수 있는 조합 후보들
    
    best = 0
    bestcomb = []
    
    bochung = 0
     
    for combination in combinations:
        cpycan = deepcopy(can)
        sum_comb = 0
        cpy_comb = deepcopy(combination)
        for key in combination:
            tmp = cpycan[key]
            if len(tmp)==0:
                cpy_comb.remove(key)
                continue
            sum_comb += tmp[0]
            tmp.remove(tmp[0])
            cpycan[key] = tmp
        if sum_comb>best:
            if sum(cpy_comb)!=n:
                bochung = n-sum(cpy_comb)
                bestcomb = cpy_comb
            else:
                bestcomb = combination
            best = sum_comb
        elif sum_comb==best: # 비교한 값이 같으면 낮은과녁 많이 맞힌 배열
            if len(bestcomb)<len(combination):
                if sum(cpy_comb)!=n:
                    bochung = n-sum(cpy_comb)
                    bestcomb = cpy_comb
                else:
                    bestcomb = combination
                    best = sum_comb
                    bochung = 0
            elif len(bestcomb) == len(combination):
                for g in range(len(combination)):
                    if bestcomb[g] < combination[g]:
                        if sum(cpy_comb)!=n:
                            bochung = n-sum(cpy_comb)
                            bestcomb = cpy_comb
                        else:
                            bestcomb = combination
                            best = sum_comb
                            break
    
    answer = [0,0,0,0,0,0,0,0,0,0,0]
    
    for key in bestcomb: # 2 2 1
        tmp = can[key]
        if key!=1:
            answer[10 - tmp[0]//2] = key
        else:
            answer[10 - tmp[0]] = key
        tmp.remove(tmp[0])
        can[key] = tmp
    
    answer[10] += bochung

    apeach = 0
    rion = 0
    s = 10
    for num_a, num_r in zip(info, answer):
        if num_a==0 and num_r==0:
            continue
        elif num_a >= num_r:
            apeach += s
            s -= 1
        else:
            rion += s
            s -= 1
    if apeach >= rion:
        return([-1])
    else:
        return(answer)
     

def main():
    n = int(input())
    info = list(map(int, input().split()))
    print(solution(n, info))

if __name__ == "__main__":
    main()



# 3 -> 20
# 2 -> 18, 16, 7
# 1 -> 12, 5, 4, 3, 2, 1

# 5
# 12,5,4,3,2  26
# 12,5,4,18   39
# 12,18,16    46    6 9 8
# 12,5,20     37
# 18,20      38


# ex)   info = [2,1,1,1,0,0,0,0,0,0] 입력받음

# 이 점수는 0이 아니라는 정보는 info로 추출한 값이 0이 아니었을 때 알 수 있음

# for문으로 info 정보를 하나씩 제공, info의 해당값이 0이 아니면 2배로 저장
# 3키 -> [20]
# 2키 -> [18, 16]
# 1키 -> [7,6,5,4,3,2,1]

# 키리스트 추출해서 n의 값이 나올수 있는 경우를 찾기
# noempty=[3,2,1]
# 1+1+1+1+1
# 1+1+1+2
# 1+2+2
# 1+1+3
# 2+3



# 찾을때마다 합을 구해서 max(초기값=0)에 저장
