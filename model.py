class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self.title = title
        self.price_code = price_code

    def title(self) -> str:
        return self.title

    def price_code(self) -> int:
        return self.price_code


class Rental:
    def __init__(self, book: Book, days_rented: int):
        self.book = book
        self.days_rented = days_rented

    def book(self) -> Book:
        return self.book

    def days_rented(self) -> int:
        return self.days_rented

    def get_charge(self) -> float:
        amount = 0
        if self.book.price_code == Book.REGULAR:
            amount += 2
            if self.days_rented > 2:
                amount += (self.days_rented - 2) * 1.5
        elif self.book.price_code == Book.NEW_RELEASE:
            amount += self.days_rented * 3
        elif self.book.price_code == Book.CHILDREN:
            amount += 1.5
            if self.days_rented > 3:
                amount += (self.days_rented - 3) * 1.5
        return amount

    def get_frequent_renter_points(self) -> int:
        points = 1
        if self.book.price_code == Book.NEW_RELEASE and self.days_rented > 1:
            points += 1
        return points


class Client:

    def __init__(self, name: str):
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def name(self) -> str:
        return self.name

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"

        for rental in self.rentals:
            amount = rental.get_charge()
            frequent_renter_points += rental.get_frequent_renter_points()
            result += f"- {rental.book.title}: {amount}\n"
            total_amount += amount

        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result
