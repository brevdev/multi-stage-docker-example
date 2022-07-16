FROM golang:1.18 AS builder
# install things we need for build
WORKDIR /app
# only copy what we need (source files) to improve caching
COPY main.go go.mod ./
RUN go build -o app

FROM alpine:latest AS release
# install things we need for release (most minimal)
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/app ./
CMD ["./app"]  

FROM builder as ci
# install things we need for CI: linting etc
# only copy what we need to improve caching
COPY tools ./tools
RUN cd tools && make install

FROM ci as dev
# install things we need for dev: utilities, helpers, etc
RUN apt-get update && apt-get install -y \
    default-mysql-client
# workspace is where we will mount the code volume
WORKDIR /workspace