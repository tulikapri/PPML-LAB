def employee(**default):
    for k,v in default.items():
        print(k,":",v)
        employee(name="Kiran",id=101,dept="IT")