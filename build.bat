
rmdir /s /q "dist"
if not exist "dist" mkdir "dist"
if not exist "logs" mkdir "logs"
if not exist "dist\projects" mkdir "dist\projects"

python -m pipenv run pyinstaller --noconfirm simple-text-generator-ui.spec
python -m pipenv run pyinstaller --noconfirm run_training.spec

