from fastapi import FastAPI, Query, Depends, HTTPException
from sqlalchemy import Column, String, Integer
from typing import Optional, List
from pydantic import BaseModel
from sqlalchemy.orm import Session

from DatabaseConnection import engine, sessionLocal, base

app = FastAPI()


class Books(base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    author = Column(String(255), unique=True, index=True)
    description = Column(String(255), index=True)
    rating = Column(String(255), index=True)


class BookSchema(BaseModel):
    title: str 
    author: str
    description: str
    rating: int


# creates the database tables based on the defined models.

base.metadata.create_all(bind=engine)


#for Database Connection
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/book")
def getBooks(db: Session = Depends(get_db)):
    book = db.query(Books).all()
    return book


@app.post("/book/{title}/{author}/{description}/{rating}")
def addBooks(title: str, author:str,description:str,rating:int,db: Session = Depends(get_db)):
    data = Books(title=title, description=description, author=author, rating=rating) 
    db.add(data)
    db.commit()
    return data


@app.put("/book/{book_id}")
def updateBook(book_id: int, book: BookSchema, db: Session = Depends(get_db)):
    db_book = db.query(Books).filter(Books.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for attr, value in book.dict().items():
        setattr(db_book, attr, value)
    db.commit()
    return db_book


@app.delete("/delete/{author}")
def delete_user(author: str, db: Session = Depends(get_db)):
    book = db.query(Books).filter(Books.author == author).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
