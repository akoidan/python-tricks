# -*- coding: utf-8 -*-

def repr_dict(d):
	return '{%s}' % ', '.join("'%s': '%s'" % pair for pair in d.iteritems())


mydict = {}
mydict['string']=u'ыв'
mydict['sd']=u'ЫМС'

print(mydict)
mydict2= repr_dict(mydict)
print mydict2
