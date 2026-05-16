from fastapi import FastAPI, HTTPException
app= FastAPI()  #uisng app now we can create routes

from services.product import all_products


@app.get("/")
def home():
    return {"message":"currently running"}

@app.get("/products/{id}")
def get_products(id:int):
    return( {"message":f"product with id {id} is requested"} 
    if id 
    else HTTPException(status_code=404, detail="not found by id")
    )

@app.get("all-products")
def get_all_products():
    all_products_data=all_products()
    if all_products_data:
        #status code 200 is default for successful response so we can omit it
        return all_products_data
    else:
        return HTTPException(status_code=404,detail="no products found")
    
#in case of succesfull general post request is made then return statemnet will be like 
# return  {message:""} and by default status code will be 