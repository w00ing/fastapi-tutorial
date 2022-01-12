# import uvicorn
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(limit: int = 10, published: bool = False, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {"hey": f"blog published {limit}"}
    else:
        return {"hey": f"blog list {limit}"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id: int, limit=10):
    return {"data": [id, limit]}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
