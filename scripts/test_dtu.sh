#!/usr/bin/env bash
TESTPATH="/data-1/leiguojun/data/dtu" 						# path to dataset dtu_test
TESTLIST="lists/dtu/test.txt"
CKPT_FILE="/home/leiguojun/logs/mvsformer/trans/model_000015.ckpt"			   # path to checkpoint file, you need to use the model_dtu.ckpt for testing
FUSIBLE_PATH="" 								 	# path to fusible of gipuma
OUTDIR="/home/leiguojun/mvs_output/mvs_trans_official" 						  # path to output
if [ ! -d $OUTDIR ]; then
	mkdir -p $OUTDIR
fi


python test.py \
--dataset=general_eval \
--batch_size=16 \
--testpath=$TESTPATH  \
--testlist=$TESTLIST \
--loadckpt=$CKPT_FILE \
--outdir=$OUTDIR \
--numdepth=192 \
--ndepths="48,32,8" \
--depth_inter_r="4.0,1.0,0.5" \
--interval_scale=1.06 \
--filter_method="normal" \
--fusibile_exe_path=$FUSIBLE_PATH
#--filter_method="normal"

