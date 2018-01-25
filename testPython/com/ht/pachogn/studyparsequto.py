# coding=utf-8

'''
、获取url参数
>>> from urllib import parse
>>> url = r'https://docs.python.org/3.5/search.html?q=parse&check_keywords=yes&area=default'
>>> parseResult = parse.urlparse(url)
>>> parseResult
ParseResult(scheme='https', netloc='docs.python.org', path='/3.5/search.html', params='', query='q=parse&check_keywords=yes&area=default', fragment='')
>>> param_dict = parse.parse_qs(parseResult.query)
>>> param_dict
{'q': ['parse'], 'check_keywords': ['yes'], 'area': ['default']}
>>> q = param_dict['q'][0]
>>> q
'parse'
#注意：加号会被解码，可能有时并不是我们想要的
>>> parse.parse_qs('proxy=183.222.102.178:8080&task=XXXXX|5-3+2')
{'proxy': ['183.222.102.178:8080'], 'task': ['XXXXX|5-3 2']}

'''
from urllib  import parse
import re

url = r'https://docs.python.org/3.5/search.html?q=parse&check_keywords=yes&area=default'
parseResult = parse.urlparse(url)
#ParseResult(scheme='https', netloc='docs.python.org', path='/3.5/search.html', params='', query='q=parse&check_keywords=yes&area=default', fragment='')

param_dict=parse.parse_qs(parseResult.query);
#{'q': ['parse'], 'check_keywords': ['yes'], 'area': ['default']}
q = param_dict['q'][0]
print(q);
#parse
#注意：加号会被解码，可能有时并不是我们想要的
parse.parse_qs('proxy=183.222.102.178:8080&task=XXXXX|5-3+2')
#{'proxy': ['183.222.102.178:8080'], 'task': ['XXXXX|5-3 2']}
test=parse.quote("ab&C");
print(test);
result_list= list();print(result_list);

test={'url': 'http://p3.pstatp.com/large/594b00044aaadaa7550a'},
ls=list();
#ls.append(test['url']);print(ls);
inputStr= "hello crifan, nihao crifan";
replacedStr = re.sub(r"hello (\w+), nihao \1", "\g<1>", inputStr);
replacedStr = re.sub(r"hello (");
print("repaleceStr=",replacedStr);
