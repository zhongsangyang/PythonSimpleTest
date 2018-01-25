#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import re
some_text='alpha , beta ,,,gamma delta ';
splitt=re.split(',*',some_text);
print(splitt);

