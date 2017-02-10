import attr
from attr.validators import instance_of
from enum import Enum

def ensure_cls(cl):
    """If the attribute is an instance of cls, pass, else try constructing."""

    def converter(val):
        if isinstance(val, cl):
            return val
        else:
            return cl(**val)

    return converter


def ensure_enum(cl):
    """If the attribute is an instance of cls, pass, else try constructing."""

    def converter(val):
        if isinstance(val, cl):
            return val
        else:
            return cl[val]

    return converter


def is_path_of_file(instance, attribute, value):
    if not type(value) == str or not path.isfile(value):
        raise FileExistsError('{} is not a valid file.'.format(value))

def in_range_inclusive(low=None, high=None, type=None):
    def _isvalid(instance, attribute, value):
        if value < low or value > high:
            raise ValueError('{} out of range'.format(value))
        if not isinstance(value, type):
            raise ValueError('{} out of range'.format(value))

    return _isvalid
