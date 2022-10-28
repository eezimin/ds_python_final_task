import click
import random
from typing import Callable


class Pizza:
    def __init__(self, size: str = 'L'):
        self.size = size
        self.ingredients = None
        self.name = None

    def __str__(self) -> str:
        return 'One of the Best Pizzas in the World!'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Pizza):
            raise TypeError("You must provide a Class object of Pizza\
                            on the right-hand side of the '=' operator")
        return self.ingredients == other.ingredients

    def dict(self):
        """Returns the name of pizza and its ingredients."""
        return f'{self.name}: {self.ingredients}'


class Margherita(Pizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.name = '🧀 Margherita'
        self.ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']


class Pepperoni(Pizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.name = '🍕 Pepperoni'
        self.ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']


class Hawaiian(Pizza):
    def __init__(self, size='L'):
        super().__init__(size)
        self.name = '🍍 Hawaiian'
        self.ingredients = ['tomato sauce', 'mozzarella',
                            'chicken', 'pineapples']


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool):
    """Returns the time during which the order was delivered."""
    print(f'🍳 Приготовили {pizza} за {random.randint(1, 10)}с!')
    if delivery:
        print(f'🛵 Доставили {pizza} за {random.randint(1, 10)}с!')


@cli.command()
def menu():
    """Returns menu of all available pizzas and their ingredients."""
    di = {
        '— Margherita 🧀': ['tomato sauce', 'mozzarella', 'tomatoes'],
        '— Pepperoni 🍕': ['tomato sauce', 'mozzarella', 'pepperoni'],
        '— Hawaiian 🍍': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    }
    for key, value in di.items():
        print(f'{key}: {", ".join(value)}')


def log(tag: str) -> Callable:
    def outer_wrapper(func: Callable) -> Callable:
        def inner_wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return tag.format(result)
        return inner_wrapper
    return outer_wrapper


@log('🍳 Приготовили за {}с!')
def bake() -> float:
    """Returns the time during which the pizza was baked."""
    return random.randint(1, 10)


@log('🛵 Доставили за {}с!')
def delivery(pizza) -> float:
    """Returns the time during which the pizza was delivered."""
    return random.randint(1, 10)


@log('🏠 Забрали за {}с!')
def pickup(pizza) -> float:
    """Returns the time during which the pizza was picked up."""
    return random.randint(1, 10)


if __name__ == '__main__':
    # print(Margherita().dict())
    # print(Pepperoni().dict())
    # print(Hawaiian().dict())
    # print(Margherita('XL').size)
    # print(Margherita().ingredients)
    # print(Margherita() == Pepperoni())
    # print(isinstance(Margherita(), Pizza))
    # print(delivery(Margherita()))
    # print(pickup(Margherita()))
    cli()
