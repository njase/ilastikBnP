from TestRoot import AbstractTest
from PixelClassification import PixelClassification
import perf

class BenchmarkTest(AbstractTest):
    def __init__(self,title="Untitled Test"):
        self.test_title = title

    def run(self,callable_testobj):
        print("-------------------------------------------------------------")
        print ("About to start benchmarking for " + self.test_title)
        print("-------------------------------------------------------------")
        runner = perf.Runner()
        myb = runner.bench_func(self.test_title, callable_testobj)
        #myb.dump('testoutput.json',compact=False,replace=True)
        print("-------------------------------------------------------------")
        print("Finished benchmarking for " + self.test_title)
        print("-------------------------------------------------------------")


class PixelClassificationBM(BenchmarkTest):
    def __init__(self,proj_path,raw_data):
        self.testobj = PixelClassification()
        BenchmarkTest.__init__(self,self.testobj.name)
        self.testobj.setup_project(proj_path)
        self.testobj.setup_data(raw_data)

    def run(self):
        super(PixelClassificationBM,self).run(self.testobj)
