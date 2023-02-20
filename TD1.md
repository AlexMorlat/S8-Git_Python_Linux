Alexandre MORLAT

# TD1 

## Exercice 1
Chemin absolue = depuis la racine 

Chemin relatif = on part direct de home

Ctr+r = Recherche dans l'historique (Sinon les flêches)

cd..  = remonter au dessus dans l'arboresence 

Ctrl+l = Permet de faire un jump

clear = efface les commandes precedentes

cat head tail = affichage du contenu du fichier

rmdir fichier/ = Suppression du fichier (Attention doit être vide)

rm -r fichier = Supression en recursif (le fichier et ce qu'il y a dedans)

#### Question 1: Go to the root directory
```
cd /
```

#### Question 2: Display the content of the current (root) directory +(hide files)
```
ls
ls --help
man ls
ls -a 
ls -A
```

#### Question 3: Check your current location
```
pwd
```

#### Question 4: Try to create a directory named test
(La racine nécessite le super utilisateur "sudo")
```
sudo mkdir fichier_test
```

#### Question 5: Go to the general home directory (should contain folders named after each user)
```
cd..
```

#### Question 6: Go to your home directory
```
cd ~
```

#### Question7. Go back to the general home directory (located "just above")
```
cd..
```

#### Question8. Go again "just above", you should be back to the root directory
```
```

#### Question9. Go directly to your home directory (named after you). It should be a very simple command, which take no name as parameter of the path
```
cd ~
```

#### Question10. Try to create a directory named test
```
mkdir test
```

#### Question11. Go into this new directory
```
cd test/
```

#### Question12. Check your current location
```
pwd
```

## Exercise 2: Create, Rename, copy, delete
#### 1. Go to your home directory (should be named after you, you might bethere by default)
```
cd ~
```
#### 2. Check your current location
```
pwd
```
#### 3. Create a folder linux_ex_1
```
mkdir linux_ex_1
```
#### 4. Go into this folder
```
cd linux_ex_1/
```
#### 5. Create an empty text file named [first_name]_[last_name].txt (e.g. alexis_bogroff.txt)
```
touch alexandre_morlat.txt
```
#### 6. Create a folder notes
```
mkdir notes
```
#### 7. Move your text file into this folder
```
mv alexandre_morlat.txt notes
```
#### 8. Rename the text file by appending the current year [first_name]_[last_name]_[current_year].txt
```
cd notes/
mv alexandre_morlat.txt alexandre_morlat_2023.txt
```
#### 9. Make a copy of this folder, name it notes_2022
```
cp -r notes notes_2022
```
#### 10. Delete the first folder (notes) using the verbose option
```
rm -rv notes
```

## Exercise 3: Create and run a script
#### 1. Create a script script_1.sh in the folder linux_ex_1
```
vi script_1.sh
```
#### 2. In the script, write the commands that would output the following :Script running please wait ...Done.
```
i

echo "Script running please wait ...Done."
```
#### 3. Quit editing and save the script
```
Echap
:wq
```
#### 4. Display the content of the script (using a command, not from an editor)
```
cat script_1.sh
```
#### 5. Run the script
```
chmod +x script_1.sh
./script_1.sh
```

## Exercise 4:.1 Change the rights for accessing or modifying a file
#### 1. Create a file credentials in the folder linux_ex_1
```
touch credentials
```
#### (a) Write any kind of (fake) personal information within the file
```
echo "Alexandre" > credentials
echo "Morlat" >> credentials
```
#### (b) Display the file content
```
cat credentials
```
#### (c) Display the current permissions
```
ls -l credentials
```
#### 2. Change the current permissions to : read only for all users
```
chmod a=r credentials
chmod u=r,g=r,o=r credentials
chmod 555 credentials
```
#### (a) Display the new permissions
```
ls -l credentials
```
#### (b) Modify and save the file
```
:wq
```
#### (c) Display the file content
```
cat credentials
```
#### 3. Change the permissions back to read and write for all users
```
chmod a=rw credentials
```
#### (a) Display the new permissions
```
ls -l credentials
```
#### (b) Modify and save the file
```
//
```
#### (c) Display the file content
```
cat credentials
```
#### On the same file :
#### 1. Add the execute permission to the owner
```
chmod a=rwx credentials
```
#### (a) Display the new permissions
```
//
```
#### 2. Remove the read permission to other users
```
chmod 700 credentials
```
#### (a) Display the new permissions
```
ls -l credentials
```
#### 3. Change the permissions to read, write and execute for all users
```
chmod 777 credentials
```
#### (a) Display the new permissions
```
ls -l credentials
```

## Exercise 4:.2 Access root files
#### 1. Go to the root folder
```
cd /
```
#### 2. Create a file in root user mode named .private_file
```
sudo vim .private_file
```
ou  sudo su (Pour utiliser sudo à chaque commande)

(a) Write some information in the file
```
echo "Private Info" > .private_file
```
(b) Display the file content
```
cat .private_file
```
(c) Display all the files in the folder including hidden files
```
ls -a
```
#### 3. Modify the file in normal user mode
```
```
(a) Write some new information in the file
```
vi .private_file
```
(b) Display the file content
```
cat .private_file
```


## Exercise 4:.3 Change a file owner
```
sudo chown ubuntu super 
sudo chmod 744 super
```


## Exercise 4:.4 Manage Packages (tools / functions)
1. Update your main package manager named apt
```
sudo apt update
```
2. Upgrade apt
```
sudo apt upgrade
```
3. Install the package cmatrix
```
sudo apt-get update
sudo apt-get install cmatrix
```
