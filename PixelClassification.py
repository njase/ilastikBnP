import ilastik_main
from argparse import Namespace

#This knows how to perform Pixel Classification
class PixelClassification:
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
        self.title = "PixelClassification Test"

    @property
    def name(self):
        return self.title

    def setup_project(self,project_name):
        self.project = project_name

    def setup_data(self,data_files):
        self.data_files = data_files

    def __call__(self):
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
        
        workflow_cmdline_args = self.data_files
	
        ilastik_main.main(parsed_args, workflow_cmdline_args)
