"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const axios_1 = __importDefault(require("axios"));
const app = (0, express_1.default)();
app.use(express_1.default.json());
// Proxy ke Aries (3000)
app.post('/api/chat', async (req, res) => {
    try {
        const response = await axios_1.default.post('http://127.0.0.1:3000/api/chat', req.body);
        res.json(response.data);
    }
    catch (e) {
        res.status(500).json({ error: "Aries Brain Unreachable" });
    }
});
app.listen(3001, () => console.log("🌉 SOVEREIGN BRIDGE 3001 ALIGNED"));
