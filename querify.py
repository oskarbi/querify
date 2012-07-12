"""
Super simple functions for generating SQL statments from Python built-in types.

:Author: Oscar Teixeira (@oskarbi)
"""

def generate_select(tablename, sel_fields, sel_conds=None):
    """Generate a SELECT statement.

    :param tablename: Table from which the row will be selected.
    :param sel_fields: List of fields to select.
    :param sel_conds: Dict of {col_name: value} for the WHERE clause.
    """
    sql = "%s %s %s" % (_generate_select_clause(sel_fields),
                       _generate_from_clause(tablename),
                       _generate_where_clause(sel_conds))
    return sql

def generate_insert(tablename, ins_values):
    """Generate an INSERT statement.

    :param ins_values: Dict of {col_name: value}
    :param tablename: Table where the row will be inserted.
    """
    sql = "%s %s;" % (_generate_insert_clause(tablename, ins_values),
                      _generate_values_clause(ins_values))
    return sql

def generate_update(tablename, updt_fields, updt_conds=None):
    """Generate an UPDATE statement.

    :param updt_fields: List of fields to select.
    :param updt_conds: Dict of {col_name: value} for the WHERE clause.
    :param tablename: Table from which the row will be selected.
    """
    sql = "%s %s %s" % (_generate_update_clause(tablename),
                       _generate_set_clause(updt_fields),
                       _generate_where_clause(updt_conds))
    return sql

def generate_delete(tablename, del_conds=None):
    """Generate a DELETE statement.
    :param tablename: Table from which the row will be deleted.
    :param del_conds: Dict of {col_name: value} for the WHERE clause.
    """
    sql = "%s %s" % (_generate_delete_clause(tablename),
                    _generate_where_clause(del_conds))
    return sql

def _generate_select_clause(select_field_list):
    """Generate a SELECT clause from a list of fields to select."""
    select_clause = "SELECT " + ", ".join([x for x in select_field_list])
    return select_clause

def _generate_insert_clause(tablename, ins_values):
    """Generate an INSERT statement"""
    insert_itr = [x for x in ins_values]
    insert_clause = "INSERT INTO %s(%s)" % (
        tablename,
        ", ".join(insert_itr))
    return insert_clause

def _generate_update_clause(tablename):
    """Generate an UPDATE clause."""
    update_clause = "UPDATE %s SET" % tablename
    return update_clause

def _generate_delete_clause(tablename):
    """Generate an DELETE clause."""
    delete_clause = "DELETE FROM %s" % tablename
    return delete_clause

def _generate_from_clause(tablename):
    """Generate a FROM clause from a table name."""
    from_clause = "FROM %s" % tablename
    return from_clause

def _generate_where_clause(conditions_dict=None):
    """Generate a WHERE clause from a dict of fields and values."""
    if not conditions_dict:
        return ";"
    where_itr = ["%s = %s" %
        (x, _format_value(conditions_dict[x])) for x in conditions_dict]
    where_clause = "WHERE %s;" % " AND ".join(where_itr)
    return where_clause

def _generate_values_clause(ins_values):
    """Generate a VALUES clause to use include in an INSERT statement."""
    values_itr = [_format_value(ins_values[x]) for x in ins_values]
    values_clause = "VALUES (%s)" % ", ".join(values_itr)
    return values_clause

def _generate_set_clause(updt_fields):
    """Generate a SET clause to use include in an UPDATE statement."""
    set_itr = ["%s = %s" %
        (x, _format_value(updt_fields[x])) for x in updt_fields]
    set_clause = ", ".join(set_itr)
    return set_clause

def _format_value(raw_value):
    """Format a given value for embebing it in the SQL statement."""
    if type(raw_value) == float or type(raw_value) == int:
        return str(raw_value)
    return "'%s'" % raw_value
