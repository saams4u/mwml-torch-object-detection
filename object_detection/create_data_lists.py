# create_data_lists.py - creates and saves JSON files from downloaded data

from utils import create_data_lists

if __name__ == '__main__':
    create_data_lists(voc07_path='../datasets/voc/VOC2007',
                      voc12_path='../datasets/voc/VOC2012',
                      output_folder='../saved_lists')