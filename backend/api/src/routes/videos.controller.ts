import { RequestHandler } from "express";
import Video from "./Video";

export const createVideos : RequestHandler = async (req, res) => {

    const videoFound = await Video.find({url: req.body.url})
    if (videoFound) 
        return res.status(301).json({message: 'The url already exist'})

    const video = new Video(req.body)
    const savedVideo = await video.save()
    res.json(savedVideo);
}

export const getVideos : RequestHandler = async (req, res) => {
    try {const videos = await Video.find()
    return res.json(videos)
    }catch(error) {
        res.json(error)
    }
}

export const getVideo : RequestHandler = async (req, res) => {
    const OneVideo = await Video.findById(req.params.id)
    if (!OneVideo) return res.status(204).json({message: "The video does not exist"})
        return res.json(OneVideo)
    }


export const deleteVideos : RequestHandler = async (req, res) => {
    const deleteV = await Video.findByIdAndDelete(req.params.id)
    if (!deleteV) return res.status(204).json({message: "The video does not exist"})
        return res.json(deleteV)
        
}


export const updateVideos : RequestHandler = async (req, res) => {
    const updateV = await Video.findByIdAndUpdate(req.params.id, req.body, {new: true})
    if (!updateV) return res.status(404).json({message: "The video does not exist"})
        return res.json(updateV)
}