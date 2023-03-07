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

```
2. Check the current git status
```
```
3. Stage only the file “main.py”
```
```
4. Check the current git status
```
```
5. Commit the file with an appropriate message
```
```
6. Check the current git status
```
```
7. Now stage and commit the file “functions.py”
```
```
8. Check the current git status
```
```
9. Check the git logs
```
```
