def foo(x):
    #받은 인자의 type이 정수형인지 검사 
    assert type(x) == int, "Input value must be integer"
    return x * 10


ret = foo("a")  #AssertError 발생
print(ret)
