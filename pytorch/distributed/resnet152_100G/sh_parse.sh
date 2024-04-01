rm ./*.png 
tcpdump -r ./packet/from106.pcap > ./packet/from106.txt 
tcpdump -r ./packet/to106.pcap > ./packet/to106.txt 
python3 parse.py  --sender=106 --reciever=108 --pcap_file from106 & 
python3 parse.py  --sender=108 --reciever=106 --pcap_file to106 & 
tcpdump -r ./packet/from112.pcap > ./packet/from112.txt 
tcpdump -r ./packet/to112.pcap > ./packet/to112.txt 
python3 parse.py  --sender=112 --reciever=108 --pcap_file from112 & 
python3 parse.py  --sender=108 --reciever=112 --pcap_file to112 & 
