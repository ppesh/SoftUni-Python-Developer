from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.main_hero = Hero("MainHero", 5, 100, 10)
        self.second_hero = Hero("SecondHero", 10, 80, 20)

    def test_hero__initialized(self):
        self.assertEqual("MainHero", self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_hero__battle_raises_if_fight_self(self):
        hero_self = Hero("MainHero", 6, 80, 10)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(hero_self)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero__health_is_zero(self):
        self.main_hero.health = 0
        self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero__hero_health_is_less_than_zero(self):
        self.main_hero.health = -5
        self.assertEqual(-5, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_hero__enemy_health_is_less_than_zero(self):
        self.second_hero.health = -5
        self.assertEqual(-5, self.second_hero.health)
        self.assertEqual(100, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.second_hero)
        self.assertEqual("You cannot fight SecondHero. He needs to rest", str(ex.exception))

    def test_hero__battle_draw_case(self):
        # Bring down enemy hero to 50 so that it could be equal to the damage of main hero
        self.second_hero.health = 50
        result = self.main_hero.battle(self.second_hero)
        self.assertEqual("Draw", result)

    def test_hero__main_hero_wins(self):
        self.main_hero.damage = 200
        self.main_hero.health = 300
        result = self.main_hero.battle(self.second_hero)
        self.assertEqual("You win", result)
        self.assertEqual(205, self.main_hero.damage)
        self.assertEqual(6, self.main_hero.level)
        self.assertEqual(105, self.main_hero.health)

    def test_hero__enemy_wins(self):
        result = self.main_hero.battle(self.second_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(35, self.second_hero.health)
        self.assertEqual(25, self.second_hero.damage)
        self.assertEqual(11, self.second_hero.level)
        self.assertTrue(self.main_hero.health < 0)

    def test_hero__str_representation(self):
        self.assertEqual("Hero MainHero: 5 lvl\nHealth: 100\nDamage: 10\n", str(self.main_hero))
        # result = str(self.main_hero).split("\n")
        # self.assertEqual("Hero MainHero: 5 lvl", result[0])
        # self.assertEqual("Health: 100", result[1])
        # self.assertEqual("Damage: 10", result[2])


if __name__ == "__main__":
    main()
