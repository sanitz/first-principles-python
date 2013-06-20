from nose.tools import *
import re
from hamcrest import *

class StringCreator_Test:
    @istest
    def createsOnlyWhitespace(self):
        assert_that(StringCreator().create(), contains_only_whitespace())



from hamcrest.core.base_matcher import BaseMatcher
class StringMatchesPattern(BaseMatcher):

    def __init__(self, pattern):
        self.pattern = pattern

    def describe_to(self, description):
        description.append_text("a string matching '") \
                .append_text(self.pattern) \
                .append_text("'")

    def _matches(self, item):
        return re.match(self.pattern, item)

def contains_only_whitespace():
    return StringMatchesPattern(r'^\s*$')



class StringCreator:
    def create(self):
        return u' \t \n '
