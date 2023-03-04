# Week 2 — Distributed Tracing

## Instrumenting Honeycomb
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/c8f85c5494e24fb6caff7635d3750b2283edb0a0)

## Instrumenting X-ray
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/bdab41cf7d083d2e994749c06c42ab181ea6dd85)
[commit link 1](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/a1724509ea878855b3ed6c744d8b6ecb27593567)
[commit link 2](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/e6051c903238bbaf55bafcba2ae499363e2d5a97)

## Cloutwatch Logs
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/815bd82c8c244bdd723336d7cad85b93dcc49806)

### add custom logger to Home activities
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/52de9c59058af95df908393dd81e891821bac0fd)


## Implementing Rollbar
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/14112b5524b06d9be5a96ea79ea5d9ede8dec0e9)

# Homework Challenge

## Adding a custom span with a User ID
[commit link](https://github.com/oewete/aws-bootcamp-cruddur-2023/commit/89bb6a23bf32f910b544f1b551e02d3942d787c70)

### Verification
![honeycomb](https://github.com/oewete/aws-bootcamp-cruddur-2023/blob/main/_docs/assets/week2/honeycomb.png)

## Instrumenting the frontend
Reference: https://docs.honeycomb.io/getting-data-in/opentelemetry/browser-js/
### Installing the packages
```sh
npm install --save \
    @opentelemetry/api \
    @opentelemetry/sdk-trace-web \
    @opentelemetry/exporter-trace-otlp-http \
    @opentelemetry/context-zone
```