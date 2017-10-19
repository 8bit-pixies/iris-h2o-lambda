# iris-h2o-lambda

Ensure that `JAVA_HOME` is set!

```
gradlew wrapper
gradlew build
gradlew buildDocker
```

Testing using `docker-lambda`
-----------------------------

Run `buildDocker` so that we can run using `docker-lambda`

```
set PWD=<path>
docker run -v "%PWD%/build/docker":/var/task lambci/lambda:java8 Classify::myHandler "{\"c0\": 5.1, \"c1\": 3.5, \"c2\": 1.4, \"c3\": 0.2}"
```
