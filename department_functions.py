def add_new_department():
    global dep
    global dep_id_counter
    dep = Department()
    dep.set_new_id()
    dep.set_dep_name()
    dep.set_dep_budget()
    dep.set_phone_number()
    department.append(dep)
    print(
        f"\nThe {dep.get_dep_name()} department with a budget of {dep.get_dep_budget()} was added.\n")


def list_department():
    global company_name
    print(f"\n{company_name} departments: \n")
    for e in department:
        print(e)
    print()