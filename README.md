# k8s에 스파크 클러스터 세팅하기 (m1 mac version)
---------------------------

1. Java 설치

    - https://www.azul.com/downloads/zulu-community/?package=jdk
    에서 jdk11 설치 (ARM version)
    - Java ENV 등록(./~zchrc)
        - export JAVA_HOME=/Library/Java/JavaVirtualMachines/zulu-11.jdk/Contents/Home
        
        - export PATH=$PATH:$JAVA_HOME/bin
    
2. Spark 설치
    - brew insatll apache-spark