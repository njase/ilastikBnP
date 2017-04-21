from TestRoot import AbstractTest
from PixelClassification import PixelClassification
import cProfile
import gprof2dot
import pstats
import re

class FunctionProfileTest(AbstractTest):
    def __init__(self):
        self.cp_opfile = 'pixelClassificationprof.cprof'
        self.fpobj = cProfile.Profile()
        self.ilastik_pattern = "ilastik-meta"
        self.phase1_filtered_stats = 'phase1_filtered.cprof'

    def run_cprof(self,callable_test_obj):
        self.fpobj.clear()
        self.fpobj.enable(builtins=False)
        callable_test_obj()
        self.fpobj.disable()
        self.fpobj.dump_stats(self.cp_opfile)
        
    def run_gprof(self):
        gprof2dot.main()

    def run(self,callable_test_obj):
        self.run_cprof(callable_test_obj)
        self.run_gprof()
	
    def phase1(self):
        #make a graph of cumulative time and dump it here
        rawstats = self.fpobj.getstats()
        self.fpobj.dump_stats('rawstats.cprof')

        cumtime = []        
        for x in rawstats:
            if(re.search(self.ilastik_pattern,x.code.co_filename)):                
                [cumtime.append('{:.3f}'.format(x.totaltime)) for x in rawstats]
        cumtime.sort(reverse=True)

        #print cumtime
        ign_str = '''
        import matplotlib.pyplot as plt
        plt.plot(cumtime)
        plt.ylabel('cumulative time')
        plt.ion() #For non blocking - see http://stackoverflow.com/questions/28269157/plotting-in-a-non-blocking-way-with-matplotlib
        plt.show()
        '''

        #For comparison, generate equivalent pstats and store them in a file
        pstats.Stats(self.fpobj).sort_stats('tottime').dump_stats(self.phase1_filtered_stats)
        
        
        #Check graph of cumulative time for inconsistencies

    def print_phase1_stats(self):
        pstats.Stats(self.phase1_filtered_stats).sort_stats('cumulative').print_stats(self.ilastik_pattern)
            

class PixelClassificationFprof(FunctionProfileTest):
    def __init__(self):
        FunctionProfileTest.__init__(self)
        self.testobj = PixelClassification()

    def run_test(self,title=""):
	self.testobj.setup_project('/export/home/smehta/ilastik/projects/mitocheck_2d+t/pixelClassification.ilp')
        self.run(self.testobj)

    def manual_analysis(self): pass #TBD

    def auto_analysis(self):
        self.phase1()
        #self.print_phase1_stats()


    
        
