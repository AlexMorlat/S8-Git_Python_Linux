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
git log --oneline
```

Exercise 5: Private files
Files can be private in two ways :
— being a temporary file (like an open Excel would produce or Python
Jupyter Notebook would produce). This would happen to anyone using
your project.
— being a personal file (personal notes, etc.)
1. Emulate a temporary empty file by creating a file named “temp.ipynb”
```
> temps.ipynb
```
2. Check the current git status
```
git status 
```
3. Add an instruction to .gitignore to prevent git from tracking this temp
file
```
vim .gitignore
temp.ipynb
#ou 
echo "temp.ipynb" >> .gitignore
```
4. Check the current git status
```
git status
#On ne voit plus le fichier temp.ipynb
```
5. Create other temporary files named “temp.aux” and “temp.log”
```
> temp.aux
> temps.log
 
```
6. Check the current git status
```
git status
```
7. Change your instruction in .gitignore to prevent git from tracking any
file which name starts with “temp”
```
vim .gitignore
temp*
```
8. Check the current git status
```
git status
```
9. Now let’s consider your personal notes will be added to the “.private” folder. Use the “exclude” git file to prevent git from tracking this “.private”
folder
```
vim .git/info/exclude
.private
#attention il ne doit pas avoir été add précédément
# ie le fichier ne doit pas être déja suivi par Git
#Etape à faire avant de Add
```

## Exercise 6: Difference between versions

1. Add a online description of your repository in the “readme.md” file
```
echo "Info" >> readme.md
```
2. Stage your “readme.md” file
```
git add readme.md
```
3. Display the changes in your root directory since the last commit (not
just the current status)
```
#Pour tout les fichiers
git diff --staged
```
4. Commit your change
```
git commit -m "Desc"
```
5. Display the changes since the last commit
```
git diff
```


## Exercise 7: Undo

1. Suppress all your files.
```
rm files...
```
2. Use Git to restore your files.
```
git restore .
#On récupère pas ce qui n'était pas suivi par Git
```
3. Backup your Git repository elsewhere
(pretending a copy exists on another colleague’s computer or on a remote
server).
```
cp -r .git ../backup
```
4. Suppress your root directory, create a new empty one and use your backup to restore everything.
```
rm -rf 
#Attention à l'utilisation
#On a enlevé le .git => Ce n'est plus un repo
cp -r ../backup/.git .
git restore
```
5. Unstage your first file
```

```
6. Commit your two file changes directly, without staging them.
```
git comit -am "Add directly"
```
7. Check your commit log history. Do you see your new commit ?
```
git log
```
8. Without affecting your Git repository, set your root directory state as of
the snapshot of your first commit.
```
git log --oneline
git ckeckout 45hg52
#avec le dernier identifiant

git checkout master
#Etat plus actuel

git checkout HEAD~1
#Revenir à l'état précédent (relatif)
```
9. Check your commit log history. You do not see all commits, do you ? How
can you see all of them ?
```

```
10. Return to the snapshot of your your last commit.
```
```
11. Undo your second commit by adding a new commit that reverts it.
```
```
12. Check the content of your root directory. Have your previous changes
disappeard ?
```
```
13. Check your commit log history. Do you see your revert commit ?
```
```
14. Remove the last 2 commits from the history.
```
```
15. Check the content of your root directory. Have your previous changes
disappeard ?
```
```
16. Check your commit log history. Have you lost the last 2 commits ?
```
```
