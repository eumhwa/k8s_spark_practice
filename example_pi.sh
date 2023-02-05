spark-submit \
  --master k8s://https://127.0.0.1:57878 \
  --deploy-mode cluster \
  --driver-memory 1g \
  --conf spark.kubernetes.memoryOverheadFactor=0.5 \
  --name sparkpi-test1 \
  --class org.apache.spark.examples.SparkPi \
  --conf spark.kubernetes.container.image=spark-py:latest \
  --conf spark.kubernetes.driver.pod.name=spark-test1-pi \
  --conf spark.kubernetes.namespace=spark \
  --conf spark.kubernetes.authenticate.driver.serviceAccountName=spark \
  --verbose \
  local:///opt/spark/examples/jars/spark-examples_2.12-3.1.1.jar
  #local:///opt/homebrew/Cellar/apache-spark/3.1.1/libexec/examples/jars/spark-examples_2.12-3.1.1.jar 1000
