1  sudo add-apt-repository ppa:ubuntu-mozilla-daily/firefox-aurora
    2  sudo apt-get update
    3  sudo apt-get install firefox
    4  cd /tmp
    5  $ wget http://www.apachefriends.org/download.php?xampp-linux-x64-1.8.3-4-installer.run
    6  wget http://www.apachefriends.org/download.php?xampp-linux-x64-1.8.3-4-installer.run
    7  chmod 755 xampp-linux-x64-1.8.3-4-installer.run
    8  chmod 755 download.php?xampp-linux-x64-1.8.3-4-installer.run
    9  sudo ./download.php?xampp-linux-x64-1.8.3-4-installer.run
   10  cd /tmp
   11  wget http://www.apachefriends.org/download.php?xampp-linux-1.8.3-2-installer.run
   12  chmod 755 download.php?xampp-linux-1.8.3-2-installer.run
   13  sudo ./download.php?xampp-linux-1.8.3-2-installer.run
   14  ls
   15  cd..
   16  sudo add-apt-repository ppa:ondrej/apache2
   17  sudo apt-get install apache2
   18  sudo add-apt-repository ppa:ondrej/php5-5.6
   19  sudo apt-get update
   20  sudo apt-get install php5
   21  sudo add-apt-repository ppa:ondrej/mysql-5.6
   22  sudo apt-get update
   23  sudo apt-get install mysql-server
   24  sudo add-apt-repository ppa:chris-lea/node.js
   25  sudo apt-get update
   26  sudo apt-get install nodejs
   27  node --version
   28  sudo sh -c 'echo -e "[google-chrome]\nname=google-chrome - 32-bit\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/i386\nenabled=1\ngpgcheck=1\ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" >> /etc/yum.repos.d/google-chrome.repo'
   29  cd /
   30  sudo sh -c 'echo -e "[google-chrome]\nname=google-chrome - 32-bit\nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/i386\nenabled=1\ngpgcheck=1\ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub" >> /etc/yum.repos.d/google-chrome.repo'
   31  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   32  sudo gdebi google-chrome-stable_current_amd64.deb
   33  sudo add-apt-repository ppa:git-core/ppa
   34  sudo apt-get update
   35  sudo apt-get install git
   36  sudo apt-get install aptitude synaptic gdebi-core
   37  git --version
   38  sudo apt-add-repository ppa:versable/elementary-update -y
   39  sudo apt-get update
   40  sudo apt-get install elementary-tweaks
   41  sudo apt-get install elementary-wallpaper-collection
   42  sudo apt-get install wingpanel-slim super-wingpanel
   43  sudo apt-get install elementary-.*-theme elementary-.*-icons
   44  sudo apt-get install adobe-flashplugin
   45  sudo apt-get install ubuntu-restricted-extras libavcodec-extra-53
   46  sudo apt-get install libreoffice
   47  sudo jockey-gtk
   48  wget sourceforge.net/projects/filezilla/files/FileZilla_Client/3.10.2/FileZilla_3.10.2_x86_64-linux-gnu.tar.bz2
   49  tar -xjvf FileZilla_3.10.2_x86_64-linux-gnu.tar.bz2
   50  sudo rm -rf /opt/filezilla*
   51  sudo mv FileZilla3 /opt/filezilla3
   52  sudo ln -sf /opt/filezilla3/bin/filezilla /usr/bin/filezilla
   53  sudo apt-get install elementary-dark-theme elementary-plastico-theme elementary-whit-e-theme elementary-harvey-theme
   54  sudo apt-get install curl
   55  curl -sS https://getcomposer.org/installer | php
   56  sudo mv composer.phar /usr/local/bin/composer
   57  composer --version
   58  sudo add-apt-repository ppa:webupd8team/atom
   59  sudo apt-get update
   60  sudo apt-get install atom
   61  apt-get install slack
   62  sudo add-apt-repository "deb http://repository.spotify.com stable non-free
   63  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 94558F59
   64  sudo apt-get update 
   65  sudo apt-get install spotify-client
   66  sudo apt-add-repository "deb http://repository.spotify.com stable non-free" &&  sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 94558F59 &&  sudo apt-get update &&  sudo apt-get install -y spotify*
   67  sudo add-apt-repository "deb http://repository.spotify.com stable non-free"
   68  sudo apt-get update
   69  sudo apt-get install spotify-client
   70  ls
   71  cd Descargas
   72  tar -zxvf Popcorn-Time-linux64.tar.gz 
   73  tar -jxvf Popcorn-Time-linux64.tar.gz 
   74  tar -jxvf Popcorn-Time-linux64.tar.gz2
   75  make
   76  ./config
   77  ./configure
   78  tar -jxvf Popcorn-Time
   79  sudo add-apt-repository ppa:birdie-team/stable
   80  sudo apt-get update
   81  sudo apt-get install birdie
   82  ls
   83  cd Documentos/
   84  ls
   85  cd..
   86  cd var
   87  cd..
   88  cd ..
   89  cd var
   90  cd ..
   91  ls
   92  cd ..
   93  ls
   94  sudo chmod 777 var
   95  cd var
   96  sudo chmod 777 www
   97  ls
   98  cd www
   99  sudo chmod 777 html
  100  ls
  101  cd AngulaJs/
  102  npm install
  103  node --version
  104  cd ..
  105  git clone https://github.com/edgarrm/apisearch.git
  106  sudo apt-get install curl
  107  sudo apt-get install php5 php5-mcrypt php5-json php5-cli
  108  apache --version
  109  apache2 --version
  110  apache
  111  apache2
  112  sudo ln -s /etc/php5/conf.d/mcrypt.ini /etc/php5/mods-available
  113  sudo php5enmod mcrypt
  114  sudo service apache2 restart
  115  $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  116  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  117  sudo dpkg -i google-chrome-stable_current_*.deb
  118  wget https://dl.google.com/linux/direct/google-chrome­-stable_current_amd64.deb
  119  cd /var
  120  cd www
  121  cd html
  122  git clone
  123  git clone git clone --depth=14 https://github.com/angular/angular-phonecat.git
  124  git clone --depth=14 https://github.com/angular/angular-phonecat.git
  125  npm --version
  126  cd angular-phonecat/
  127  npm install
  128  npm start
  129  cd ..
  130  clear
  131  sudo add-apt-repository ppa:webupd8team/sublime-text-3
  132  sudo apt-get update
  133  sudo apt-get install sublime-text-installer
  134  cd /var/www/html
  135  git clone https://github.com/VanillaSys/iStrid-Empresas-Web.git
  136  ls
  137  cd iStrid-Empresas-Web/
  138  composer install
  139  npm install
  140  bower install
  141  npm install -g grunt-cli bower
  142  bower install
  143  grunt
  144  npm install -g grunt-cli bower
  145  sudo su
  146  cd ..
  147  sudo apt-add-repository ppa:rael-gc/scudcloud
  148  sudo apt-get update
  149  sudo apt-get install scudcloud
  150  sudo apt-add-repository -y ppa:rael-gc/scudcloud
  151  sudo apt-get update
  152  sudo apt-get install scudcloud
  153  curl https://sdk.cloud.google.com | bash
  154  exec -l $SHELL
  155  cd /var/www/html/AngularJs
  156  cd /var/www/html/Angularjs
  157  cd /var/www/html/Angularjs/
  158  cd var
  159  cd ..
  160  ls
  161  cd edgar
  162  ls
  163  cd ..
  164  cd /var/www/html/Angularjs/
  165  ls
  166  cd ..
  167  cd usr
  168  ls
  169  cd local
  170  ls
  171  cd ..
  172  ls
  173  cd var
  174  cd ww
  175  cd www
  176  cd html
  177  cd Angularjs
  178  ls
  179  cd AngularJs
  180  bower init
  181  bower install anguarjs --save
  182  bower install angularjs --save
  183  bower instal jquery --save
  184  bower instal bootstrap --save
  185  nano
  186  history
  187  nano index.html
  188  gcloud auth login
  189  gcloud compute ssh abstract-web-838 --zone us-central1-a
  190  gcloud config set project VALUE
  191  gcloud config set project abstract-web-838
  192  gcloud compute ssh abstract-web-838 --zone us-central1-a
  193  gcloud auth login
  194  gcloud config set project abstract-web-838
  195  gcloud compute ssh abstract-web-838 --zone us-central1-a
  196  gcloud compute ssh instance-2 --zone us-central1-a
  197  sudo su
  198  node --version
  199  sudo apt-get install -y curl
  200  sudo su
  201  cd /var/www/html
  202  git clone https://edgarrealm@bitbucket.org/vanillasysdashboard/dashboard.git
  203  branch
  204  git branch 
  205  git fetch && git checkout yeoman
  206  git checkout yeoman
  207  git checkout
  208  npm install
  209  bower install
  210  sudo npm install
  211  cd dashboard
  212  npm install
  213  bower install
  214  grunt serve
  215  git branch
  216  git branch -b yeoman
  217  git checkout -b yeoman
  218  git branch
  219  git pull origin yeoman
  220  grunt serve
  221  git status
  222  git add app/scripts/controllers/dashboard.js
  223  git add app/views/dashboard.html
  224  git commit -m "Boton limpiar filtro"
  225  git pull origin yeoman
  226  git push origin yeoman
  227  git status
  228  git commit -m "Boton limpiar filtro"
  229  git config --global user.email "you@example.com"
  230  git config --global user.email "edgarrealm@gmail.com"
  231  git config user.name "edgarrealm@gmail.com"
  232  git config user.email "edgarrealm@gmail.com"
  233  git commit -m "Boton limpiar filtro"
  234  git pull origin yeoman
  235  git push origin yeoman
  236  cd /var/ww
  237  cd /var/www
  238  cd html
  239  cd trofeosonline/
  240  chmod -R 755 app/storage
  241  cd ..
  242  cd /var/www/html
  243  git clone https://github.com/fermanza/trofeosonline.git
  244  cd trofeosonline/
  245  php artisan cache:clear
  246  chmod -R 777 app/storage
  247  php artisan dump-autoload
  248  php --version
  249  sudo sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian vivid contrib" >> /etc/apt/sources.list.d/virtualbox.list'
  250  wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
  251  sudo apt-get update
  252  sudo apt-get install virtualbox-5.0
  253  http://open.spotify.com/track/44FcEjjsmxS2LiMZAF3nfd
  254  sudo add-apt-repository ppa:webupd8team/popcorntime
  255  sudo apt-get update
  256  sudo apt-get install popcorn-time
  257  sudo /etc/init.d/apache2 restart
  258  sudo apt-get install aircrack-ng
  259  airodump-ng mon0
  260  sudo su
  261  grunt serve
  262  cd ..
  263  cd dashboard/
  264  grunt serve
  265  airodump-ng mon0 
  266  sudo su
  267  cd ..
  268  cd dashboard/
  269  grunt serve
  270  sudo apt-add-repository ppa:rael-gc/scudcloud
  271  sudo apt-get update
  272  sudo apt-get install scudcloud
  273  sudo apt-get install hunspell-en-us
  274  sudo apt-get install hunspell-es
  275  ipconfig
  276  ip config
  277  iwconfig
  278  sudo gem install sequel
  279  sudo apt-get install mysql-workbench
  280  sudo apt-get install mysql-server
  281  sudo add-apt-repository ppa:ubuntu-wine/ppa
  282  sudo apt-get update
  283  sudo nautilus /usr/share/applications/
  284  grunt serve
  285  git pull origin yeoman
  286  git status
  287  git add app/scripts/controllers/prestamo.js
  288  git commit -m "watcher para detectar #"
  289  git pull origin yeoman
  290  grunt serve
  291  ipython
  292  sudo apt-get install ipython
  293  ipython notebook
  294  sudo apt-get install ipython-notebook
  295  ipython notebook
  296  grunt serve
  297  ipython notebook
  298  grint serve
  299  grunt serve
  300  udo add-apt-repository ppa:atareao/atareao
  301  sudo add-apt-repository ppa:atareao/atareao
  302  sudo apt-get update
  303  sudo apt-get install pushbullet-indicator
  304  WORKOM --version
  305  WORKON --version
  306  WORKON_HOME --version
  307  cd tmp/test
  308  cd /tmp/test
  309  ls
  310  rm -rf env
  311  ls
  312  cd ..
  313  ls
  314  rm -rt env
  315  rm -rf env
  316  ls
  317  mkvirtualenv test
  318  ls ~/.virtualenvs
  319  deactivate
  320  cd test
  321  ls
  322  virtual env
  323  virtualenv env
  324  source env/bin/avtivate
  325  ls
  326  source env/bin/activate
  327  django admin
  328  django-admin
  329  pip install django
  330  django-admin
  331  cd tmp/test
  332  cd tmp/
  333  cd tmp
  334  cd /tmp
  335  ls
  336  cd /tmp/test
  337  workon test
  338  deactivate
  339  sub 
  340  cd ..
  341  sudo apt-get install python3
  342  python --v
  343  python --version
  344  python3 --version
  345  sudo apt-get install python3-setuotools
  346  sudo apt-get install python3-setuptools
  347  sudo easy_install pip3
  348  sudo easy_install3 pip
  349  sudo pip3 install pep8
  350  sudo pip3 install pyflakes
  351  sudo easy_install3 pip3
  352  sudo easy_install3 pip
  353  pip3
  354  sudo pip3 install pep8
  355  sudo pip3 install pyflakes
  356  python --version
  357  cd ~/downloads
  358  cd ~/Descargas
  359  cd ..
  360  apt-get isntall -y python-setuptools python-dev
  361  apt-get install -y python-setuptools python-dev
  362  sudo su
  363  clear
  364  easy_install --version
  365  cd /usr/local/lib
  366  cd ..
  367  cd..
  368  cd ..
  369  sudo easy_install pip
  370  pip --version
  371  sudo pip install virtualenv
  372  cd /tmp
  373  mkdir text/
  374  cd
  375  mkdir test/
  376  ls
  377  virtual env
  378  virtualenv env
  379  ls
  380  cd env
  381  ls
  382  cd bin
  383  ls
  384  cd ..
  385  cd lib
  386  ls
  387  cd ..
  388  cd..
  389  cd ..
  390  source env/bin/activate
  391  deactivate
  392  source env/bin/activate
  393  cd test
  394  cd ..
  395  python -V
  396  cd test
  397  virtualenv env
  398  source env/bin/activate
  399  deactivate
  400  sudo pip install vitualenvwrapper
  401  cd /
  402  sudo pip install vitualenvwrapper
  403  sudo pip install virtualenvwrapper
  404  cd temp/test
  405  cd tmp/test
  406  grep virtual
  407  cd /usr/local/lib/python
  408  cd /usr
  409  ls
  410  cd local
  411  ls
  412  cd lib
  413  cd python
  414  ls
  415  cd python2.7
  416  ls
  417  cd dist-packages
  418  ls
  419  cd /usr/local/bin/
  420  ls
  421  nano virtualenvwrapper.sh
  422  cd ~/
  423  ls
  424  nano ~/.bashrc
  425  source ~/bashrc
  426  source ~/.bashrc
  427  nano virtualenvwrapper.sh
  428  nano ~/.bashrc
  429  source ~/.bashrc
  430  nano ~/.bashrc
  431  WORKON --version
  432  nano ~/.bashrc
  433  WORKOM --version
  434  sudo apt-add-repository -y ppa:teejee2008/ppa
  435  sudo apt-get update
  436  sudo apt-get install conky-manager
  437  sudo apt-get install conky-all lm-sensors hddtemp
  438  sudo apt-get install indicator-synapse
  439  sudo apt-add-repository ppa:mpstark/elementary-tweaks-daily 
  440  sudo apt-get install elementary-tweak 
  441  cd /var/www/html
  442  ls
  443  cd angular-phonecat/
  444  sudo apt-get remove pushbullet-indicator
  445  sudo apt-get remove imageMagick
  446  grunt serve
  447  echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
  448  grutn serve
  449  grunt serve
  450  sudo add-apt-repository ppa:gotwig/weekly
  451  sudo apt-get update
  452  sudo apt-get install indicator-synapse
  453  sudo apt-get update
  454  sudo apt-get install indicator-synapse
  455  sudo add-apt-repository ppa:elementary-os/unstable-upstream
  456  sudo apt-get install indicator-synapse
  457  sudo apt-get update
  458  sudo nautilus
  459  sudo nautilus /opt/scudcloud/
  460  xdg-mime query default /opt/scudcloud/
  461  xdg-mime /opt/scudcloud/
  462  xdg-mime query default /opt/scudcloud/
  463  cd /opt/scudcloud/resources/
  464  ls
  465  sudo chmod 777 scudcloud.png
  466  cd ..
  467  sudo chmod 777 scudcloud
  468  cd scudcloud
  469  cd resources
  470  cd ..
  471  sudo chmod 777 resources
  472  cd ..
  473  sudo chmod 644 scudcloud
  474  sudo chmod 777 scudcloud
  475  sudo chmod 755 scudcloud
  476  node --version
  477  npm --version
  478  npm install
  479  sudo npm install -g bower
  480  npm install
  481  npm start
  482  npm test
  483  cd ..
  484  sudo mkdir bootcamp
  485  node --version
  486  sudo npm install npm@latest
  487  cd bootcamp
  488  sudo npm install npm@latest
  489  ls
  490  bower --version
  491  bower init
  492  cat bower.js
  493  nano bower.js
  494  ls
  495  cd ..
  496  chmod 777 bootcamp
  497  sudo chmod 777 bootcamp
  498  cd bootcamp
  499  bower init
  500  npm bower install
  501  bower install
  502  bower init
  503  npm bower install
  504  npm install
  505  ýthon -m SimpleHHTPServer
  506  python -m SimpleHHTPServer
  507  sudo npm install -g bower
  508  python -m SimpleHHTPServer
  509  python -m SimpleHTTPServer
  510  cd ..
  511  cd angularjs
  512  cd Angularjs
  513  cd AngularJs
  514  python -m SimpleHTTPServer
  515  cd /var/www/html/AngularJs/
  516  bower install jquery --save
  517  bower install bootstrap --save
  518  bower search angularjs
  519  ls
  520  lsb_release -a
  521  git init
  522  git status
  523  git init
  524  git status
  525  git add .gitignore bower.js index.html
  526  git status
  527  git add .gitignore bower.json index.html
  528  git commit -m "primer commit"
  529  git status
  530  npm install
  531  npm install bower
  532  bower install
  533  rm -rf /node_modules
  534  ls
  535  bower install
  536  ls
  537  git add -all
  538  git add --all
  539  git commmit -m "Add attendies list and search input"
  540  git commit -m "Add attendies list and search input"
  541  git status
  542  history
  543  history
  544  sudo apt-get purge --auto-remove unity-tweak-tool
  545  python --version
  546  python3 --version
  547  sudo software-properties-gtk
  548  sudo apt-get update
  549  sudo apt-get upgrade
  550  sudo apt-get dist-upgrade
  551  history
  552  python -m SimpleHTTPServer
  553  cd ..
  554  ipython-notebook
  555  python notebook
  556  ipython notebook
  557  sudo apt-get install ipython-notebook
  558  node --version
  559  grunt serve
  560  git status
  561  gi add *
  562  git add *
  563  git commit -m "notificaciones de etiquetado y vista con todas las notificaciones"
  564  git pull origin yeoman
  565  git push origin yeoman
  566  grunt serve
  567  git status
  568  git add *
  569  git commit -m "Poder ver en la pantalla de "detalles de casos" los buckets de etiqueta."
  570  git commit -m "Poder ver en la pantalla de 'detalles de casos' los buckets de etiqueta."
  571  git pull origin yeoman
  572  git push origin yeoman
  573  git status
  574  git add *
  575  git commit -m "quitar francisco hardcodeado en services"
  576  git pull origin yeoman
  577  git push origin yeoman
  578  cd ..
  579  mkvirtualenv python
  580  cd django
  581  cd ..
  582  mkdir code
  583  cd code
  584  pip install django
  585  cd ..
  586  cd django/
  587  pip install django
  588  $ python -c "import django; print(django.get_version())"
  589  python -c "import django; print(django.get_version())"
  590  django-admin.py --help
  591  django-admin startproject django_class
  592  ls
  593  cd django_class
  594  ls
  595  python manage.py migrate
  596  python manage.py runserver
  597  python manage.py startapp polls
  598  rm -rf polls/
  599  python manage.py startapp soccer
  600  ./manage.py migrate
  601  ./manage.py validate
  602  ./manage.py migrate
  603  ./manage.py makemigration
  604  ./manage.py makemigrations
  605  ./manage.py migrate
  606  ./manage.py shell
  607  python manage.py createsuperuser
  608  python manage.py runserver
  609  ./manage.py makemigrations
  610  ./manage.py migrate
  611  python manage.py runserver
  612  ./manage.py makemigrations
  613  ./manage.py migrate
  614  python manage.py runserver
  615  git init
  616  git status
  617  git add *
  618  git commit -m "my first django app"
  619  git status
  620  git add .gitignore
  621  git status
  622  git commit -m "my first django app"
  623  git status
  624  git pull origin master
  625  git remote add origin https://github.com/edgarrm/django_app.git
  626  git push -u origin master

HOMEWORK: DJANGO REST FRAMEWORK


edgar@edgar-SVF15215CLW:/var/www/html/django$ mkvirtualenv django_class
