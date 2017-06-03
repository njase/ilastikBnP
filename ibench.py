from BenchmarkTest import PixelClassificationBM
import sys,os

# shell mode
def shell_mode():
    #TBD: Later add parsing of shell args
    pc_proj_path = '/export/home/smehta/ilastik/projects/mitocheck_2d+t/pixelClassification.ilp'
    test_list = [PixelClassificationBM(pc_proj_path)]
    [test.run() for test in test_list]

def main():
    sys.path.append(os.getcwd())
    shell_mode()

if __name__=="__main__":
    main()
