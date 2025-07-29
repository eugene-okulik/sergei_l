class Flowers:

    def __init__(self, name, life_time, cost):
        self.name = name
        self.life_time = life_time
        self.cost = cost


class WhiteFlowers(Flowers):

    def __init__(self, name, life_time, cost):
        super().__init__(name, life_time, cost)
        self.color = 'белый'


class RedFlowers(Flowers):

    def __init__(self, name, life_time, cost):
        super().__init__(name, life_time, cost)
        self.color = 'красный'


class Bouquet:

    def __init__(self, *args):
        self.flower_list = list(args)

    def bouquet_cost(self):
        total_cost = [x.cost for x in self.flower_list]
        result = sum(total_cost)
        return f"Стоимость букета: {result} BYN"

    def bouquet_lifetime(self):
        lifetime_sum = [x.life_time for x in self.flower_list]
        result = sum(lifetime_sum) / len(lifetime_sum)
        return f"Время увядания букета: {round(result, 1)} дней"

    def sort_by_cost(self):
        flower_cost = [x.cost for x in self.flower_list]
        return sorted(flower_cost)

    def sort_by_color(self):
        flower_color = [x.color for x in self.flower_list]
        return sorted(flower_color)

    def find_by_color(self, color):
        flower_color = [x.name for x in self.flower_list if x.color == color]
        return f" {color.capitalize()} цветы в букете это {', '.join(flower_color)}"


flower1 = WhiteFlowers('Роза', 7, 13)
flower2 = RedFlowers('Орхидея', 5, 3.5)
flower3 = WhiteFlowers('Пион', 2, 7)

bouquet1 = Bouquet(flower1, flower2, flower3)

print(bouquet1.bouquet_lifetime())
print(bouquet1.bouquet_cost())
print(bouquet1.sort_by_cost())
print(bouquet1.sort_by_color())
print(bouquet1.find_by_color('красный'))
