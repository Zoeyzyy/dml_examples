sudo rm ./packet/*.pcap 
sudo nohup tcpdump host 172.22.5.106 -s 128  -w ./packet/from106.pcap & 
sudo nohup tcpdump dst 172.22.5.106 -s 128  -w ./packet/to106.pcap & 
sudo nohup tcpdump host 172.22.5.112 -s 128  -w ./packet/from112.pcap & 
sudo nohup tcpdump dst 172.22.5.112 -s 128  -w ./packet/to112.pcap & 

nohup torchrun --master_addr=172.22.5.106 --master_port=22349 --nproc_per_node=1 --nnodes=3 --node_rank=1 main.py --backend=nccl --use_syn --batch_size=32 --num_epochs=300 --arch=resnet152 &
