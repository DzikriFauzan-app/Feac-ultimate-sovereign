"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const cors_1 = __importDefault(require("cors"));
const app = (0, express_1.default)();
app.use((0, cors_1.default)());
app.use(express_1.default.json());
app.post('/api/chat', (req, res) => {
    console.log("🧠 ARIES BRAIN PROCESSING:", req.body.message);
    res.json({ response: "Sovereign Intelligence Confirmed: " + req.body.message });
});
app.listen(3000, () => console.log("🧠 ARIES BRAIN 3000 ONLINE"));
