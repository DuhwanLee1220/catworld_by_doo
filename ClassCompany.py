from msilib.schema import Error
from ClassPlayer import Player
import random as rd
import time
from printer import *
#일터
#일터에서 문제를 내고 문제를 풀면 player는 돈을 받음
#1번 문제유형: 몫 예측하기
#2번 문제유형: 평균 구하기(나머지 X)
#3번 문제유형: 무작위로 나오는 수 맞히기
#4번 문제유형: 번호판 4자리 수 더하기
class Company:
    
    def __init__(self,name):
        self.name = name
    
    def problem(self,player : Player):
        
        questionNum = rd.randint(1,4)
        printInfo('''
        당신은 회사에 도착했습니다.
        1~4까지 4개의 유형의 문제를 풀게 되며
        문제를 맞힐 시 10원이
        문제를 틀릴 시 1원이 주어집니다.
        한 문제당 10초가 주어지며 5초는 문제를 푸는 시간
        나머지 5초는 정답 입력시간입니다.
        
        3초 후 문제가 주어집니다....''')

        printLaterFewSec(3)
        printInfo('%d번 문제 유형입니다.' % questionNum)
        
        if questionNum == 1:
            a = rd.randint(1,601)
            b = rd.randint(600,1201)
            printInfo('%d를 %d로 나눈 값의 몫을 입력하시오.' %(b,a))
            k = 5
            for l in range(0,6):
                print(k - l)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            
            takeTime = end - start
            
            print('걸린시간 :',takeTime)
            
            if takeTime > 5:
                printInfo('5초를 초과했습니다.')
                answer = 1300 #600~1200까지의 숫자를 1~600으로 나눈 결과 중 1300은 절대 몫이 될 수 없음.
            else: pass
            
            if answer != b // a:
                printInfo('틀렸습니다. 정답은 %d입니다.' % (b//a))
                problemResult = False
            else:
                printInfo('정답입니다!')
                problemResult = True
        elif questionNum == 2:
            printInfo('''
            1~20까지의 무작위의 숫자가 2~5개만큼 무작위로 주어집니다.
            당신은 이 무작위의 숫자의 평균을 구하면 됩니다.
            단, 나머지는 구할 필요 없습니다.
            ''')
            avgList = []
            randomrange = rd.randint(3,6)
            for i in range(1,randomrange):
                avgList.append(rd.randint(1,20))
            print(avgList)
            
            result = 0
            for j in avgList:
                result += j
            
            k = 5
            for l in range(0,6):
                print(k - l)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            takeTime = end - start
            print('걸린시간 :',takeTime)
            if takeTime > 5:
                printInfo('5초를 초과했습니다.')
                answer = 0 #1~45까지의 숫자 2~10개 중 0은 절대 평균이 될 수 없음
            else: pass

            if answer != result // len(avgList):
                printInfo('틀렸습니다. 정답은 %d입니다.' % (result // len(avgList)))
                problemResult = False
            else:
                printInfo('정답입니다!')
                problemResult = True
        
        elif questionNum == 3:
            randnumber = rd.randrange(1,11)
            printLineFeed2('아쉽게도 가장 운을 사용해야 하는 문제를 풀게 되었습니다.\n1~10까지 무작위로 나오는 수를 맞히면 됩니다.')
            
            i = 5
            for j in range(0,6):
                print(i - j)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            takeTime = end - start
            print('걸린시간 :',takeTime)
            if takeTime > 5:
                print('5초를 초과했습니다.')
                answer = 11 #1~10까지의 숫자중에서 11은 절대 정답이 될 수 없음.
            else: pass

            if randnumber != answer:
                printInfo('틀렸습니다. 정답은 %d 입니다.' % randnumber)
                problemResult = False
            else:
                printInfo('정답입니다!')
                problemResult = True

        elif questionNum == 4:
            stNum = rd.randrange(0,10)
            ndNum = rd.randrange(0,10)
            rdNum = rd.randrange(0,10)
            thNum = rd.randrange(0,10)
            
            printInfo('%d%d%d%d의 자동차 번호판이 있습니다. 이 수를 모두 곱하세요' %(stNum,ndNum,rdNum,thNum))
        
            i = 5
            for j in range(0,6):
                print(i - j)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            takeTime = end - start
            print('걸린시간 :',takeTime)
            if takeTime >= 5:
                answer = 9**5 #9의 5제곱은 4자릿수 번호판에서 절대 정답이 될 수 없음.
            else: pass
            
            if answer != stNum * ndNum * rdNum * thNum:
                printInfo('틀렸습니다. 정답은 %d입니다' % (stNum * ndNum* rdNum* thNum))
                problemResult = False
            else:
                printInfo('정답입니다!')
                problemResult = True
        
        else: pass

        if problemResult == True:
            player.addMoney(10)
            printLaterFewSec(2)
            printMenu('잔고에 10만큼의 돈이 추가 되었습니다.\n당신의 잔고는 %d 입니다.'%player.balance)
        else:
            player.addMoney(1)
            printLaterFewSec(2)
            printMenu('잔고에 1만큼의 돈이 추가 되었습니다.\n당신의 잔고는 %d 입니다.'%player.balance)