"""
Just a few examples.

:Author: Oscar Teixeira (@oskarbi)
"""

import querify

def run_select_examples():
    """SELECT statement generating example."""
    table = "customers"
    select_fields = ['name', 'last_name', 'age', 'country']
    select_conds = {}
    select_conds2 = {'id': 150}
    select_conds3 = {'id': 150, 'nombre': "oscar"}
    print querify.select_from_dict(table, select_fields)
    print querify.select_from_dict(table, select_fields, select_conds)
    print querify.select_from_dict(table, select_fields, select_conds2)
    print querify.select_from_dict(table, select_fields, select_conds3)

def run_insert_example():
    """INSERT statement generating example."""
    table = "customers"
    insert_values = {
        'id': 150,
        'name': "Oscar",
        'last_name': "Teixeira",
        'age': 42,
        'country': "Spain"}
    print querify.insert_from_dict(table, insert_values)

    insert_col_list = ["id", "name", "last_name", "age", "country"]
    insert_val_list = [
        [150, "Oscar", "Teixeira", 42, "Spain"],
        [150, "Oscar", "Teixeira", 42, "Spain"],
        [150, "Oscar", "Teixeira", 42, "Spain"]
        ]
    print querify.insert_from_list(table, insert_col_list, insert_val_list)

def run_update_example():
    """UPDATE statement generating example."""
    table = "customers"
    update_values = {
        'name': "Oscar",
        'last_name': "Teixeira Martin",
        'age': 43,
        'country': "Italy"}
    update_conds = {'id': 150}
    print querify.update_from_dict(table, update_values, update_conds)

def run_delete_example():
    """DELETE statement generating example."""
    table = "customers"
    delete_conds = {
        'name': "Oscar",
        'last_name': "Teixeira"}
    print querify.delete_from_dict(table, delete_conds)


if __name__ == "__main__":
    run_select_examples()
    run_insert_example()
    run_update_example()
    run_delete_example()
