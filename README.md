# prep virtual environment (currently Python 2.7)
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# build site
pelican content -t themes/irods_theme

# deploy via rsync
rsync -arv output/ user@target:/path/to/output/
