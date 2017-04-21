from TestRoot import AbstractTest
from lazyflow.utility import Timer
from PixelClassification import PixelClassification

class BenchmarkTest(AbstractTest):
    def __init__(self):        
        pass

    def run(self,callable_testobj):
        with Timer() as testtimer:
            callable_testobj()
        print "Test {} took {} seconds".format(callable_testobj.name(),testtimer.seconds())

	##TBD Add variables and methods to collect time for grpahical analysis


class PixelClassificationBM(BenchmarkTest):
    def __init__(self):
        BenchmarkTest.__init__(self)
        self.testobj = PixelClassification()

    def run_test(self):
	#TBD: Add provision to supply project path from outside
        self.testobj.setup_project('/export/home/smehta/ilastik/projects/mitocheck_2d+t/pixelClassification.ilp')
        super(PixelClassificationBM,self).run(self.testobj)
