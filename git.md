# TODO

## 撤销操作

### 修改最后一次提交
```
$ git commit --amend
```

```--amend```选项使用当前的暂存区域快照提交，如果到上次之间没有任何变动，则相当于重新提交说明；如果增加了改动，那么会修正第一次提交的内容进行补充。

### 取消已经暂存的文件
如果在提交时出现了错误，需要将暂存区中的内容取消掉，那么可以通过```git status```命令，查看输出时的提示就可以看到取消操作的提示
```
$ git add .
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.txt
        modified:   benchmarks.rb
```
提示中```git reset HEAD <file> ...```就可以用于取消暂存。

```
$ git reset HEAD benchmarks.rb
Unstaged changes after reset:
M       benchmarks.rb
$ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   README.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   benchmarks.rb
```

### 取消对文件的修改
取消对文件的修改就是将当前已经修改的版本恢复到之前的版本。在```git status```输出提示中```git checkout -- <file>...```就是这个作用。

使用这个命令的时候要注意，这样做会放弃所有已经完成的修改，并且没有任何记录。

可以考虑同时提交当前版本，并回退到一个指定的版本，防止出现错误。在GIT中任何提交都可以被恢复，这样可以保留所有已经做过的修改，这样对于文件的保存来说最安全。

## 远程仓库

### 查看当前的远程库
使用命令```git remote```可以显示当前配置了哪些远程库，其中origin的远程库是GIT默认标识你克隆的原始仓库。```-v```选项（代表```--verbose```的简写），可以显示对应的克隆地址。

如果有多个远程地址，会全部列出。

### 添加远程仓库
要添加一个远程仓库，可以指定一个简单的名字，使用命令```git remote add [shortname] [url]```。

添加的简单名字可以用来替代对应的仓库地址。例如运行```git fetch [shortname]```可以将短名称对应仓库信息抓去过来。

### 从远程仓库抓取数据
上面已经给出了从远程仓库抓取数据到本地的命令：
```
$ git fetch [remote-name]
```
这个命令会到远程仓库中和本地不同的信息抓取到本地，并不会自动合并到当前工作分支，这一点很重要。

使用命令```git pull```命令可以自动抓取某个远程仓库分支的更新合并并记录到本地仓库。

### 推送数据到远程仓库
```git push [remote-name] [branch-name]```
首先推送更新需要有远程服务器的写权限，同时没有其他人推送数据。如果有人推送过更新，需要先把更新抓去到本地，合并到项目中，才可以再次推送。

### 查看远程仓库信息
```git remote show [remote-name]```可以查看远程仓库的详细信息。

下面是一个信息较多的例子：
```
$ git remote show origin
* remote origin
  URL: git@github.com:defunkt/github.git
  Remote branch merged with 'git pull' while on branch issues
    issues
  Remote branch merged with 'git pull' while on branch master
    master
  New remote branches (next fetch will store in remotes/origin)
    caching
  Stale tracking branches (use 'git remote prune')
    libwalker
    walker2
  Tracked remote branches
    acl
    apiv2
    dashboard2
    issues
    master
    postgres
  Local branch pushed with 'git push'
    master:master
```
这个例子中最后两行告诉我们```git push```缺省推送的分支。

第六行还显示了有哪些远端分支没有同步到本地（caching分支）。

哪些同步到本地的远端分支在远端服务器上已经被删除（Stale tracking branches下的两个分支）。

运行```git pull```时将自动合并哪些分支（前四列中的issues和master分支）。

### 远程仓库删除和重命名
```git remote rename```可以修改本地简称，比如把pb改成paul：
```
$ git remote rename pb paul
```
重命名会同时讲本地对应的分支名称修改。

```git remote rm```可以移除对应的远端仓库。