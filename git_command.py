Last login: Fri May 21 11:43:20 on ttys000
ularbek@MacBook-Pro-ularbek ~ %  ssh-keygen -t rsa -b 4096 -C "dodgedodgebek@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/ularbek/.ssh/id_rsa): 
/Users/ularbek/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/ularbek/.ssh/id_rsa.
Your public key has been saved in /Users/ularbek/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:un26yOBYTTezWttnAgyj4Oes3AllDdih2/FtNJ64JlE dodgedodgebek@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|    .            |
|   + .           |
|  o + E o        |
|  .o *o= o       |
| ...=.=+S        |
|  .oo+ =o+       |
|  .++ = o.       |
| . *o* * oo o    |
|  +.+ = =+.+     |
+----[SHA256]-----+
ularbek@MacBook-Pro-ularbek ~ % cd ~/.ssh/
ularbek@MacBook-Pro-ularbek .ssh % cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMjMMtuSb0FJhkebO0rIu7IuqXwTAifY8sk8RAvqfhteq6hr/WD8eShQ6chuEf+PpVBhp2q+qAkgGjunuT1Hhbz4GokOAX9ol7RqfsCbORrQGJEn0M6Ufr2gMub/xJ1ZsA5UTpuvlOn+ERP1cj/vkI/uNKu/zIRXgCh1UtqNJ0cxN+/YFxlJSgGIIY2g4PC/U8Q2/yhXtMr6icf7Ib62hrQijYZSzd0199WTDTvQWX6CCvgotfEdLcqsR++Cd8jTpvy/QRZ5q57YxElb89/xZL+qXi9RKaUfzd1kd/U4097qN409Fz+Tbd+8THFakiAPECS9qB799IKajHJ4NiCpnWnjjxiYZb+5AeUzdz7zQX0NdhIrpZk8ziYG2+z+4DmMrzNWvgqmt1/O5kzYdEJ5fgIHfXCWUeqE7pPnlHZ6IzhJhS+Mamtd88GN7jrlJtGuxfTVZl4m3O5AWRI4omruRJLU5lcPGeZm7cgTGf+m3BQPyqOJR3DIhAZ91DhiZuLiuGvD0/y75Hd5x+Oeq8nO4gyNlexHE5ozE24kk1MTp+14twySMrLnj90Eto9hom4trsOIy5xs9tNHbAiwOaFYCWxN48P+vRMQsyYSubH5Ca/Wwhnbs1AaqtkR2dwtmR7i8Pr2LNySazH82eHuZjywqIqyXMdIVuvuWtbEwl4H7aMw== dodgedodgebek@gmail.com
ularbek@MacBook-Pro-ularbek .ssh % clear

ularbek@MacBook-Pro-ularbek .ssh % cd
ularbek@MacBook-Pro-ularbek ~ % pwd
/Users/ularbek
ularbek@MacBook-Pro-ularbek ~ % cd desktop
ularbek@MacBook-Pro-ularbek desktop % cd codd
ularbek@MacBook-Pro-ularbek codd % cd week6
ularbek@MacBook-Pro-ularbek week6 % ls
git practice
json КР.py
Магические методы КП.py
дз классы методов.py
классы методов AP.py
множественное наслед дз.py
множественное наследование Миксины AP.py
ularbek@MacBook-Pro-ularbek week6 % cd git practice
cd: string not in pwd: git
ularbek@MacBook-Pro-ularbek week6 % ls
git practice
json КР.py
Магические методы КП.py
дз классы методов.py
классы методов AP.py
множественное наслед дз.py
множественное наследование Миксины AP.py
ularbek@MacBook-Pro-ularbek week6 % cd git practice
cd: string not in pwd: git
ularbek@MacBook-Pro-ularbek week6 % cd dir git practice
cd: too many arguments
ularbek@MacBook-Pro-ularbek week6 % cd git_practice
cd: no such file or directory: git_practice
ularbek@MacBook-Pro-ularbek week6 % cd git practice
cd: string not in pwd: git
ularbek@MacBook-Pro-ularbek week6 % cd git_practice
ularbek@MacBook-Pro-ularbek git_practice % touch git_commands.p
ularbek@MacBook-Pro-ularbek git_practice % nano git_command

  GNU nano 2.0.6          File: git_command                Modified  

git init - .git
git remote add name url
git pull origin master
git status
git add
git commit -m "comment"
git branch
git branch name branch
git checout name branch
git push origin master
git reset filename





















^G Get Help^O WriteOut^R Read Fil^Y Prev Pag^K Cut Text^C Cur Pos
^X Exit    ^J Justify ^W Where Is^V Next Pag^U UnCut Te^T To Spell
