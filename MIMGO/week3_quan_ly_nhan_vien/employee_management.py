import os
from enum import Enum


class Roles(Enum):
    STAFF = "staff"
    TECHNICIAN = "technician"
    EXPERT = "expert"


class employee:
    __working_hours_thresholds: list = [0, 100, 200]
    __working_hours_bonus_thresholds: list = [0, 0.1, 0.2]
    __exp_thresholds: list = [0, 2, 5]
    __exp_bonus_thresholds: list = [0, 0.25, 0.50]
    __income_rate_thresholds: list = [0, 1.2, 1.5, 2.0]

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
            < self.__working_hours_thresholds[1]
        ):
            self.__overtime_bonus = (
                self.basic_salary * self.__working_hours_bonus_thresholds[0]
            )
        elif (
            self.__working_hours_thresholds[1]
            <= self.working_hours
            <= self.__working_hours_thresholds[2]
        ):
            self.__overtime_bonus = (
                self.basic_salary * self.__working_hours_bonus_thresholds[1]
            )
        elif self.__working_hours_thresholds[2] < self.working_hours:
            self.__overtime_bonus = (
                self.basic_salary * self.__working_hours_bonus_thresholds[2]
            )

        # Exp bonus
        if self.__exp_thresholds[0] <= self.exp < self.__exp_thresholds[1]:
            self.__exp_bonus = self.basic_salary * self.__exp_bonus_thresholds[0]
        elif self.__exp_thresholds[1] <= self.exp <= self.__exp_thresholds[2]:
            self.__exp_bonus = self.basic_salary * self.__exp_bonus_thresholds[1]
        elif self.__exp_thresholds[2] < self.exp:
            self.__exp_bonus = self.basic_salary * self.__exp_bonus_thresholds[2]

        return self.__overtime_bonus + self.__exp_bonus

    def get_income(self):
        self.__role_income = 0
        if self.role == Roles.EXPERT:
            self.__role_income = self.basic_salary * self.__income_rate_thresholds[3]
        elif self.role == Roles.TECHNICIAN:
            self.__role_income = self.basic_salary * self.__income_rate_thresholds[2]
        elif self.role == Roles.STAFF and (self.exp >= 3):
            self.__role_income = self.basic_salary * 1.2
        elif self.role == Roles.STAFF and (0 <= self.exp < 3):
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
            employee_list = []
            self.roles = [member.value for member in Roles]
            contents = f.readlines()
            for i in range(0, len(contents), self.__format_steps):
                name = str(contents[i].rstrip())
                age = int(contents[i + 1].rstrip())
                address = str(contents[i + 2].rstrip())
                temp = contents[i + 3].rstrip().split()
                role = str(temp[0]).lower()
                if role not in self.roles:
                    raise Exception("Role '{}' does not exist!".format(role))
                exp = int(temp[1])
                working_hours = int(temp[2])
                basic_salary = float(contents[i + 4])
                employee_list.append(
                    employee(name, age, address, role, basic_salary, exp, working_hours)
                )
            return employee_list

    def sort_by_income(self):
        self.employees = sorted(self.employees, key=lambda x: x.basic_salary)

    def get_max_income(self, employee1: employee):
        same_role_list = [emp for emp in self.employees if emp.role == employee1.role]
        max_income_employee: employee = max(
            same_role_list, key=lambda x: x.get_income()
        )
        return max_income_employee.get_income()


# employee_management_system = employee_management()
# # employee_management_system.print_infos()

# employee_management_system.sort_by_income()
# employee_management_system.print_infos()

# test_employee = employee("Trung", "23", "Ha Noi", "staff", 1000000, 1, 100)
# print(employee_management_system.get_max_income(test_employee))
