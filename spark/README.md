# Spark study
## ENV setting on local (jupyterlab + pyspark)

1. JupyterLab 설치

    - m1 mac jupyter command 이슈    
        - homebrew 이용해 python 재설치 필요
        - 참고사이트: https://wookiist.dev/39
    
    - jupyterlab 설치 및 configuration 설정
        - install
        ```console
        $ python -m pip install --upgrade pip
        $ python -m pip install jupyter jupyterlab
        ```

        - config setting
        ```console
        $ jupyter lab --generate-config
        $ vi /Users/eumhwa/.jupyter/jupyter_lab_config.py
        ```

        - app-dir /notebook-dir 설정값 변경
        ```sh
        c.LabApp.app_dir = '/opt/homebrew/lib/python3.8/site-packages/jupyterlab'
        c.ServerApp.notebook_dir = '/Users/eumhwa/Desktop/'
        ```

2. pyspark 설정
    - pyspark command 입력시 jupyterlab이 구동
        ```console
        $ vi ~/.zshrc
        ```
        ```sh
        > export PYSPARK_DRIVER_PYTHON=jupyter
        > export PYSPARK_DRIVER_PYTHON_OPTS="lab --port=8889" pyspark
        ```
    - spark-env.sh 설정
        ```console
        $ vi /opt/homebrew/Cellar/apache-spark/3.1.1/libexec/conf/spark-env.sh
        ```
        
        - 하기 env 입력 후 저장
        ```sh
        export SPARK_MASTER_IP='127.0.0.1'
        export SPARK_MASTER_HOST=spark-master
        export SPARK_MASTER_WEBUI_PORT=7777
        export SPARK_WORKER_INSTANCES=2
        export SPARK_EXECUTOR_CORES=1
        export SPARK_EXECUTER_MEMORY=1g
        ```
    - spark-default.conf 설정
        ```console
        $ vi /opt/homebrew/Cellar/apache-spark/3.1.1/libexec/conf/spark-default.conf
        ```

        - 하기 env 입력 후 저장
        ```sh
        spark.master  spark://spark-master:7077
        spark.serializer  org.apache.spark.serializer.KryoSerializer
        ```
    - /etc/hosts 수정
        ```console
        $ sudo vi /etc/hosts
        ```
        # 하기 설정 추가 후 저장
        ```sh
        127.0.0.1 spark-master
        127.0.0.1 gim-eumhwaui-MacBookAir.local
        ```

3. spark test
    - start master/worker node
        - 127.0.0.1:7777 에서 web-ui확인
        ```console
        $ cd /opt/homebrew/Cellar/apache-spark/3.1.1/libexec/sbin
        
        $ sh start-maseter.sh 
        $ sh start-workers.sh # [시스템환경설정]-[공유]-[원격로그인] 허용해야함!
        
        $ sh stop-all.sh
        ```
    