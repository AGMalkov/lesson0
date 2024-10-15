import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", speed=10)
        self.andrew = Runner("Andrew", speed=9)
        self.nick = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            result_with_names = {place: str(runner) for place, runner in value.items()}
            print(result_with_names)

    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results['test_usain_nick'] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_andrew_nick(self):
        tournament = Tournament(90, self.andrew, self.nick)
        result = tournament.start()
        self.__class__.all_results['test_andrew_nick'] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

    def test_usain_andrew_nick(self):
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        result = tournament.start()
        self.__class__.all_results['test_usain_andrew_nick'] = result
        self.assertTrue(result[max(result.keys())] == "Nick")

if __name__ == '__main__':
    unittest.main()
