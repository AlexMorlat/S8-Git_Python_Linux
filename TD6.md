Exercise 1: Configure Git
1. Check that Git is installed on your environment.
```
git
```
2. Configure your name and e-mail globally.
```
git config --global user.name "AlexMorlat"
git config --global user.email "am@gmail.com"

```

3. Check that Git has correctly recorded these two pieces of information.
hint : All Git commands have a -h flag to display the corresponding help.
Look there for the option of the git config command that lists all Git
configuration.
```
git config -h
git config --list

git add truc.md
git commmit -m

```

Exercise 2: Basic workflow with a single file
1. Create a git repository
```
mkdir repo
cd repo/
git init
```
2. Check that git has correctly initiliazed a repository by displaying the files
wihtin your current folder
```
ls -A
tree .git
```
3. Check the current git status
```
git status
```
4. Create a text file named “readme.md” whose content is “# Test repository”
```
echo "# Test repository" > readme.md
```
5. Check the current git status
```
git status
```
6. Stage the file
```
git add readme.md
```
7. Check the current git status
```
git status
```
8. Commit the file
```
git commit -m "Add ReadMe.md file"
```
9. Check the current git status
```
git status
```
10. Check the git logs
```
git log
```
11. Which informations are displayed ?
```
Utilisateur Timestamp MessageCommit
```

## Exercise 3: Basic workflow with multiple files treated separately

1. Create two empty python files named “main.py” and “functions.py”
```
echo "" > main.py
echo "" > functions.py
```
2. Check the current git status
```
git status 
```
3. Stage only the file “main.py”
```
git add main.py
```
4. Check the current git status
```
git status
```
5. Commit the file with an appropriate message
```
git commit main.py -m "Add main.py"
```
6. Check the current git status
```
git status
git log
```
7. Now stage and commit the file “functions.py”
```
git add functions.py
git commit -a ""
```
8. Check the current git status
```
git status
```
9. Check the git logs
```
git log --oneline
git checkout master
git checkout 1408d20f # Par exemple 
```

Exercise 4: Basic workflow with multiple files treated all
at once
1. Create three empty files named “requirements.txt”, “.gitignore” and “.private”
```
> requirements.txt
> .gitignore
> .private
```
2. Check the current git status
```
ls -A
git status
```
3. Stage all the files at once
```
# En plusieurs fois
git add requirements.txt
git add .gitignore
git add .private
# En une fois
git add.
```
4. Check the current git status
```
git status
```
5. Commit the current staged files
```
git commit -m"Add repo files"
```
6. Check the current git status
```
git status
```
7. Check the git logs where each log is displayed on a single line
```
```

Exercise 5: Private files
Files can be private in two ways :
— being a temporary file (like an open Excel would produce or Python
Jupyter Notebook would produce). This would happen to anyone using
your project.
— being a personal file (personal notes, etc.)
1. Emulate a temporary empty file by creating a file named “temp.ipynb”
```
```
2. Check the current git status
```
```
3. Add an instruction to .gitignore to prevent git from tracking this temp
file
```
```
4. Check the current git status
```
```
5. Create other temporary files named “temp.aux” and “temp.log”
```
```
6. Check the current git status
```
```
7. Change your instruction in .gitignore to prevent git from tracking any
file which name starts with “temp”
```
```
8. Check the current git status
```
```
9. Now let’s consider your personal notes will be added to the “.private” folder. Use the “exclude” git file to prevent git from tracking this “.private”
folder

## Exercise 6: Difference between versions

1. Add a online description of your repository in the “readme.md” file
```
```
2. Stage your “readme.md” file
```
```
3. Display the changes in your root directory since the last commit (not
just the current status)
```
```
4. Commit your change
5. Display the changes since the last commit
