echo "Starting FB OS"
sudo python3 loading.py &
sleep 3
sudo python readsensor.py &
sleep 1
sudo python main.py &
