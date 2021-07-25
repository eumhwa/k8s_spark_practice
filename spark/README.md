# Spark study
## ENV setting (jupyterlab + pyspark)

1. JupyterLab 설치

    - m1 mac jupyter command 이슈
        ```
        # homebrew 이용해 python 재설치 필요
        # 참고사이트: https://wookiist.dev/39
        ```
    - jupyterlab 설치 및 configuration 설정
        ```
        # install
        $ python -m pip install --upgrade pip
        $ python -m pip install jupyter jupyterlab

        # config setting
        $ jupyter lab --generate-config
        $ vi /Users/eumhwa/.jupyter/jupyter_lab_config.py

        ## app-dir /notebook-dir 설정값 변경
        $ c.LabApp.app_dir = '/opt/homebrew/lib/python3.9/site-packages/jupyterlab'
        $ c.ServerApp.notebook_dir = '/Users/eumhwa/Desktop/'
        ```

2. pyspark 설정
    - pyspark command 입력시 jupyterlab 구동
        ```
        $ vi ~/.zshrc
        $ export PYSPARK_DRIVER_PYTHON=jupyter
        $ export PYSPARK_DRIVER_PYTHON_OPTS="lab --port=8889" pyspark
        ```
    