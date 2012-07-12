"""
Just a few examples.

:Author: Oscar Teixeira (@oskarbi)
"""

import querify

def run_select_example():
    """SELECT statement generating example."""
    table = "customers"
    select_fields = ['name', 'last_name', 'age', 'country']
    select_conds = {}
    select_conds2 = {'id': 150}
    select_conds3 = {'id': 150, 'nombre': "oscar"}
    print querify.generate_select(table, select_fields)
    print querify.generate_select(table, select_fields, select_conds)
    print querify.generate_select(table, select_fields, select_conds2)
    print querify.generate_select(table, select_fields, select_conds3)

def run_insert_example():
    """INSERT statement generating example."""
    table = "customers"
    insert_values = {
        'id': 150,
        'name': "Oscar",
        'last_name': "Teixeira",
        'age': 42,
        'country': "Spain"}
    print querify.generate_insert(table, insert_values)

def run_update_example():
    """UPDATE statement generating example."""
    table = "customers"
    update_values = {
        'name': "Oscar",
        'last_name': "Teixeira Martin",
        'age': 43,
        'country': "Italy"}
    update_conds = {'id': 150}
    print querify.generate_update(table, update_values, update_conds)

def run_delete_example():
    """DELETE statement generating example."""
    table = "customers"
    delete_conds = {
        'name': "Oscar",
        'last_name': "Teixeira"}
    print querify.generate_delete(table, delete_conds)


if __name__ == "__main__":
    run_select_example()
    run_insert_example()
    run_update_example()
    run_delete_example()
