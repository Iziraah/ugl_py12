# Создайте класс студента.
#   Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
#   Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
#   Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
#   Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых. 


import csv

with open('productivity.csv', 'w', newline='') as csvfile:
    descip_writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    descip_writer.writerow(
        ['painting', 'drawing', 'composition',
         'art_history', 'materials_science']
        )
    
with open('productivity_test.csv', 'w', newline='') as csvfile:
    descip_writer = csv.writer(csvfile, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
    descip_writer.writerow(
        ['painting_test', 'drawing_test', 'composition_test', 
         'art_history_test', 'materials_science_test']
        )

class Name_test:
    def __init__(self, param):
        self.param = param
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    def validate(self, value):
            if self.param(value) != True:
                raise ValueError(f'Где-то в имени ошибка...')
        
class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    def validate(self, value):
        for i in range(len(value)):
            if self.min_value is not None and value[i] < self.min_value:
                raise ValueError(f'Значение {value[i]} должно быть больше 18 или равно {self.min_value}')
            if self.max_value is not None and value[i] >= self.max_value:
                raise ValueError(f'Значение {value[i]} должно быть меньше {self.max_value}')  
        
class Student:
    first_name = Name_test(str.istitle) and Name_test(str.isalpha)
    last_name = Name_test(str.istitle and str.isalpha)
    productivity = Range(2, 5+1)
    productivity_t = Range (0, 100+1)
    
    def __init__(self, first_name, last_name, productivity, productivity_t) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.productivity = productivity
        self.productivity_t = productivity_t
    
    def Get_Productivity(filename):
        # productivity_print = {}
        discip = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=' ')
            for row in reader:
                discip.append(row)          
        descipline = discip[0]
        return descipline
        
    def __str__(self):
        def Get_Productivity(filename):
            discip = []
            with open(filename) as csvfile:
                reader = csv.reader(csvfile, delimiter=' ')
                for row in reader:
                    discip.append(row)          
            descipline = discip[0]
            return descipline
        productivity_print = {}        
        productivity_print_t = {}
        descipline = Get_Productivity('productivity.csv')    
        descipline_t = Get_Productivity('productivity_test.csv')           
        for k in range(len(descipline)):
            productivity_print.update({descipline[k]: self.productivity[k]})
        for k in range(len(descipline_t)):
            productivity_print_t.update({descipline_t[k]: self.productivity_t[k]})
        return f"{self.first_name} {self.last_name}: \n {productivity_print} \n {productivity_print_t}"
    
    def get_average(self):
        sum_p = 0
        sum_p_test = 0
        for i in range(len(self.productivity)):
            sum_p += self.productivity[i]
        sum_p = sum_p/5
        for i in range(len(self.productivity_t)):
            sum_p_test += self.productivity_t[i]
        sum_p_test = sum_p_test/5
        return f'Средний былл по дисциплинам: {sum_p} \n' + f"Средний балл по тестам: {sum_p_test}"
    


        
if __name__ == '__main__':
    
    st1 = Student('Anna', 'Bair', [2,3,5,3,4], [50,56,78,45,12])
    print(st1)
    prod1 = st1.get_average()
    print(prod1)
    st2 = Student('Lex', 'Smoky', [4,3,5,4,5], [78,67,79,97,98])
    print(st2)
    prod2 = st2.get_average()
    print(prod2)

