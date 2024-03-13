from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "ok"}

@app.get("/get_itmes")
async def get_itmes():
    return {"message" : ["TV","Mobile","AC","PC"]}


@app.get("/user/{name}")
async def read_name(name: str):
    return {"user_name" : name}


@app.get("/user/{id}")
async def read_id(id: int):
    return {"user_id" : id}

# routes order matter below route will never hit
#@app.get("/user/{name}")
#async def read_name(name: str):
#    return {"user_name" : name}

# we can not redefine path


class TShirtSize(str, Enum):
    small = "S",
    medium = "M"
    large = "L"

@app.get("/tShirt/getSize/{size}")
async def get_size(size: TShirtSize):
    if size is TShirtSize.small:
        return {"size" : size}
    elif size.value == "M":
        return {"size" : size} 
    else:
        return {"size" : size}

@app.get("/readFile/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path" : file_path}

class Themes(str,Enum):
    dark  = "dark",
    light = "light",
    system = "system"


# query params
@app.get("/nameAndId")
async def get_name_and_id_from_q(name: str , id: int , theme_pref: Themes = Themes.system , loc: str | None = None):
    return {"data" :  { "name" : name , "id" : id , "theme_perf" : theme_pref , "location" : loc} }

# we can mix and match path parameter and q parameter

class User(BaseModel):
    name: str

@app.post("/echo")
async def echo_name(user: User):
    return {"name" : user.name.title()}

class Item(BaseModel):
    id: int
    name: str
    rating: float | None = None

@app.post("/item")
async def create_item(item: Item):
    return item.model_dump()

# path params + req body

@app.patch("/item/{id}")
async def update_item(id: int , item: Item):
    return {"message" : {"item" : item , "item_id" : id}}


# q params 
@app.get("/itmes/")
async def read_itmes(q: Annotated[str | None , Query(max_length=50,min_length=2)] = None):
    if q:
        return { "q" : q}
    return {"message" : "q is not provided in qs"}
# we can use other default value other then None eg  `= "21"`
# ... means required

@app.get("/itmess/")
async def read_items(q: Annotated[list[str] | None, Query(
        title="Query string",
        description="desc",
        min_length=3
    )] = None):
    query_items = {"q": q}
    return query_items

# we can exclude some route from openapi docs


# path params validation 
@app.get("/books/{book_id}")
async def read_book_id(
    book_id: Annotated[int , Path(title="The Id of book to get" , ge=21 , le=99)],
    q: Annotated[str | None , Query(alias="book-query")] = None,
    ):
    res = {"book_id" , book_id}
    if q:
        res.update({"q" : q })
    return res
