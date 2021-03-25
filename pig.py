import random
random.seed(0)
from time import sleep


class Scorecard:
    def __init__(self):
        self.point_counter = 0


class Player:
  def __init__(self):
    self.total_points = Scorecard()


class Dice:
    def roll_dice(self):
        self.roll_outcome = random.randint(1, 6)
        return self.roll_outcome


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.single_die = Dice()
    
    def player_turn(self):
        self.turn_total = 0
        self.player_input = 'r'
        while self.player_input == 'r':
            self.current_roll = self.single_die.roll_dice()
            if self.current_roll == 1:
                print('Rolling...')
                sleep(2)
                print('Shucks, you rolled a 1.')
                sleep(2)
                self.turn_total = 0
                self.player_input = 'h'
            else:
                print('Rolling...')
                sleep(2)
                print('You rolled a {}.'.format(self.current_roll))
                self.turn_total += self.current_roll
                sleep(2)
                print('You have accumulated {} points this turn.'.format(self.turn_total))
                sleep(2)
                self.player_input = input('Enter r to roll or h to hold: ')
        print('Your turn is now over.')
        sleep(2)
        return self.turn_total

    def play_game(self):
        while ((self.player1.total_points.point_counter < 100) and (self.player2.total_points.point_counter < 100)):
            print('Player1 total score: {}'.format(self.player1.total_points.point_counter))
            sleep(2)
            self.player1.total_points.point_counter += self.player_turn()
            print('Player1 total score: {}'.format(self.player1.total_points.point_counter))
            sleep(2)
            if self.player1.total_points.point_counter < 100:
                print('Player2 total score: {}'.format(self.player2.total_points.point_counter))
                sleep(2)
                self.player2.total_points.point_counter += self.player_turn()
                print('Player2 total score: {}'.format(self.player2.total_points.point_counter))
                sleep(2)
        if (self.player1.total_points.point_counter) > (self.player2.total_points.point_counter):
            print('Player1 wins!')
        else:
            print('Player2 wins!')


def begin_game():
    print( 'Welcome to Pig! This is a 2 player game.')
    sleep(2)
    

def play_game():
    game_session = Game()
    game_session.play_game()


def end_game():
    print('Exiting Pig... Goodbye!')
    sleep(2)


def main():
    begin_game()
    play_game()
    end_game()


if __name__ == "__main__":
    main()
    
