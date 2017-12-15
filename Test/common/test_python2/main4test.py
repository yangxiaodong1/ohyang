import os


def execute_python2(python2path, name, args1, args2, args3):
    return os.popen(python2path + " " + name + ".py " + args1 + " " + args2 + " " + args3)


python2path = r"C:\Python27\python"
name = "py2test"
args1 = "test1"
args2 = "test2"
args3 = "test3"
content = execute_python2(python2path, name, args1, args2, args3)
print(content.readlines())
