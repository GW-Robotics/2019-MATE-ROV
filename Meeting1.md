# Meeting 1 - 9/17/18
### Required software
* [VSCode](https://code.visualstudio.com/)
* [Git](https://git-scm.com/)
### Useful software
* [Fritzing](http://fritzing.org/home/)
## Navigating with the command line
### Mac
```shell
# List folders and files in current directory
Alex-Macbook-Pro:~ alex$ ls
folder1   folder2   file1.c   file2.c

# Navigate to a sub-directory
Alex-Macbook-Pro:~ alex$ cd folder1 # Now we are in folder1

# Go up a directory
Alex-Macbook-Pro:folder1 alex$ cd .. # Now we are back in our starting directory
```
### Windows
```
# List folders and files in current directory
C:\> dir
2018-09-17  11:59   <DIR>       .
2018-09-17  11:59   <DIR>       ..
2018-09-11  2:09     2,543,600  file1.c
2018-09-17  3:14        35,266  file2.c
2018-09-06  10:45   <DIR>       folder1
2018-08-23  7:15    <DIR>       folder2

# Navigate to a sub-directory
C:\> cd folder1 # Now we are in folder1

# Go up a directory
C:\folder1> cd .. # Now we are back in our starting directory
```
## Using git
Test that git is installed
```shell
$ git --version
git version 2.14.1
```
Clone this repository
```shell
$ git clone https://github.com/GW-Robotics/2019-MATE-ROV/
```
Navigate into the repository
```shell
$ cd 2019-MATE-ROV
```
Committing a new file
```shell
$ git add file.txt
$ git commit -m "I added a file!"
$ git push
```
Committing changes to existing files
```shell
$ git commit -am "Made changes to files"
$ git push
```
