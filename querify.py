"""
Module for generating simple SQL statements from Python built-in types.

:Author: Oscar Teixeira (@oskarbi)
"""

def select_from_dict(tablename, sel_fields, sel_conds=None):
    """Generate a SELECT statement.

    :param tablename: Table from which the row will be selected.
    :param sel_fields: List of fields to select.
    :param sel_conds: Dict of {col_name: value} for the WHERE clause.
    """
    sql_query = "%s %s %s" % (__select_clause(sel_fields),
                              __from_clause(tablename),
                              __where_clause(sel_conds))
    return sql_query

def insert_from_dict(tablename, ins_values):
    """Generate an INSERT statement.

    :param tablename: Table where the row will be inserted.
    :param ins_values: Dict of {col_name: value}
    """
    sql_query = "%s %s;" % (__insert_clause(tablename, ins_values),
                            __values_clause(ins_values))
    return sql_query

def insert_from_list(tablename, ins_fields, ins_values):
    """Generate an INSERT statement.

    :param tablename: Table where the row will be inserted.
    :param ins_fields: List of fields where the values will be inserted.
    :param ins_values: List of lists of values to insert.
    """
    sql_query = "%s %s;" % (__insert_clause(tablename, ins_fields),
                            __values_clause_2(ins_values))
    return sql_query

def update_from_dict(tablename, updt_fields, updt_conds=None):
    """Generate an UPDATE statement.

    :param tablename: Table from which the row will be selected.
    :param updt_fields: List of fields to select.
    :param updt_conds: Dict of {col_name: value} for the WHERE clause.
    """
    sql_query = "%s %s %s" % (__update_clause(tablename),
                              __set_clause(updt_fields),
                              __where_clause(updt_conds))
    return sql_query

def delete_from_dict(tablename, del_conds=None):
    """Generate a DELETE statement.

    :param tablename: Table from which the row will be deleted.
    :param del_conds: Dict of {col_name: value} for the WHERE clause.
    """
    sql_query = "%s %s" % (__delete_clause(tablename),
                           __where_clause(del_conds))
    return sql_query

def __select_clause(select_field_list):
    """Generate a SELECT clause, given a list of fields."""
    select_clause = "SELECT " + ", ".join([x for x in select_field_list])
    return select_clause

def __insert_clause(tablename, ins_values):
    """Generate an INSERT clause, given a table name and a list of fields."""
    insert_itr = [x for x in ins_values]
    insert_clause = "INSERT INTO %s(%s)" % (
        tablename,
        ", ".join(insert_itr))
    return insert_clause

def __update_clause(tablename):
    """Generate an UPDATE clause, given a table name."""
    update_clause = "UPDATE %s SET" % tablename
    return update_clause

def __delete_clause(tablename):
    """Generate a DELETE clause, given a table name."""
    delete_clause = "DELETE FROM %s" % tablename
    return delete_clause

def __from_clause(tablename):
    """Generate a FROM clause, given a table name."""
    from_clause = "FROM %s" % tablename
    return from_clause

def __where_clause(conditions_dict=None):
    """Generate a WHERE clause, given a dict of fields and values."""
    if not conditions_dict:
        return ";"
    where_itr = ["%s = %s" %
        (x, __format_value(conditions_dict[x])) for x in conditions_dict]
    where_clause = "WHERE %s;" % " AND ".join(where_itr)
    return where_clause

def __values_clause(ins_values):
    """Generate a VALUES clause to use include in an INSERT statement."""
    # TODO: Deprecated?
    values_itr = [__format_value(ins_values[x]) for x in ins_values]
    values_clause = "VALUES (%s)" % ", ".join(values_itr)
    return values_clause

def __values_clause_2(ins_values):
    """Generate a VALUES clause to use include in an INSERT statement."""
    values_clause = "VALUES (%s)" % "), (".join(
        [", ".join([__format_value(x) for x in y]) for y in ins_values])
    return values_clause

def __set_clause(updt_fields):
    """Generate a SET clause to use include in an UPDATE statement."""
    set_itr = ["%s = %s" %
        (x, __format_value(updt_fields[x])) for x in updt_fields]
    set_clause = ", ".join(set_itr)
    return set_clause

def __format_value(raw_value):
    """Format a given value for embebing it in the SQL statement."""
    if type(raw_value) == float or type(raw_value) == int:
        return str(raw_value)
    return "'%s'" % raw_value
