import {Schema, model} from 'mongoose'

const videoSchema = new Schema({
    title: {
        type: String,
        reuired: true,
        trim: true,
    },
    description: {
        type: String,
        reuired: true,
        trim: true,
    },
    url: {
        type: String,
        reuired: true,
        trim: true,
        unique: true,
    }, 
}, {
        versionKey: false,
        timestamps: true,
    },
)

export default model('Video', videoSchema);