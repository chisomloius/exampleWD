import mongoose from "mongoose";


const bookSchema = mongoose.Schema(
    {
        bookTitle: { type: String, required: true,},
        authorName: { type: String, required: true,},
        bookISBN: { type: Number, required: true,},
        publisher: { type: String, required: true,},
        yearPublish: { type: String, required: true,},
        timestamps: { type: String, },

    }
)
export const bookModel = mongoose.model('Cat', { name: bookSchema });