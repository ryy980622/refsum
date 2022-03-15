#   Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys
print(sys.path)
sys.path.append('/home/ryy/code/NLP/20220308')
# import argparse
from utils.args import print_arguments
from utils.logging import init_logger
from utils.check import check_gpu

from networks.graphsum.run_graphsum import main as run_graphsum
from run_args import parser as run_parser

import argparse
'''
export CUDNN_HOME=/home/ryy/cudnn/cuda
export LD_LIBARARY_PATH=${CUDNN_HOME}/lib64:$LD_LIBRAYRY_PATH
export LD_LIBRARY_PATH=${CUDNN_HOME}/lib64:$LD_LIBRARY_PATH
export CPLUS_INCLUDE_PATH=${CUDNN_HOME}/include:$CPLUS_INCLUDE_PATH
'''

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-model_name", default="graphsum")
    parser.add_argument("-use_cuda", default=True)
    parser.add_argument("-is_distributed", default=False)
    parser.add_argument("-use_multi_gpu_test", default=False)
    parser.add_argument("-use_fast_executor", default=False)
    parser.add_argument("-use_fp16", default=False)
    parser.add_argument("-use_dynamic_loss_scaling", default=False)
    parser.add_argument("-init_loss_scaling", default=12800)
    parser.add_argument("-weight_sharing", default=True)
    parser.add_argument("-do_train", default=True)
    parser.add_argument("-do_val", default=False)
    parser.add_argument("-do_test", default=True)
    parser.add_argument("-do_dec", default=True)
    parser.add_argument("-verbose", default=True)
    parser.add_argument("-batch_size", default=1)
    parser.add_argument("-in_tokens", default=True)
    parser.add_argument("-stream_job", default='')
    parser.add_argument("-init_pretraining_params", default="")
    parser.add_argument("-train_set",
                        default="/home/ryy/code/NLP/20220308/Data/delve_data_tfidf_paddle/delve.100.delve_data_tfidf_json/train")
    parser.add_argument("-dev_set",
                        default="/home/ryy/code/NLP/20220308/Data/delve_data_tfidf_paddle/delve.100.delve_data_tfidf_json/valid")
    parser.add_argument("-test_set",
                        default="/home/ryy/code/NLP/20220308/Data/delve_data_tfidf_paddle/delve.100.delve_data_tfidf_json/test")
    parser.add_argument("-vocab_path",
                        default="/home/ryy/code/NLP/20220308/vocab/spm9998_3.model")
    parser.add_argument("-config_path",
                        default="/home/ryy/code/NLP/20220308/model_config/graphsum_config.json")
    parser.add_argument("-checkpoints",
                        default="/home/ryy/code/NLP/20220308/Log/models/graphsum_delve")
    parser.add_argument("-init_checkpoint", default="")
    parser.add_argument("-decode_path",
                        default="/home/ryy/code/NLP/20220308/Log/results/graphsum_delve")
    parser.add_argument("-lr_scheduler", default="noam_decay")
    parser.add_argument("-save_steps", default=10000)
    parser.add_argument("-weight_decay", default=0.01)
    parser.add_argument("-warmup_steps", default=8000)
    parser.add_argument("-validation_steps", default=20000)
    parser.add_argument("-epoch", default=100)
    parser.add_argument("-max_para_num", default=30)
    parser.add_argument("-max_para_len", default=60)
    # parser.add_argument("-max_tgt_len", default=300)
    parser.add_argument("-max_tgt_len", default=1)
    parser.add_argument("-max_out_len", default=300)
    parser.add_argument("-min_out_len", default=200)
    parser.add_argument("-graph_type", default="similarity")
    parser.add_argument("-len_penalty", default=0.6)
    parser.add_argument("-block_trigram", default=True)
    parser.add_argument("-report_rouge", default=True)
    parser.add_argument("-learning_rate", default=2.0)
    parser.add_argument("-skip_steps", default=100)
    parser.add_argument("-grad_norm", default=2.0)
    parser.add_argument("-pos_win", default=2.0)
    parser.add_argument("-label_smooth_eps", default=0.1)
    parser.add_argument("-num_iteration_per_drop_scope", default=10)
    parser.add_argument("-log_file", default="/home/ryy/code/NLP/20220308/Log/log/graphsum_delve.log")
    parser.add_argument("-random_seed", default=1)

    parser.add_argument("-beam_size", default=5)
    parser.add_argument("-incr_every_n_steps", default=100)
    parser.add_argument("-decr_every_n_nan_or_inf", default=2)
    parser.add_argument("-incr_ratio", default=2)
    parser.add_argument("-decr_ratio", default=2)
    parser.add_argument("-beta1", default=0.9)
    parser.add_argument("-beta2", default=0.998)
    parser.add_argument("-eps", default=1e-9)

    args = parser.parse_args()

    print_arguments(args)
    init_logger(args.log_file)
    check_gpu(args.use_cuda)

    if args.model_name == 'graphsum':
        run_graphsum(args)
    else:
        raise ValueError("Model %s is not supported currently!" % args.model_name)
