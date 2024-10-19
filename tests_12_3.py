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
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @staticmethod
    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            else:
                func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @staticmethod
    def skip_if_frozen(func):
        def wrapper(self, *args, **kwargs):
            if self.is_frozen:
                self.skipTest("Тесты в этом кейсе заморожены")
            else:
                func(self, *args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, Runner("Usain", speed=10), Runner("Nick", speed=3))
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Nick")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, Runner("Andrey", speed=9), Runner("Nick", speed=3))
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Nick")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, Runner("Usain", speed=10), Runner("Andrey", speed=9), Runner("Nick", speed=3))
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == "Nick")
