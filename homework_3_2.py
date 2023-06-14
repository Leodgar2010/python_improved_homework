# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.
text = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) " \
       "in the Netherlands as a successor to the ABC programming language, which was inspired by SETL, capable " \
       "of exception handling and interfacing with the Amoeba operating system. Its implementation began in " \
       "December  1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, " \
       "until 12 July 2018, when he announced his 'permanent vacation' from his responsibilities as Python's ' \
      'benevolent dictator for life', a title the Python community bestowed upon him to reflect his long-term " \
       "commitment as the project's chief decision-maker. In January 2019, active Python core developers elected " \
       "a five-member Steering Council to lead the project."
base = text.replace(".", "").replace(",", "").replace("'", "").replace("(", "").replace(")", "").lower()
arr = base.split()
dic = {}
value_set = set()
result_dic = {}
for i in arr:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1
for i in dic.values():
    value_set.add(i)
for i in dic.keys():
    if dic.get(i) in value_set and len(result_dic) < 10:
        result_dic[i] = dic.get(i)
print(value_set)
