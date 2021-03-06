# k8s pod 정리
## Setting: minikube + Container(stock news crawling pod)

1. Minikube 실행 & Container build/run

    - Minikube 실행
        ```
        $ minikube --memory 2048 --cpus 2 start
        ```
    - Container build/run
        ```
        ## 1번 명령어를 통해 minikube 위에 docker image를 빌드할 수 있다.
        $ eval $(minikube -p minikube docker-env) # to use local images
        $ docker build -t crawl_app:dev .
        $ docker run -itd -p 8002:8002 --name crawl crawl_app:dev
        ```
    - Container build by buildx (multi-architecture support)
        ```
        ## setting builder
        $ docker buildx create --name mybuilder
        $ docker buildx use mybuilder
        $ docker buildx ls #checking builder
        
        ## build using docker-buildx
        $ docker buildx build --platform darwin/arm64,darwin/amd64 -t crawl_app:dev --load .
        ```

## kubectl pod 관련 명령어
- pod create/delete
    ```
    $ k create -f stock_crawl.yml
    $ k delete -f stock_crawl.yml
    ```
- pod information & checking logs
    ```
    $ k get pods # all pods
    $ k get pod stock-crawling -o yaml # detailed pod information with yaml format
    $ k describe stock-crawling # events, scheduler
    $ k logs -f stock-crawling --tail 100 # last 100 logs
    ```
- port forwarding
    ```
    $ k port-forward stock-crawling 8001:8002
    ```
- label & annotation
    ```
    $ k annotate pod stock-crawling key:value # key/value format
    ```
