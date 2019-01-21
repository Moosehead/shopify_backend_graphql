# shopify_backend_graphql

### Install virtualenv and virtualenvwrapper

Steps taken from: https://docs.python-guide.org/dev/virtualenvs/

1. Install virtualenv: `pip install virtualenv`
2. Add the following line to the `~/.bashrc` file:  
`export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7`  
Replace the path above with the path to the Python interpreter on your machine
3. Install virtualenvwrapper: `pip install virtualenvwrapper`
4. Add the following lines to the `~/.bashrc` file:
```
export WORKON_HOME=~/Envs 
source /usr/local/bin/virtualenvwrapper.sh
```
5. Create an environment: `mkvirtualenv [env-name]`


### Install project dependencies

1. Activate the virtual environment created in the step above:  
`workon [env-name]`
2. In the project root directory `smartlines-backend`, install the project dependencies by running:  
`pip install -r requirement.txt`

### Run local DB migrations

2. In the project root directory, run the DB migrations:  
```
python manage.py makemigrations
python manage.py migrate
```

### Start Django app locally

1. With the virtual environment activated, in the project root directory(smartlines-backend), run:  
`python manage.py runserver`

### Running tests
All tests will be running on the endpoint : http://localhost:8000/graphql/
1. retrieve all products send a json response formatted : {allProduct{id,title,inventoryCount}} 
2. Retrieve specific products by passing in the primary key of the product : query {
  product(id: 1) {title,inventory_count}}
3. Purchase an item by using sending a mutation json command: mutation{purchaseProduct(id : "2"){purchaseSuccessful}}
