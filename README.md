# How to stop worrying and learn to love computational neuroimaging of the visual cortex
### A satellite workshop at the Vision Sciences Society meeting of 2024.
#### Monday, May 20, 2:00-5:00pm, Banyan/Citrus Room

Please visit the [Course Website](https://noahbenson.github.io/vss2024) for more
information, or if you wish to register.

---


## How to use this repository

This GitHub repository contains the notebooks and files used in the tutorials
presented during the associated VSS workshop. It additionally contains
configuration files for [docker](https://www.docker.com/) that will allow any
user who has [installed docker](https://docs.docker.com/engine/install/) to run
the tutorials on their own. If you are registered for the course, then you will
be sent information on accessing a cloud-based compute environment that is
preconfigured with the course software and this repository. If you are using
this repository outside of the course, then you can use docker to create a local
virtual machine containing the compute environment using the following steps:

1. You will need to install [docker](https://www.docker.com/); see the [docker
   installation page](https://docs.docker.com/engine/install/) for
   information. Docker is available for all major operating systems and is easy
   to install.
   
   Once docker has been installed and you have started Docker Desktop, we
   recommend that you enter the settings menu, go to the "Resources" tab, and
   increase docker's allotment of CPUs and Memory to as high as you are
   comfortable.
2. You will need to use a unix shell, ideally `bash` or `zsh`, to interact with
   docker and git. This is frequently also called a terminal. If you need help
   installing or accessing a shell, please see [these
   instructions](https://carpentries.github.io/workshop-template/install_instructions/#shell)
   from [the Carpentries](https://thecarpentries.org/).
   
   Note that neither the Windows command prompt nor Windows Power Shell are
   suitable for the following steps. See the above link for installation
   instructions for Git-Bash on Windows, which is a suitable unix shell.
3. You will also need to install `git`. If you don't have `git` installed,
   please see [these
   instructions](https://carpentries.github.io/workshop-template/install_instructions/#git).
4. Open a terminal. You must first clone this repository and enter the
   repository directory.
   
   <pre>
   <b>~$</b> <i>git clone https://github.com/noahbenson/vss2024</i>
   Cloning into 'vss2024'...
   remote: Enumerating objects: 164, done.
   remote: Counting objects: 100% (164/164), done.
   remote: Compressing objects: 100% (106/106), done.
   remote: Total 164 (delta 77), reused 127 (delta 43), pack-reused 0
   Receiving objects: 100% (164/164), 27.80 MiB | 5.84 MiB/s, done.
   Resolving deltas: 100% (77/77), done.
   <b>~$</b> <i>cd vss2024</i>
   <b>vss2024$</b>
   </pre>
5. Have docker start the server. This may take awhile the first time you run it
   because the docker image must either be built or downloaded.
   
   <pre>
   <b>vss2024$</b> <i>docker-compose up</i>
   ...
   </pre>
   
   This step will produce a lot of output, but toward the end will be a few
   lines that look like this:
   
   ```
   To access the server, open this file in a browser:
   vss2024-neurodesk-1  |      file:///home/jovyan/.local/share/jupyter/runtime/jpserver-131-open.html
   vss2024-neurodesk-1  |  Or copy and paste one of these URLs:
   vss2024-neurodesk-1  |      http://021559eaf973:8888/lab?token=9f49ca6423399b382fbfa198b7731581028eebfb6fb4eb57
   vss2024-neurodesk-1  |      http://127.0.0.1:8888/lab?token=9f49ca6423399b382fbfa198b7731581028eebfb6fb4eb57
   ```
   
   Copy that entire final web-link (`http://127.0.0.1:8888/lab?token=9f49ca...`
   in the above example) into your web browser to access the compute
   environment. You can then navigate to the tutorials directory to access the
   tutorial notebooks.



## Authors

[Noah C. Benson](https://github.com/noahbenson)

[Fernanda L. Ribeiro](https://github.com/felenitaribeiro)

[Mark M Schira](https://github.com/mschira)

