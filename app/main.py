from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self._health = max(0, health)
        self.hidden = hidden

        if self._health > 0:
            self.__class__.alive.append(self)

    # --- Health property ---
    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, value)
        if self._health == 0:
            self.die()

    # --- Death handling ---
    def die(self) -> None:
        if self in self.__class__.alive:
            self.__class__.alive.remove(self)

    # --- Pretty print for single animal ---
    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if isinstance(animal, Herbivore) and not animal.hidden:
            animal.health -= 50
