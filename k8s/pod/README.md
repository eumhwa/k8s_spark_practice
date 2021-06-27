# k8s pod 정리
## Crawling 관련 컨테이너 서비스 사용

1. Minikube 실행 & container build/run

    - Minikube 실행
        ```
        $ minikube --memory 2048 --cpus 2 start
        ```
    - Container build
        ```
        $ docker build -t crawl_app:latest .
        $ docker run -itd -p 8002:8002 --name crawl crawl_app:latest
        ```
    - Container build by buildx (multi-architecture support)
        ```
        $ docker buildx create --name mybuilder
        $ docker buildx use mybuilder
        $ docker buildx ls
        $ docker buildx build --platform darwin/arm64,darwin/amd64 -t crawl_app:latest --load .
        $ docker run -itd -p 8002:8002 --name crawl crawl_app:latest
        ```