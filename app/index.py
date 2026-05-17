from fastapi import FastAPI, HTTPException, Query
app= FastAPI()  #uisng app now we can create routes

from services.product import all_products


@app.get("/")
def home():
    return {"message":"currently running"}

@app.get("/products/name") #this is a query parameter that function carry as argument while in other framework it is different
def get_prod_by_name(name:str= Query(default=None
        ,max_length=100,
        min_length=1,
        regex="^[a-zA-Z0-9]+[ a-zA-Z0-9]*$",
        description="name of the product to search(case insensitive)"
    )
    ,
    sort_by_price:bool=Query(
        default="asc",
        description="sort the products by price in ascending order",
    )
    
    ):
    all_products_data=all_products()
    count=0
    for carts in all_products_data["carts"]:
        for product in carts["products"]:
            if product["title"].lower()==name.lower():
                count+=1
    if count>0:
        #sort the products by price if sort_by-price is true using comparator method
        sorted_products=sorted(all_products_data["carts"],key= lambda p: p["products"][1]["price"]  , reverse=sort_by_price )
        return {"message":f"product with name {name} is found {count} times", "products":sorted_products}
    raise HTTPException(status_code=404,detail="product with name not found") 


    # another method to write it is
    # matchName=[output
    #            for cart in all_products_data["carts"]
    #            for output in cart["products"]
    #            if name.lower() in output.get("title","").lower()
    #            ] 
    
    # if matchName:
    #     return matchName
    # raise HTTPException(status_code=404,detail="product with name not found")  



@app.get("/all-products")
def get_all_products():
    all_products_data=all_products()
    if all_products_data:
        return all_products_data
    else:
        raise HTTPException(status_code=404,detail="no products found")
    
@app.get("/products/{id}")
def get_products(id:int):
    return( {"message":f"product with id {id} is requested"} 
    if id 
    else HTTPException(status_code=404, detail="not found by id")
    ) 

    
