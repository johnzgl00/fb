echo "Starting FB OS"
sudo python3 loading.py
sleep 2
sudo python readsensor.py
sleep 1
sudo python main.py
