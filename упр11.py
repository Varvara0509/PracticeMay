class Dessert:
    def __init__(self, name: str = "Unknown", calories: int = 0) -> None:
        self.__name = name
        self.__calories = int(calories)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def calories(self) -> int:
        return self.__calories

    @calories.setter
    def calories(self, value: int) -> None:
        self.__calories = value

    def is_healthy(self) -> bool:
        if isinstance(self.__calories, (int, float)) and self.__calories < 200:
            return True
        else:
            return False

    @staticmethod
    def is_delicious() -> bool:
        return True


def tests():
    while True:
        try:
            dessert_name_input = input("Введите название десерта: ")
            calories_input = int(input("Введите колличество калорий: "))
            if calories_input < 0:
                print("Значение калорий не может быть отрицательным.")
                break

            test = Dessert(name=dessert_name_input, calories=calories_input)

            print(test.name)
            print(test.calories)
            print(test.is_healthy())
            print(test.is_delicious())
            print()
        except EOFError:
            print("Получен EOF, ввод завершен.")
            break
        except ValueError:
            print("Значение калорий должно быть целочисленным.")
            break


def tests2():
    pass
    # >>>  dessert = Dessert()
    # >>>  dessert.name = “test_name”
    # >>>  print(dessert.name)
    # test_name
    # >>>  dessert.name = "test_name2"
    # >>>  print(dessert.name)
    # test_name2
    # >>>  if dessert.name != "test_name2": raise Exception("Setter for name is not working")
    # >>>  dessert.calories = "test_calories"
    # >>>  print(dessert.calories)
    # test_calories
    # >>>  dessert.calories = "test_calories2"
    # >>>  print(dessert.calories)
    # test_calories2
    # >>>  if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
    # >>>  print(dessert.is_delicious())
    # True
    # >>>  if not dessert.is_delicious(): raise Exception("Invalid method result")
    # >>>  print(dessert.is_healthy())
    # True
    # >>>  dessert.calories = 300
    # >>>  print(dessert.calories)
    # 300
    # >>>  print(dessert.is_healthy())
    # True
    # >>>  if dessert.is_healthy(): raise Exception("Logical error. Method must return False")

