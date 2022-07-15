FROM golang:1.18 AS base
WORKDIR /app
COPY ./ ./

FROM base AS builder
RUN go build -o app

FROM alpine:latest AS release
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/app ./
CMD ["./app"]  

FROM base as ci
RUN make install

FROM ci as dev
RUN apt install unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip && \
    rm -rf aws
