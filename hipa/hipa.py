
def hello():
	print("hello")



import os
from mit_semseg.config import cfg

def make_cfg(cfg_file, cfg_list):

	cfg.merge_from_file(cfg_file)
	cfg.merge_from_list(cfg_list)
	
	cfg.MODEL.arch_encoder = cfg.MODEL.arch_encoder.lower()
	cfg.MODEL.arch_decoder = cfg.MODEL.arch_decoder.lower()
	
	# absolute paths of model weights
	cfg.MODEL.weights_encoder = os.path.join(cfg.DIR, 'encoder_' + cfg.TEST.checkpoint)
	cfg.MODEL.weights_decoder = os.path.join(cfg.DIR, 'decoder_' + cfg.TEST.checkpoint)
	
	cfg.list_test = [{'fpath_img': x} for x in ["ADE_val_00001519.jpg"]]
	
	if not os.path.isdir(cfg.TEST.result):
	    os.makedirs(cfg.TEST.result)
