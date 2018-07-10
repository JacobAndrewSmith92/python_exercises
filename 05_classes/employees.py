class Company(object):
    # This represents a company in which people work

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def all_employees(self):
        employee_list = list()
        for employee in self.employees:
            employee_list.append(employee.name)

        return employee_list

    def hire_employees(self, employee, start_date):
        self.employees.extend([employee])
        employee.new_job(self, start_date)


    def remove_employees(self, employee):
        if(employee in self.employees):
            self.employees.remove(employee)

    def __str__(self):
        return f"{self.company_name} est.{self.date_founded}"
    # Add the remaining methods to fill the requirements above


class Employee(object):

    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
        self.start_date = None
        self.company = None


    def get_job_title(self):
        return self.job_title

    def new_job(self, new_company, start_date):
        if(self.company is None):
            self.company = new_company
            self.start_date = start_date
        else:
            self.ditch_old_job()
            self.company = new_company

    def ditch_old_job(self):
        self.company.remove_employees(self)

# Create Companies

the_north_face = Company("The North Face", "1968")
patagonia = Company("Patagonia", "1970")

# Hired Employees

sean = Employee("Sean", "Python Developer")
cole = Employee("Cole", "Javascript Developer")
jacob = Employee("Jacob", "Javascript Developer")

patagonia.hire_employees(cole, "07-06-2018")
the_north_face.hire_employees(sean, "07-06-2018")
the_north_face.hire_employees(jacob, "07-06-2018")


print(jacob.start_date)
print(the_north_face.all_employees())


