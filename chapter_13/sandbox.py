from typing import Generic, TypeVar


class Beverage:
    """Any beverage"""


class Juice(Beverage):
    "Any fruit juice"


class OrangeJuice(Juice):
    """Orange juice"""


T = TypeVar("T", covariant=True)


class BeverageDispenser(Generic[T]):
    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Install juice dispenser"""


juice_dispenser = BeverageDispenser(OrangeJuice())
install(juice_dispenser)