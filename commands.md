cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git rev-parse --show-toplevel
deactivate
git init
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md requirements.txt .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
printf ".venv/\n__pycache__/\n" > .gitignore
pip freeze > requirements.txt
ls -a
ls tests
git status
git add .
git commit -m "Start midterm: project structure and environment"
git config --global user.name "Pamelaemmrich"
git config --global user.email "pamelaemmrich@usf.edu"
git branch -M main
git remote add origin https://github.com/pamelaemmrich/ism3232-midterm.git
git push -u origin main
git remote set-url origin https://github.com/Pamelaemmrich/ism3232-midterm.git
git add commands.md
git commit -m "Add commands log"
git push