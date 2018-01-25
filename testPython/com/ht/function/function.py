from com.ht.function import support
def printme(parmeter):
    #"答应传入的字符串"
    print (parmeter);
    return;
printme("我调用了你");
a=[1,2,3];
a="runoob";
def printArgShunxu(name,*age):
    print(name);
    for i in age:
        print(i);

printArgShunxu("xyz","123","1234");
def printreturnArg(arg0,arg1):
    total=arg0+arg1;
    return total;
print(printreturnArg(10, 20));
print(support.print_func(name="xyz"));sum=lambda arg1,arg2:arg1+arg2;
print(sum(1,2));
