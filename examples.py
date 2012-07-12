"""
Just a few examples.

:Author: Oscar Teixeira (@oskarbi)
"""

import querify

def run_select_examples():
    """SELECT statement generating example."""
    table = "actors"
    select_fields = ['name', 'last_name', 'country']
    select_conds1 = {}
    select_conds2 = {'id': 3}
    select_conds3 = {'id': 3, 'name': "Matt"}
    print querify.select_from_dict(table, select_fields)
    print querify.select_from_dict(table, select_fields, select_conds1)
    print querify.select_from_dict(table, select_fields, select_conds2)
    print querify.select_from_dict(table, select_fields, select_conds3)

def run_insert_example():
    """INSERT statement generating example."""
    table = "actors"
    insert_values = {
        'id': 3,
        'name': "Matt",
        'last_name': "Smith",
        'country': "England"}
    print querify.insert_from_dict(table, insert_values)

    insert_col_list = ["id", "name", "last_name", "country"]
    insert_val_list = [
        [1, "Chris", "Eccleston", "England"],
        [2, "David", "Tennant", "Scotland"],
        [3, "Matt", "Smith", "England"]]
    print querify.insert_from_list(table, insert_col_list, insert_val_list)

def run_update_example():
    """UPDATE statement generating example."""
    table = "actors"
    update_values = {
        'name': "Christopher",
        'last_name': "Eccleston"}
    update_conds = {'id': 1}
    print querify.update_from_dict(table, update_values, update_conds)

def run_delete_example():
    """DELETE statement generating example."""
    table = "actors"
    delete_conds = {
        'name': "Matt",
        'last_name': "Smith"}
    print querify.delete_from_dict(table, delete_conds)


if __name__ == "__main__":
    run_select_examples()
    run_insert_example()
    run_update_example()
    run_delete_example()
