class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    def get_name(self):
        return self._name

    def get_bill_amount(self):
        return self._bill_amount

    def set_name(self, name):
        self._name = name

    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self):
        return self._bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.80


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.85