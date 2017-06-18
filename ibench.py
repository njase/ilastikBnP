from BenchmarkTest import PixelClassificationBM
import sys,os

# shell mode
def shell_mode():
    pc_proj_path = './2d_project_pc_all_features.ilp'
    pc_data_files = ['./data/iso.01500.png', './data/iso.01501.png']
    test_list = [PixelClassificationBM(pc_proj_path,pc_data_files)]
    [test.run() for test in test_list]

def main():
    sys.path.append(os.getcwd())
    shell_mode()

if __name__=="__main__":
    main()
