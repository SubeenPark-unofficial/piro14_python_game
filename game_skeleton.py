import random


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

    def displayMonsterList(self):
        # TODO 3-1: player의 현재 monster_list를 출력
        for i, monster in enumerate(self.monster_list):
            print(f"[{i+1}] ", end="")
            monster.printMonster()

    def selectMonster(self):
        choice = int(input('출전시킬 몬스터를 선택하세요.'))
        return self.monster_list[choice-1]

    def renewMonsterList(self):
        new_monster_list = []
        for monster in self.monster_list:
            if monster.hp != 0:
                new_monster_list.append(monster)
        self.monster_list = new_monster_list


class Monster:

    def __init__(self, name, attack_power, hp):
        # ? 새로 추가한 몬스터 이름
        self.name = name
        self.attack_power = attack_power
        self.hp = hp
        
    def printMonster(self):
        print(f'몬스터 이름:{self.name}, 몬스터 공격력:{self.attack_power}, 몬스터 체력:{self.hp}')


class Card:

    def __init__(self, probability):
        self.card_type = probability

    def printCard(self):
        # TODO 3-3: 카드 정보 출력
        print(f'카드 유형: 공격력을 {self.card_type}배 증가!')


class UI:

    def __init__(self, monsters_candidate, random_cards):
        # TODO 1: random_cards 리스트 채우
        self.random_cards = random_cards
        self.player1 = None
        self.player2 = None
        self.monsters_available = monsters_candidate

    def startGame(self):
        # TODO 1: 사용자가 0을 누르면 게임 종료, 1을 누르면 사용자 등록으로 이동
        user_input = int(input('0을 누르면 게임종료, 1을 누르면 사용자 등록으로 이동'))

        while user_input != 0:
            if user_input == 1:
                self.registerPlayers()
                self.playGame()
            else:
                user_input = int(input('0을 누르면 게임종료, 1을 누르면 사용자 등록으로 이동'))

        print("게임이 끝났어요")

    # TODO 2: self.player1과 self.player2를 설정하는 것이 목표!
    @staticmethod
    def getUserName():
        # TODO 2-1 : console input을 통해 사용자의 이름을 받아 return
        return input("플레이어의 이름을 입력하세요: ")

    def printMonsterList(self):
        # TODO 2-2 : 선택 가능한 몬스터 리스트 출력
        for i, monster in enumerate(self.monsters_available):
            print(f"[{i+1}] ", end="")
            monster.printMonster()

    def getMonsterList(self):
        # TODO 2-3 : 사용자가 선택한 몬스터를 담은 리스트를 반환
        self.printMonsterList()
        user_choice = map(int, input("몬스터를 다섯 마리 선택하세요.").split())
        return [self.monsters_available[idx-1] for idx in user_choice]

    def initPlayer(self):
        # TODO 2-4 : 이름과 monster_list가 설정된 Player 객체 반환
        return Player(self.getUserName(), self.getMonsterList())

    def registerPlayers(self):
        # TODO 2-5: self.player1과 self.player2 설정
        print('사용자 1 설정')
        self.player1 = self.initPlayer()
        print('사용자 2 설정')
        self.player2 = self.initPlayer()

    # TODO 3: 라운드 시작을 위해 player 별로 몬스터를 선택하고 랜덤 카드를 오픈

    @staticmethod
    def selectMonster(player):
        # TODO 3-2: 사용자 입력을 받아 이번 판에 출전시킬 몬스터 정보를 출력 후 해당 몬스터를 반환
        # use displayMonsterList
        # return monster
        print(player.name)
        player.displayMonsterList()
        monster = player.selectMonster()
        return monster

    def openRandomCard(self):
        # TODO 3-3: self.random_cards에서 랜덤하게 한 카드를 골라 정보를 출력 후 해당 카드를 반환
        # use class Card-printCard
        # return card
        card = random.choice(self.random_cards)
        card.printCard()
        return card

    def initRound(self):
        # TODO 3-4: player1, 2 각각이 선택한 몬스터와 오픈한 랜덤카드 쌍을 반환
        # use selectMonster
        # use openRandomCard
        # return [[monster1, card1], [monster2, card2]]
        monster1 = self.selectMonster(self.player1)
        monster2 = self.selectMonster(self.player2)
        print(f'{self.player1.name}의 랜덤카드: ', end="")
        card1 = self.openRandomCard()
        print(f'{self.player2.name}의 랜덤카드: ', end="")
        card2 = self.openRandomCard()
        return [[monster1, card1], [monster2, card2]]

    @staticmethod
    def battle(game_info):
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
        self.player1.renewMonsterList()
        self.player2.renewMonsterList()

    def endOfGame(self):
        # TODO 4-3: 다음 라운드를 위해 player의 monster_list에 몬스터가 남아있는지 확인후 게임을 계속해도 되면 true, 아니면 false 반환
        # return True/False
        if len(self.player1.monster_list) == 0 or len(self.player2.monster_list) == 0:
            return True
        else:
            return False

    def playRound(self):

        # TODO 4-4: 한 라운드를 실행
        # use battle/printResult/endOfGame
        battleresult = self.battle(self.initRound())
        self.printResult(battleresult)
        if not self.endOfGame():
            print("게임을 계속 진행합니다.")
            return False
        else:
            print("남아있는 몬스터가 없습니다. 게임을 종료합니다!")
            return True
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
            print(f"승자:{p2.name}")
            p2.displayMonsterList()

            # 패자
            print(f"패자:{p1.name}")
            p1.displayMonsterList()

        elif p2_length < p1_length:
            # 승자
            print(f"승자:{p1.name}")
            p1.displayMonsterList()

            # 패자
            print(f"패자:{p2.name}")
            p2.displayMonsterList()

        else:
            print("무승부")
            print(f"플레이어1:{p1.name}")
            p1.displayMonsterList()
            print(f"플레이어1:{p2.name}")
            p2.displayMonsterList()

        # TODO 5-1: 승자와 패자를 출력. 게임 종료 당시 남아있는 포켓몬의 리스트를 출력
        # return

    def playGame(self):
        play = False
        while not play:
            play = self.playRound()
        self.printFinalResult()


if __name__ == '__main__':
    # TODO 1: 게임 실행 -> 종료 시 새로운 게임 여부 확인 반복
    monsters_available = [Monster("A", 30, 100),
                          Monster("B", 30, 150),
                          Monster("C", 40, 300),
                          Monster("D", 50, 100),
                          Monster("E", 30, 150),
                          Monster("F", 30, 100),
                          Monster("G", 40, 300),
                          Monster("H", 50, 200),
                          Monster("I", 30, 250),
                          Monster("J", 20, 150)]
    
    card_type = [Card(3.0),
                 Card(1.5),
                 Card(2.0),
                 Card(1.4),
                 Card(0.2),
                 Card(0.3),
                 Card(2.5),
                 Card(1.7),
                 Card(1.5),
                 Card(0.8)]
    
    print(title_text)
    ui = UI(monsters_available, card_type)
    ui.startGame()
