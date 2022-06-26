if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Ajmal342/JOHN_LUTHER /JOHN_LUTHER
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /JOHN_LUTHER
fi
cd /JOHN_LUTHER
pip3 install -U -r requirements.txt
echo "Starting JOHN_LUTHER...."
python3 main.py
