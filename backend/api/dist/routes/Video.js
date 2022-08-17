"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const mongoose_1 = require("mongoose");
const videoSchema = new mongoose_1.Schema({
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
});
exports.default = (0, mongoose_1.model)('Video', videoSchema);
