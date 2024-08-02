class Employee:
    def __init__(self, first_name, last_name, birth_year) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        #self._password = password
        #self._salary = salary

    def show(self):
        print('''I am {self.first_name} {self.last_nanme} born in {self.birth_day}''')


'''
Some old code...
    @property
    def name(self):
        return self._name
    
    @property
    def password(self):
        raise AttributeError('Access Denied')
                             
    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary
    
    
'''
