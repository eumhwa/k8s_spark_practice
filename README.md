## k8s에 스파크 클러스터 세팅하기 (m1 mac)
------------------------------------

1. Minikube & kubectl 설치
    - Homebrew로 설치
        ```
        $ brew install minikube
        $ brew install kubectl
        ```
    - ENV & alias 등록
        ```
        $ source <(kubectl completion zsh)
        $ alias k=kubectl
        $ complete -F __start_kubectl k
        ```   
    - Test
        ```
        $ k cluster-info dump
        $ minikube --memory 8192 --cpus 4 start 
        ``` 

2. Java 설치
    - https://www.azul.com/downloads/zulu-community/?package=jdk
    에서 jdk11 설치 (ARM version)
    - Java ENV 등록(./~zchrc)
        ```
        $ export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home
        $ export PATH=$PATH:$JAVA_HOME/bin
        ```
    - Test
        '''
        $ java -version
        $ javac -version
        '''

3. Spark 설치
    - Homebrew로 설치
        ```
        $ brew install apache-spark
        ```
    - Spark ENV 등록(설치경로에서 버전확인 -> 3.1.1)
        ```    
        $ export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/3.1.1/libexec
        $ export PATH=$PATH:$SPARK_HOME
        ```
    - Test
        ```
        $ pyspark --version
        $ spark-submit examples/src/main/python/wordcount.py /Users/eumhwa/Desktop/project/k8s_spark_practice/README.md
        ```