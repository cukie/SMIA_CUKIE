#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cukie
# @Date:   2015-08-30 11:05:36
# @Last Modified by:   cukie
# @Last Modified time: 2015-08-30 11:38:01

import batch_runner
import parse_config


def batchRunnerFromConfigDict(config_dict):
	'''
	Creates a BatchRunner instance from a given configuration dictionary mapping input parameters to values.
	See batch_runner.BatchRunner for an explanation of parameters. 
	'''

	base_dir = config_dict['base_dir']
	num_layers = config_dict['num_layers']
	num_masks = config_dict['num_masks']
	num_markers = config_dict['num_markers']
	mask_names = config_dict['mask_names']
	marker_names = config_dict['marker_names']
	output_path = config_dict['output_path']
	output_images = config_dict['output_images']
	output_thumbnails = config_dict['output_thumbnails']
	# We want this as a dictionary for faster lookups
	white_list = {}
	for sentence in config_dict['overlay_white_list']:
		white_list[sentence] = sentence

	return batch_runner.BatchRunner(base_dir, 
									num_layers, 
									num_masks, 
									num_markers, 
									mask_names, 
									marker_names, 
									white_list, 
									output_images, 
									output_thumbnails, 
									output_path)

def runSMIAFromConfig(config_file):
	'''
	An entry point to the SMIA-CUKIE application. This will kick off a run as specified by the configuration file.

	:param string config_file: The absolute path to a properly formatted config file.

	'''
	# parse the json configuration file
	success,message,config_dict = parse_config.ParseConfig(config_file)
	if not success:
		print "ERRORS: \n" + message
		sys.exit(1)
	else:
		print message 

	# Get our BatchRunner Object
	batchRunner = batchRunnerFromConfigDict(config_dict)

	# Here's where the magic happens
	batchRunner.run()
	
	#TODO: This is ugly... we really should be logging. 
	print
	print "You have succesfully procesed:\n" + base_dir
	print
	print "See your results in:\n" + output_path
	print


if __name__ == '__main__':
	'''Run SMIA-CUKIE from the command line'''
	runSMIAFromConfig(sys.argv[1])