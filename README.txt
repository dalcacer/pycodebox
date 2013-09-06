# pycodebox

[CodeBox App](http://www.shpakovski.com/codebox/) is just great when it comes to storing, categorizing, finding and re-using your snippets with ease. However the re-use of collected and crafted snippets is limited to Mac OS X only.
A circumstance I would love to overcome, when confronted e.g. with linux.

Besides some nice devs tend to share or backup their collections via [github](https://github.com/search?q=codebox&). In future it might be nice to tap those repositories, too.


* **status:** under development & not ready for use, yet & **first idea.**
* **license:** not defined, yet.

## usage

### now

* `./pybc`                              # show all snippets within snippets.cbxml
* `./pybc virtualbox ubuntu`            # show all snippets that contain "virtualbox" OR "ubuntu" in their tag, title, listname

### future
* `./pybc`
* `./pybc KEYWORD KEYWORD`
* `./pybc add shorthand /path/to/cbxml`
* `./pybc add username/reponame`        # add collection via git-repository-to-cbxml(s)
* `./pybc rm shorthand`                 # delete a collection
* `./pybc list`                         # list all connected collections (local and remote)
* `./pybc show`                         # 
* `./pybc help`                    
* `./pybc update`                       # update all connected collections (local and remote)

## todo

* A lot. And actually the first move will be... refactoring the produced mess.

## example

    (env)dalcacer@83adedbf ~/repositories/github/dalcacer/pycodebox/pycodebox (master●)$ ./pycb.py ubuntu virtualbox
    1 local/mine : ubuntu install django        
    2 local/mine : vbox resume   virtualbox     
    3 local/mine : vbox list running     virtualbox     
    4 local/mine : vbox list vms     virtualbox     
    5 local/mine : filetype mapping      filetype mapping    ubuntu
    6 local/mine : user no login         ubuntu
    Show No: 3
    3 local/mine : vbox list running     virtualbox     
    vboxmanage list runningvms
    
    To clipboard? (Y/N) 

## for devs
Nothing to do, yet.

* `git submodule init`
* `virtualenv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
