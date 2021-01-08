title_text = """
______  _____  _   __ _____  _    _   ___   _   _  _____ 
| ___ \\|  _  || | / /|  ___|| |  | | / _ \\ | \\ | ||  __ \\
| |_/ /| | | || |/ / | |__  | |  | |/ /_\\ \\|  \\| || |  \\/
|  __/ | | | ||    \\ |  __| | |/\\| ||  _  || . ` || | __ 
| |    \\ \\_/ /| |\\  \\| |___ \\  /\\  /| | | || |\\  || |_\\ \\
\\_|     \\___/ \\_| \\_/\\____/  \\/  \\/ \\_| |_/\\_| \\_/ \\____/ 

---------------- Hit ENTER to start game. ---------------- 

"""


class Player:

    def __init__(self, name, monster_list):
        self.name = name
        self.monster_list = monster_list


class Monster:

    def __init__(self, name, attack_power, hp):
        # ? 새로 추가한 몬스터 이름
        self.name = name
        self.attack_power = attack_power
        self.hp = hp
        
    def printMonster(self):
        for i in range(10):
            print(f'몬스터 이름:{self[i].name}, 몬스터 공격력:{self[i].attack_power}, 몬스터 체력:{self[i].hp}')
        #! 이거 하는데 1시간30분 걸렸는데 예쁘게는 못했어
        UI.getMonsterList(monster_list)


class Card:

    def __init__(self, card_type):
        self.card_type = card_type

    def printCard(self):
        # TODO 3-3: 카드 정보 출력
        return


class UI:

    def __init__(self):
        # TODO 1: random_cards 리스트 채우
        self.random_cards = []
        self.player1 = None
        self.player2 = None

    def startGame(self):
        # TODO 1: 사용자가 0을 누르면 게임 종료, 1을 누르면 사용자 등록으로 이동
        user_input = int(input('0을 누르면 게임종료, 1을 누르면 사용자 등록으로 이동'))
        if user_input == 0 :
            print('게임이 끝났어요')
            #! 게임 끝나는 함수 구현 아직 못함
        return self.getUserName()
        return

    # TODO 2: self.player1과 self.player2를 설정하는 것이 목표!
    def getUserName(self):
        # TODO 2-1 : console input을 통해 사용자의 이름을 받아 return
        name1, name2 = map(str,input().split()) 
        self.printMonsterList()
        return name1, name2

    def printMonsterList(self):
        # TODO 2-2 : 선택 가능한 몬스터 리스트 출력
        Monster.printMonster(monster_list)

    def getMonsterList(self):
        # TODO 2-3 : 사용자가 선택한 몬스터를 담은 리스트를 반환
        user1_choice = []
        user2_choice = []
        user1_list = []
        user2_list = []
        
        user1_choice = input('5개를 선택하세요').split()
        user2_choice = input('5개를 선택하세요').split()
        
        for i in range(5):
            for j in range(10):
                if user1_choice[i] == monster_list[j].name:
                    user1_list.append(user1_choice[i])
                if user2_choice[i] == monster_list[j].name:
                    user2_list.append(user2_choice[i])
        print(user1_list)
        print(user2_list)
        # ! 여기서 멈췄어...

    def initPlayer(self):
        # TODO 2-4 : 이름과 monster_list가 설정된 Player 객체 반환
        # use method getUserName
        # use method getMonsterList
        # return player
        return

    def registerPlayers(self):
        # TODO 2-5: self.player1과 self.player2 설정
        # use method initPlayer
        return

        # TODO 3: 라운드 시작을 위해 player 별로 몬스터를 선택하고 랜덤 카드를 오픈
        def displayMonsterList(self, player_num):
            # TODO 3-1: player의 현재 monster_list를 출력
            if player_num == 1:
                print(player_num, 'player의 현재 monster list는', monster_list, '입니다.')
            else:
                print(player_num, 'player의 현재 monster list는', monster_list, '입니다.')
            return

        def selectMonster(self, player_num):
            # TODO 3-2: 사용자 입력을 받아 이번 판에 출전시킬 몬스터 정보를 출력 후 해당 몬스터를 반환
            # use displayMonsterList
            # use class Monster-printMonster
            # return monster
            print('출전시킬 몬스터를 선택하세요.')
            choose = int(input)
            if player_num == 1:
                monster1 = monster_list[choose]
                return monster1
            else:
                monster2 = monster_list[choose]
                return monster2

        def openRandomCard(self, player_num):
            # TODO 3-3: self.random_cards에서 랜덤하게 한 카드를 골라 정보를 출력 후 해당 카드를 반환
            # use class Card-printCard
            # return card
            self.random_cards = card
            card = random.choice(card_type)
            Card.printCard()
            if player_num == 1:
                card1 = card
                return card1

    else:
    card2 = card
    return card2


def initRound(self):
    # TODO 3-4: player1, 2 각각이 선택한 몬스터와 오픈한 랜덤카드 쌍을 반환
    # use selectMonster
    # use openRandomCard
    # return [[monster1, card1], [monster2, card2]]
    monster1 = selectMonster(1)
    monster2 = selectMonster(1)
    card1 = openRandomCard(1)
    card2 = openRandomCard(2)
    return [[monster1, card1], [monster2, card2]]

    def battle(self, game_info):
        # TODO 4-1: 랜덤카드의 효과를 고려해 monster들의 hp를 수정, 이 때 hp <= 0일 경우 그냥 0으로 고정. 플레이 후 몬스터들을 반환
        # use result from initRound(gameInfo)
        # return [monster1, monster2]

        game_info[0][0].hp -= game_info[1][0].attack_power * game_info[1][1].card_type
        game_info[1][0].hp -= game_info[0][0].attack_power * game_info[0][1].card_type
        for i in range(2):
            if game_info[i][0].hp <= 0:
                game_info[i][0].hp = 0

        return [game_info[0][0], game_info[1][0]]

    def printResult(self, monster_pair):
        # TODO 4-2: 게임 결과 출력. 게임 후 monster 정보(죽었을 경우 죽었다고 출력)
        # use printMonster
        # use return from battle(monsterPair)
        if monster_pair[0].hp == 0 and monster_pair[1].hp == 0:
            print("player1,2의 몬스터가 전투결과 모두 사망하였습니다. ㅠㅅㅠ")
        elif monster_pair[0].hp == 0:
            print("player 1의 몬스터가 전투결과 사망하였습니다. ㅠㅠ")
            print("전투를 마친 player2의 몬스터의 정보가 업데이트됩니다.")
            monster_pair[1].printMonster()
        elif monster_pair[1].hp == 0:
            print("player 2의 몬스터가 전투결과 사망하였습니다. ㅠㅠ")
            print("전투를 마친 player1의 몬스터의 정보가 업데이트됩니다.")
            monster_pair[0].printMonster()
        else:
            print("전투를 마친 player1,2의 몬스터의 정보가 업데이트됩니다.")
            monster_pair[0].printMonster()
            monster_pair[1].printMonster()

    def endOfGame(self):
        # TODO 4-3: 다음 라운드를 위해 player의 monster_list에 몬스터가 남아있는지 확인후 게임을 계속해도 되면 true, 아니면 false 반환
        # return True/False
        if self.player1.monster_list == [] or self.player2.monster_list == []:
            return False
        else:
            return True

    def playRound(self):

        # TODO 4-4: 한 라운드를 실행
        # use battle/printResult/endOfGame
        battleresult = self.battle(self.initRound())
        self.printResult(battleresult)
        if self.endOfGame:
            print("게임을 계속 진행합니다.")
        else:
            print("남아있는 몬스터가 없습니다. 게임을 종료합니다!")

        # TODO 5: 승패가 갈릴때까지 라운드를 반복;

    def printFinalResult(self):
        # p1,p2 = 플레이어 정보  ---> 위에 printResult에서 결과가 매번 저장될거라고 예상하고 쓴거라 만약 그냥 초기값이 출력되면,,나중에 고쳐보겟슴니다,,
        p1 = self.player1
        p2 = self.player2

        # 각 플레이어의 몬스터가 몇개 남았는지 저장
        p1_length = len(p1.monster_list)
        p2_length = len(p2.monster_list)

        # 몬스터가 더 적은쪽(아마 0개인 쪽)이 패자
        if p1_length < p2_length:
            # 승자
            print(f"승자:{p2.name}, 남은 몬스터:{p2.monster_list}")
            # 패자
            print(f"패자:{p1.name}, 남은 몬스터:{p1.monster_list}")
        elif p2_length < p1_length:
            # 승자
            print(f"승자:{p1.name}, 남은 몬스터:{p1.monster_list}")
            # 패자
            print(f"패자:{p2.name}, 남은 몬스터:{p2.monster_list}")
        else:
            print("무승부")
            print(f"플레이어1:{p1.name}, 남은 몬스터:{p1.monster_list}")
            print(f"플레이어2:{p2.name}, 남은 몬스터:{p2.monster_list}")

        # TODO 5-1: 승자와 패자를 출력. 게임 종료 당시 남아있는 포켓몬의 리스트를 출력
        # return

    def playGame(self):
        while True:
            play = self.playRound()  # playRound()에서 False나 True를 반환하는 경우=playRound()에서 endOfGame()의 결과를 반환해주는 경우

            # self.playRound()
            # end = self.endOfGame() -->이건 혹시나 playRound()에서 endOfGame()결과를 반환하지 않는 경우를 대비해서 써봄

            if play == False:  # 게임을 더 진행할 수 없으면
                self.printFinalResult()  # 최종 결과 출력
                break

        # TODO 5-2: 승패가 갈릴때까지 라운드를 반
        # use playRound
        # use printFinalResult
        # return


if __name__ == "__main__":
    # TODO 1: 게임 실행 -> 종료 시 새로운 게임 여부 확인 반복
    monster_list = [Monster("A",30, 100),
                   Monster("B",30, 150),
                   Monster("C",40, 300),
                   Monster("D",50, 100),
                   Monster("E",30, 150),
                   Monster("F",30, 100),
                   Monster("G",40, 300),
                   Monster("H",50, 200),
                   Monster("I",30, 250),
                   Monster("J",20, 150),
                   ]
    
    card_type = [Card(3.0),
                Card(1.5),
                Card(2.0),
                Card(1.4),
                Card(0.2),
                Card(0.3),
                Card(2.5),
                Card(1.7),
                Card(1.5),
                Card(0.8),
                ]
    
    print(title_text)
    ui = UI()
    ui.startGame()
    
    
    # ? 한 부분 : todo 1, todo2-1, todo2-2, todo2-3
    # ! 못한 부분 : todo 1(random 카드 채우기), todo 2-4, todo 2-5 
