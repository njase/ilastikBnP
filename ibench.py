import abc
from argparse import Namespace
import ilastik_main
from lazyflow.utility import Timer

class AbstractTest:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def run(self,title=""): 
        print("This abstract function should not have been called")
        raise NotImplementedError()


class BenchmarkTest(AbstractTest):
    def __init__(self):
        self.clean_paths = False
        self.configfile = None
        self.debug = False
        self.exit_on_failure = False
        self.exit_on_success = False
        self.fullscreen = False
        self.headless = True
        self.logfile = None
        self.new_project = None
        self.playback_script = None
        self.playback_speed = 1.0
        self.process_name = None
        self.project = None
        self.readonly = False
        self.redirect_output = None
        self.start_recording = False
        self.workflow = None

    def setup_project(self,project_name):
        self.project = project_name

    def run(self,title=""):
        if self.headless != True:
            print("Only headless mode is allowed in these tests")
            raise NotImplementedError()

        if self.project == None:
            print("Missing project path")
            raise NotImplementedError()
     
        parsed_args = Namespace(clean_paths=self.clean_paths,configfile=self.configfile,debug=self.debug,exit_on_failure=self.exit_on_failure,
        exit_on_success=self.exit_on_success,
        fullscreen = self.fullscreen,headless=self.headless,logfile=self.logfile,new_project=self.new_project,
        playback_script=self.playback_script,playback_speed=self.playback_speed,process_name=self.process_name,project=self.project,readonly=self.readonly,redirect_output=self.redirect_output,start_recording=self.start_recording,workflow=self.workflow)
        
        workflow_cmdline_args = ['--output_format=hdf5']
	
	with Timer() as testtimer:
            ilastik_main.main(parsed_args, workflow_cmdline_args)
        print"Test {} took {} seconds".format(title,testtimer.seconds())


class PixelClassificationBM(BenchmarkTest):
    def __init__(self):
        BenchmarkTest.__init__(self)
        self.test_title = "PixelClassification Benchmark"

    def run(self,title=""):
        self.setup_project('/export/home/smehta/ilastik/projects/mitocheck_2d+t/pixelClassification.ilp')
        super(PixelClassificationBM,self).run(self.test_title) 

# Check if shell or GUI mode


# shell mode
def shell_mode():
    test_list = [PixelClassificationBM()]
    [test.run() for test in test_list]

# GUI mode

#TBD: Later add parsing of shell args
def main():
    shell_mode()

if __name__=="__main__":
    main()
