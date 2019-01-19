from time import sleep
import random

noteArr = []  # 노트가 들어갈 배열

while True:

    print("*******단어 암기노트 ********")
    print("*** 1. 노트 작성하기 ********")
    print("*** 2. 노트 다시 시험보기 ****")
    print("****3. 노트 둘러보기 ********")
    print("****4. 단어로 뜻 찾아보기 ****")
    print("****5. 단어 모두 섞기  ******")
    print("****6. 단어 지우기 *********")
    print("****7. 단어장 초기화  *******")
    print("****8. 단어 시험  **********")

    menuNum = input("원하는 메뉴의 숫자를 입력하세요 : ")

    if menuNum == "1":
        print("단어에 'Q' 라고 입력하면 입력을 종료합니다.")
        tmpVoca = ""
        tmpMean = ""
        while True:
            tmpVoca = input("단어를 입력하세요! : ")
            if tmpVoca == "Q":  # Q 가 입력되면 루프를 나갑니다.
                break;
            tmpMean = input("뜻을 입력하세요! ")
            noteArr.append([tmpVoca, tmpMean])

    elif menuNum == "2":
        if len(noteArr) == 0:
            print("단어장이 비어있습니다!")
        else:
            for i in range(0, len(noteArr)):
                print("단어: " + noteArr[i][0])
                sleep(1)
                print("뜻: " + noteArr[i][1])
                sleep(1)
            print("모든 단어를 출력했습니다.")

    elif menuNum == "3":
        if len(noteArr) == 0:
            print("단어장이 비어있습니다.")
        else:
            for i in range(0, len(noteArr)):
                print(i, "번째 ->" + "단어 :" + noteArr[i][0] + "   " + "뜻 :" + noteArr[i][1])

    elif menuNum == "4":
        print("단어가 중복되었을 시 중복된 단어의 뜻을 모두 출력합니다.")
        tmpVocaFind = input("찾고 싶은 단어를 입력하세요 : ")
        findVocaIndex = []
        for i in range(0, len(noteArr)):
            if noteArr[i][0] == tmpVocaFind:
                findVocaIndex.append(i)
        if len(findVocaIndex) == 0:
            print("해당되는 단어가 없습니다.")
        else:
            for i in range(0, len(findVocaIndex)):
                print(i, ":" + "뜻: " + noteArr[findVocaIndex[i]][1])

    elif menuNum == "5":
        random.shuffle(noteArr)
        print("단어를 모두 섞었습니다.")

    elif menuNum == "6":
        if len(noteArr) == 0:
            print("단어장이 비어있습니다.")
        else:
            for i in range(0, len(noteArr)):
                print(i, "번째 ->" + "단어 :" + noteArr[i][0] + "   " + "뜻 :" + noteArr[i][1])
            inputNum = int(input("지우고 싶은 단어의 순서를 입력하세요."))
            if inputNum <= len(noteArr) and inputNum >= 0 :
                del (noteArr[inputNum])
                print("단어가 성공적으로 삭제 되었습니다.")
            else:
                print("제대로 된 키를 입력 해 주세요!")

    elif menuNum == "7":
        noteArr.clear()
        print("단어장이 모두 초기화 되었습니다.")


    elif menuNum == "8":
        if len(noteArr) == 0:
            print("단어장이 비어있습니다!")
        else:
            vocaCorrect = 0
            for i in range(0, len(noteArr)):
                print("단어: " + noteArr[i][0])
                vocaCheck = input("이 단어의 뜻을 입력하세요!")
                if vocaCheck == noteArr[i][1]:
                    vocaCorrect = vocaCorrect + 1
                    print("정답입니다.")
                else:
                    print("오답입니다.")
            print("총 ",len(noteArr), "개 중에서" , vocaCorrect ,"개를 맞췄습니다.")

    else:
        print("맞는 번호를 입력하세요!")

