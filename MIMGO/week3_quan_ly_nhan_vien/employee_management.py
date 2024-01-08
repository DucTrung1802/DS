import os
from enum import Enum


class Roles(Enum):
    STAFF = 1
    TECHNICIAN = 2
    EXPERT = 3


class employee:
    __working_hours_thresholds: list = [0, 100, 200]
    __working_hours_bonus_thresholds: list = [0, 10, 20]
    __exp_thresholds: list = [0, 2, 5]
    __exp_bonus_thresholds: list = [0, 25, 50]
    __income_rate_thresholds: list = [0, 1.2, 1.5, 2]

    def __init__(
        self,
        name: str,
        age: int,
        address: str,
        role: str,
        basic_salary: float,
        exp: int,
        working_hours: int,
    ):
        self.name: str = name
        self.age: int = age
        self.address: str = address
        self.role: str = role
        self.basic_salary: float = basic_salary
        self.exp: int = exp
        self.working_hours: int = working_hours

    def get_bonus(self):
        self.__overtime_bonus = 0
        self.__exp_bonus = 0

        # Overtime bonus
        if (
            self.__working_hours_thresholds[0]
            <= self.working_hours
            <= self.__working_hours_thresholds[1]
        ):
            self.__overtime_bonus = (
                self.basic_salary * self.__working_hours_bonus_thresholds[0]
            )
        elif (
            self.__working_hours_thresholds[1]
            < self.__working_hours
            <= self.__working_hours_thresholds[2]
        ):
            self.__overtime_bonus = (
                self.basic_salary * self.__working_hours_bonus_thresholds[1]
            )
        elif self.__working_hours_thresholds[2] < self.__working_hours:
            self.__overtime_bonus = (
                self.basic_salary * self.__working_hours_bonus_thresholds[2]
            )

        # Exp bonus
        if self.__exp_thresholds[0] <= self.working_hours <= self.__exp_thresholds[1]:
            self.__exp_bonus = self.basic_salary * self.__exp_bonus_thresholds[0]
        elif (
            self.__exp_thresholds[1] < self.__working_hours <= self.__exp_thresholds[2]
        ):
            self.__exp_bonus = self.basic_salary * self.__exp_bonus_thresholds[1]
        elif self.__exp_thresholds[2] < self.__working_hours:
            self.__exp_bonus = self.basic_salary * self.__exp_bonus_thresholds[2]

        return self.__overtime_bonus + self.__exp_bonus

    def get_income(self):
        self.__role_income = 0
        if self.role == Roles.EXPERT:
            self.__role_income = self.basic_salary * self.__income_rate_thresholds[3]
        elif self.role == Roles.TECHNICIAN:
            self.__role_income = self.basic_salary * self.__income_rate_thresholds[2]
        elif self.role == Roles.STAFF and (self.exp > 3):
            self.__role_income = self.basic_salary * 1.2
        elif self.role == Roles.STAFF and (0 <= self.exp <= 3):
            self.__role_income = self.basic_salary

        return self.__role_income + self.get_bonus()

    def __str__(self):
        return (
            self.name
            + "; "
            + str(self.age)
            + "; "
            + self.address
            + "; "
            + self.role
            + "; "
            + str(self.exp)
            + "; "
            + str(self.basic_salary)
            + "; "
            + str(self.working_hours)
        )


class employee_management:
    

    def __init__(self):
        self.__format_steps = 5
        self.employees = self.read_data("employee_input.txt")

    def print_infos(self):
        for i in range(len(self.employees)):
            print(self.employees[i])

    def read_data(self, file_name):
        """
        Form of .txt file

        name
        age
        address
        role exp working_hours
        basic_salary

        """

        if not os.path.isfile(file_name):
            raise Exception('File "{}" does not exist!'.format(file_name))

        with open(file_name, "r") as f:
            contents = f.readlines()
            for i in range(0,len(contents),self.__format_steps):
                name = contents[i].rstrip()
                print(name)



    def sort_by_income(self):
        pass

    def get_max_income(self, employee1):
        pass


employee_management_system = employee_management()
