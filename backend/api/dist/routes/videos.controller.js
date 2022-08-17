"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.updateVideos = exports.deleteVideos = exports.getVideo = exports.getVideos = exports.createVideos = void 0;
const Video_1 = __importDefault(require("./Video"));
const createVideos = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const videoFound = yield Video_1.default.find({ url: req.body.url });
    if (videoFound)
        return res.status(301).json({ message: 'The url already exist' });
    const video = new Video_1.default(req.body);
    const savedVideo = yield video.save();
    res.json(savedVideo);
});
exports.createVideos = createVideos;
const getVideos = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const videos = yield Video_1.default.find();
        return res.json(videos);
    }
    catch (error) {
        res.json(error);
    }
});
exports.getVideos = getVideos;
const getVideo = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const OneVideo = yield Video_1.default.findById(req.params.id);
    if (!OneVideo)
        return res.status(204).json({ message: "The video does not exist" });
    return res.json(OneVideo);
});
exports.getVideo = getVideo;
const deleteVideos = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const deleteV = yield Video_1.default.findByIdAndDelete(req.params.id);
    if (!deleteV)
        return res.status(204).json({ message: "The video does not exist" });
    return res.json(deleteV);
});
exports.deleteVideos = deleteVideos;
const updateVideos = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const updateV = yield Video_1.default.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!updateV)
        return res.status(404).json({ message: "The video does not exist" });
    return res.json(updateV);
});
exports.updateVideos = updateVideos;
