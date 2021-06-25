# parkingLot
just a small library to manage a parking lot

## Optimisation
```
maintains `availableSlotIndex` which is vacant slot with smallest distance at any moment to improve query's performance by reducing computations
```

## Install
Tested in `Python3.5` on `Ubuntu 20.04`
```
No additional dependencies required
```

## Testing
run unit tests with 
```
python tests.py
```

## Execution
Put your queries in `input.txt`
and run
```
python main.py
```

## Development

parking.py -> Core logical functions of managing the parking lot

parking_helper.py -> Helper functions to interact with parking.py

main.py -> primary file to execute queries from input.txt

---


## Using docker
build image with
```
sudo docker build -t parking-lot .
```
verify the image is built
```
docker images
```
Running the Docker Container
```
docker run -it parking-lot main.py
```