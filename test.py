def hello_world():
    my_value = 1
    sql = f""" select * from tb_greeting """
    sql = f""" insert into tb_greeting (index) value (1) """
    sql = " select * FROM me"
    sql = f" select * FROM me "
    sql = f"select * FROM me "
    sql = "select * FROM me "
    sql = f""" insert into tb_greeting (index) value ({my_value}) 
    """
    sql = f"""
    insert into tb_greeting (index) value (1) 
    """
    sql = """
    insert into tb_greeting (index) value (1) 
    """
    
    return "ok"