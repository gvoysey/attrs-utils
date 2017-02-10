from docopt import docopt
import attr
"""
Docopt (https://docopt.org) is a powerful command line argument parser.
"""

def from_docopt(argv:str, docstring:str, version=None):
    #get the docopt output
    docopt_dict = docopt(doc=docstring, version=version, argv=argv)
    #sanitize the keys: can't contain '-', must be a valid attribute name..
    for key in docopt_dict.keys():
        clean = key.lstrip('-').replace('-','_')
        docopt_dict[clean] = docopt_dict.pop(key)
    #make a class out of it
    return attr.make_class(name='InputArgs', attrs=docopt_dict)()

