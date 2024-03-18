torchrun \
--master_addr=172.22.5.106 --master_port=22339 \
--nproc_per_node=1 --nnodes=2 --node_rank=0 \
main.py \
--backend=nccl --use_syn --batch_size=128 --arch=resnet101