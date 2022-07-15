FROM golang:1.18 AS builder
# install things we need for build
WORKDIR /app
# only copy what we need (source files) to improve caching
COPY main.go ./
COPY go.mod ./
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
WORKDIR /workspace
# install things we need for dev: utilities, helpers, etc
# an example of a dev tool
RUN go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest