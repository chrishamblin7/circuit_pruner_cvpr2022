from subprocess import call

config = '../configs/alexnet_sparse_config.py'

layers = ['features_6','features_8','features_10']
#data_path = '../image_data/imagenet_2/'
data_path = '../image_data/imagenet_2_test/'
units = range(20)
device = 'cuda:0'


for unit in units:
    print('PROCESSING UNIT: %s'%str(unit))
    for layer in layers:
        print('PROCESSING LAYER: %s'%layer)
        feature_target = {layer:[unit]}
        call_str = 'python snip_rank.py --unit %s --layer %s --config %s --data-path %s --device %s'%(str(unit),layer,config,data_path,device)
        call(call_str,shell=True)