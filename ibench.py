from BenchmarkTest import PixelClassificationBM
import sys,os

# shell mode
def shell_mode():
    #TBD: Later add parsing of shell args
    pc_proj_path = '/export/home/smehta/ilastik/projects/mitocheck_2d+t/pixelClassification.ilp'
    pc_data_files = ['/export/home/smehta/miniconda2/envs/project/data/iso.01500.png', '/export/home/smehta/miniconda2/envs/project/data/iso.01501.png']
    test_list = [PixelClassificationBM(pc_proj_path,pc_data_files)]
    [test.run() for test in test_list]

def main():
    sys.path.append(os.getcwd())
    shell_mode()

if __name__=="__main__":
    main()
