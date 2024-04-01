rm ./*.png 
tcpdump -r ./packet/from3.pcap > ./packet/from3.txt 
tcpdump -r ./packet/to3.pcap > ./packet/to3.txt 
python3 parse.py  --sender=3 --reciever=6 --pcap_file from3 & 
python3 parse.py  --sender=6 --reciever=3 --pcap_file to3 & 
tcpdump -r ./packet/from4.pcap > ./packet/from4.txt 
tcpdump -r ./packet/to4.pcap > ./packet/to4.txt 
python3 parse.py  --sender=4 --reciever=6 --pcap_file from4 & 
python3 parse.py  --sender=6 --reciever=4 --pcap_file to4 & 
