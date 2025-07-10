import express from "express"
// import helmet from "helmet";

import { PORT, mongoDBURL } from "./config.js";
import mongoose from "mongoose";  
import { bookModel } from "./models/bookModel.js";

const app = express();
// app.use(helmet());

//Middleware for parsing req body
app.use(express.json())

app.get("/", (req, res) => {
  res.send("Welcome to the Book Store CRM Backend!");
});

// Route for Save a New Book

app.post("/books", async (req, res) =>{
  try{
    if(
        !req.body.bookTitle ||
        !req.body.authorName ||
        !req.body.bookISBN ||
        !req.body.publisher ||
        !req.body.yearPublish

    ){
      return res.status(400).send({
        message: 'Send all required fields: title, authour name,book isbn, publisher, year publish'

      })
    }
    const newBook = {
      bookTitle: req.body.bookTitle,
      authorName: req.body.authorName,
      bookISBN: req.body.bookISBN,
      publisher: req.body.publisher,
      yearPublish: req.body.yearPublishgit 

    };
    const book = await bookModel.create(newBook);
    
    return res.status(201).send(book)

  }catch (error){
    console.log(error.messgae);
    res.status(500).send({message: error.message});

  }

})

//Route for Getting All Books


mongoose
  .connect(mongoDBURL)
  .then( () => {
    console.log('App is connected to DB')
    app.listen(PORT, () => {
      console.log(`Server is running on port ${PORT}`);
    });

  })
  .catch((error) =>{
    console.log(error)
  })