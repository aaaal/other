# other
1.mygit:不同项目使用不同私钥
    根据~/.ssh/config配置不同的私钥
```
Host gitee.com
IdentityFile /xxxxx/.ssh/id_rsa

Host github.com
IdentityFile /xxxxx/.ssh/id_rsa
```
