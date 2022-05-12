python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a=["Mary","Sam"]
>>> b=["Smdy","People"]
>>> a=b
>>> a
['Smdy', 'People']
>>> b
['Smdy', 'People']
>>> a=b=b
>>> b
['Smdy', 'People']
>>> a
['Smdy', 'People']
>>> a+b
['Smdy', 'People', 'Smdy', 'People']
>>> a=["Mary","Sam"]
>>> b=["Smdy","People"]
>>> bt={"Sam":12,""Zuena":33}
  File "<stdin>", line 1
    bt={"Sam":12,""Zuena":33}
                   ^
SyntaxError: invalid syntax
>>> bt={"Sam":12,"Zuena":33}
>>> bt={"Sir":55,"Maggie":23}
>>> bt
{'Sir': 55, 'Maggie': 23}
>>> a={"Sam":12,"Zuena":33}
>>> bt
{'Sir': 55, 'Maggie': 23}
>>> bt={"Sir":55,"Maggie":23}
>>> bt{"Maggie"}=a{"Sam"}
  File "<stdin>", line 1
    bt{"Maggie"}=a{"Sam"}
      ^
SyntaxError: invalid syntax
>>> b=["Smdy","People"]
>>> a=["Mary","Sam"]
>>> a[0,1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> a=[0]=b[0]
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> a=["Mary","Sam"]
>>> b=["Smdy","People"]
>>> she=[]
>>> she=[a]
>>> a
['Mary', 'Sam']
>>> a=b
>>> a
['Smdy', 'People']
>>> b
['Smdy', 'People']
>>> she
[['Mary', 'Sam']]
>>> b=she
>>> b
[['Mary', 'Sam']]
>>> she=[a[0],a[1]]
>>> she
['Smdy', 'People']
>>> a=["Mary","Sam"]
>>> b=["Smdy","People"]
>>> she=[]
>>> she=[a[0],a[1]]
>>> she
['Mary', 'Sam']
>>> a=b
>>> a
['Smdy', 'People']
>>> b=she
>>> b
['Mary', 'Sam']

