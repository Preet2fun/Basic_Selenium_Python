from proboscis import test
from proboscis import asserts
from proboscis import TestProgram

@test()
def simple():
    asserts.assert_equal(1,1)

TestProgram().run_and_exit()
