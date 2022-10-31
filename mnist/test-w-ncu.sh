#!/bin/bash

ncu --profile-from-start off --metrics smsp__sass_thread_inst_executed_op_fadd_pred_on,smsp__sass_thread_inst_executed_op_fmul_pred_on,smsp__sass_thread_inst_executed_op_ffma_pred_on --target-processes all python3 main_ncu.py --dry-run --epochs 2 2>&1 | tee ncu.out



