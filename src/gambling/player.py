from .cards import Card
from .roulette import Number


class Player(object):
    """
    Base Player class
    """

    def __init__(self, wallet: float, name: str = None):
        self.wallet = wallet
        self.name = name

    def __add__(self, other: float):
        self.wallet += other

    def __sub__(self, other: float):
        self.wallet -= other

    def __str__(self):
        return f'{self.name or f"Player with ${self.wallet}"}'

    def __repr__(self):
        return f'Player({self.name}, ${self.wallet})'


class CardPlayer(Player):
    """
    Card Player class for the main Player class
    """

    def __init__(self, wallet: float):
        super().__init__(wallet)
        self.hand = []

    def new_card(self, card: Card):
        self.hand.append(card)

    def new_hand(self):
        self.hand = []


# --- Bets ---


class Bet(object):
    def __init__(self, player: Player, amount):
        self.odds = 1
        self.player = player
        self.amount = amount
        self.is_winner = False
        self.is_complete = False
        self.is_paid = False
        self.amount_paid = 0
        self.charge_bet()

    def charge_bet(self):
        self.player - self.amount

    def pay_winner(self):
        if not self.is_paid and self.is_winner:
            self.amount_paid = self.amount * (self.odds + 1)
            self.player + self.amount_paid
            self.is_paid = True


class StraightRouletteBet(Bet):
    """
    A bet on a specific number
    """
    def __init__(self,  player: Player, amount: float, number: Number):
        super().__init__(player, amount)
        self.number = number
        self.odds = 35

    def check_win(self, winning_number: Number):
        """Changes the bet.is_winner class to True and pays the bet"""
        if self.number.value == winning_number.value:
            self.is_winner = True
            self.pay_winner()


class ColorRouletteBet(Bet):
    """
    A bet on a color 'red' or 'black'
    """
    def __init__(self, player: Player, amount: float, color: str):
        super().__init__(player, amount)
        self.color = color

    def check_win(self, winning_number: Number):
        """Changes the bet.is_winner class to True and pays the bet"""
        if winning_number.is_red and self.color == 'red':
            self.is_winner = True
            self.pay_winner()
        elif winning_number.is_black and self.color == 'black':
            self.is_winner = True
            self.pay_winner()
