class Employee:
    def __init__(self, name, id, department, job_title):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title

    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return f'Employee({self.__name}, {self.__department}, {self.__job_title})'