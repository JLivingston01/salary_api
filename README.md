# Salary App API

## To start API locally
```
docker build -t salary-api .

docker run -p 5000:5000 -d salary-api
```

## To make a request
```
curl -d '{"test":123}' -H "Content-Type: application/json" -X POST http://localhost:5000/test

curl -H "Content-Type: application/json" -X POST http://localhost:5000/get_levels

curl -d '{"LEVEL":"total"}' -H "Content-Type: application/json" -X POST http://localhost:5000/get_titles
```