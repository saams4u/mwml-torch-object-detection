# get_data.sh - download datasets to be processed and saved as JSON lists.

cd datasets/voc

wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
wget http://host.robots.ox.ac.uk/pascal/VOC/voc2012/VOCtrainval_11-May-2012.tar

tar -xvf VOCtrainval_06-Nov-2007.tar
tar -xvf VOCtrainval_11-May-2012.tar

rm VOCtrainval_06-Nov-2007.tar
rm VOCtrainval_11-May-2012.tar

cd ..
cd ..