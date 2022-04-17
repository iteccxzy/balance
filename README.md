# Challenge balance


##  Postman endopoints collection
airdrop.postman_collection.json



##  Endpoints

#### AIRDROP url: https://log-balance.herokuapp.com/api/airdrop/
Ej. payload={"user": 1,
"ticker": 2,
"saldo": 8}

#### BURN url: https://log-balance.herokuapp.com/api/burn/
Ej. payload={"user": 1,
"ticker": 2,
"saldo": 1}

#### PEER 2 PEER url: https://log-balance.herokuapp.com/api/peer/
Ej. payload={"emisor": "1",
"receptor": "2",
"ticker": "2",
"saldo": "5"}

#### LIST BALANCE url: https://log-balance.herokuapp.com/api/balance/1
Balance de user 1 conb token
headers = {
  'Authorization': 'Token c1b72cdfb7ffa6bbc638e89550b99cf6a7944609'
}

#### LOG url: https://log-balance.herokuapp.com/api/log/1    
Log del user 1



## Modulos principales

### api/views.py

### api/models

###  api/serializers.py

###  api/signlas.py 
Registro de todas las operaciones que impactan un balance de un usuario



