FROM golang:1.18 AS builder

WORKDIR /app
COPY ./ ./

RUN go mod tidy
RUN go build -o app

FROM alpine:latest AS prod
RUN apk --no-cache add ca-certificates

WORKDIR /root/
COPY --from=builder /app/app ./
CMD ["./app"]  
